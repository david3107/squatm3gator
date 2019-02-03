## About Squatm3gator


<img src="ui.png"/> <br><br>
Squatm3gator is a complete web solution based on the python tool squatm3, designed to enumerate available domains generated modifying the original domain name through different techniques:

-	Substitution attacks
-	Flipping attack
- 	Homoglyph attack fast (execute a fast homoglyph attack, mutating only one letter at the time)
-   Homoglyph attack complete (generates all the possible combinations)


The tool is meant to help penetration testers to identify domains to be used in phishing attack simulations and security analysts to detect and prevent cybersquatting attacks.


## Architecture

<img src="architecture.png"/> <br> 


## Installation


### Clone the repo
```
git clone https://github.com/david3107/squatm3gator.git

```

### Install the dependencies in squatme-api

```
pip3 install -r requirements.txt

```

### Spin up a Redis container

One way to get it quickly done is to use the bitnami/redis docker:
```
docker run -e REDIS_PASSWORD=waddup --name squatme-redis -p 6379:6379 bitnami/redis

```

### Setup flask and run the server

```
cd squatm3-api/
export FLASK_APP=server.py   
python3 -m flask run

```

## Recommended Python Version:

Squatm3gator currently supports only **Python 3** 


## Dependencies:

Squatm3gator heavily depends on 

``` 
tld==0.9.1
attrs==18.2.0
redis==2.10.6
requests==2.19.1
simplejson==3.16.0
Flask_RESTful==0.3.6
Flask==1.0.2
Flask_Session==0.3.1
homoglyphs==1.3.1
validators==0.12.2
Flask_SocketIO==3.0.2
attr==0.3.1
Flask_And_Redis==0.7
eventlet

``` 

python modules.

These dependencies can be installed using the requirements file:

- Installation on Windows:
```
c:\python33\python.exe -m pip install -r requirements.txt --user
```
- Installation on Linux and MacOS
```
pip3 install -r requirements.txt --user
```

## Usage

Run the app on browsing on: 

```
http://localhost:5000
```

## License

Squatm3gator is licensed under the GNU GPL license.


## Version
Current version is 1.1

## Presented at

[Black Hat Arsenal Europe 2018](https://www.blackhat.com/eu-18/arsenal/schedule/index.html#squatm-cybersquatting-made-easy-13319)
       
