FROM python:3.7

WORKDIR /app/api
COPY . /app/api

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "server.py"]
