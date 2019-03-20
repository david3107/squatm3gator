FROM python:3.7.2-alpine3.9
ENV TZ=Europe/Berlin
RUN apk --no-cache update 
RUN apk --no-cache upgrade
RUN apk --no-cache add --virtual .build-deps gcc musl-dev
RUN apk --no-cache add tzdata && cp -r -f /usr/share/zoneinfo/$TZ /etc/localtime
RUN apk --no-cache add coreutils
COPY . /app
WORKDIR /app/squatm3-api
RUN pip3 install -r requirements.txt
ENV FLASK_APP=server.py
ENV FLASK_ENV=development
CMD ["python3", "-m", "flask", "run", "--host", "0.0.0.0" ]
