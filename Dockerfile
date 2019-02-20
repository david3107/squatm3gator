FROM python:3.7.2-alpine3.9
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
COPY . /app
WORKDIR /app/squatm3-api
RUN pip3 install -r requirements.txt
ENV FLASK_APP=server.py
ENV FLASK_ENV=development
CMD ["python3", "-m", "flask", "run", "--host", "0.0.0.0" ]
