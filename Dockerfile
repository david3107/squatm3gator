FROM python:3.7.2-alpine3.9
RUN apk --no-cache update 
RUN apk --no-cache upgrade
RUN apk --no-cache add git
RUN apk --no-cache add make build-base
RUN apk --no-cache add gcc
COPY . /app
WORKDIR /app/squatm3-api
RUN pip3 install -r docker-requirements.txt
ENV FLASK_APP=server.py
ENV FLASK_ENV=development
CMD ["python3", "-m", "flask", "run", "--host", "0.0.0.0" ]
