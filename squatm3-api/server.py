from flask import Flask
from flask_redis import FlaskRedis
from flask_restful import Resource, Api
from flask_socketio import SocketIO, send, emit
from flask import Flask, session
from flask_session import Session
import redis, attr, json, threading, uuid
from threading import Lock
from wrapper.classes import job, comm
from wrapper.producer import producer
from wrapper.consumer import consumer
from flask import render_template, current_app, redirect, copy_current_request_context, request
import os
import validators
import eventlet
eventlet.monkey_patch(socket=True)

# initiate the app, Api and redis settings reading from config file
template_dir = os.path.abspath('../squatm3-ui')
app = Flask(__name__, template_folder=template_dir)

app.debug = True
async_mode = 'eventlet'
api = Api(app)


# config file has STATIC_FOLDER='/core/static'
app.static_url_path="../squatm3-ui/static"

# set the absolute path to the static folder
app.static_folder=app.static_url_path

# Setup Session
app.config['SESSION_TYPE'] = 'redis'
app.config['SECRET_KEY'] = 'mysecretrediskey'
app.config['SESSION_REDIS'] = redis.Redis(host='redis', port=6379, password='waddup')
sess = Session()
sess.init_app(app)

# Setup SocketIO
socketio = SocketIO(app)
socketio.init_app(app, async_mode=async_mode, message_queue='redis://:waddup@redis:6379/')


@app.before_first_request
def start_worker():
    def run_job():
        c = consumer
        c.listen_for_commands()
    worker = threading.Thread(target=run_job)
    worker.setDaemon(True)
    worker.start()


def start_reporting(sess_key=None, sid=None):
    '''
        General format of reporting: WORKER_ID#JOB_UUID#{MESSAGE/RESULT}
        Fuction that reads from reporting queue and reports back via websocket
        We need to make sure that the log in the reporting queue is ment for the right user.
        We do this by comparing the job_id and the session key. When we start an attack we create a UUID used as session
        key and as job_id
    '''
    print("Entering start_reporting")
    c = comm.Communication()
    with app.app_context():
        while True:
            socketio.sleep(0.1)
            job = c.redis.rpop(c.channel_reporting)
            if job and sess_key:
                w_id,job_id,msg = job.decode().split("#")   
                if job_id == sess_key:
                    socketio.emit('results', msg, room=sid)
                else:
                    #message not for this client, return it back in the queue
                    c.redis.rpush(c.channel_reporting, job)

@socketio.on('client_connected')
def handle_client_connect_event():
    worker_reporter = threading.Thread(target=start_reporting, kwargs=dict(sess_key=check_session(), sid=request.sid))
    worker_reporter.setDaemon(True)
    worker_reporter.start()
    

@app.route('/')
def index():
    create_session()
    return render_template('index.html', async_mode=socketio.async_mode)
    
@app.errorhandler(404)
def page_not_found(e):
    return 'Aaaaah jammer, not found my friend. Try again!'


@app.errorhandler(500)
def page_not_found(e):
    return 'Ah this is our fault!! The developer is waking up after an automatic call due to this error. We \'ll fix it ASAP!'

@app.errorhandler(400)
def bad_request(e):
    return 'Wrong input my friend'



class GetTheListOfDomainsGeneratedByHomoglyphsComplete(Resource):
    def get(self, domain):
        """
        retrieves all the domains generated by the COMPLETE HOMOGLYPHS attack
        """
        pass

class get_list_domains_generated(Resource):
    def get(self, domain):

        """
        The server receives the attacks in the following format: 
        attacks=Hf,Hc,F,R,add
        if all are selected send the whole list
        """
        if validators.domain(domain) != True:
            return "This is not a valid domain";

        attacks = []
        godaddy = 0
        output = 1
        options = ""

        try:
            if request.args.get('attacks') != None:
                attacks = request.args.get('attacks').split(',')
            godaddy = int(request.args.get('godaddy'))
            output = int(request.args.get('output'))

            commands = ["Hf","Hc","-add","F","R"]
            
            for attack in attacks:
                if attack in commands:
                    options = options + "-" + attack + " "

            if godaddy == 1:
                options = options + "--godaddy "

            if output == 1:
                options = options + "--output=json "

            print (options)

        except Exception as e:
            print(e)
            return "Something went wrong while parsing the query string"
            
        """
            Retrieves all the domains generated by the ALL attacks
            We use the redis producer to push a Job object to the queue. 
            The session key is important as the results from the job are taged with the same session key.
                !!! USER SESSION KEY == JOB ID !!!
        """
        session_key = check_session()
        if session_key:
            c = comm.Communication()
            p = producer
            #create attack
            j = job.Job(session_key, domain)
            #options
            #Define the options for all attacks
            #--output=json -> will return all results in one shot. This means if domains are checked 
            #on GoDaddy it will take ages
            #without --output=json it will return one by one message
            j.options = options
            #command
            p.publish(c.channel_jobs, j.to_json())
            return 'All domains attack'
        else:
            return redirect('/')

api.add_resource(get_list_domains_generated, '/api/<domain>')


#Utils Funcs
def create_session():
    key = str(uuid.uuid4())
    session['key'] = key
    return key

def check_session():
    return session.get('key', None)


#main 
if __name__== '__main__':
    socketio.run(app, host="0.0.0.0", async_mode=async_mode)
