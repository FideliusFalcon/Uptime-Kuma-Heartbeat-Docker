FROM python:slim-buster
WORKDIR /usr/src/app
COPY src/ ./

RUN python -m pip install -r requirements.txt

CMD ["python", "-u", "heartbeat.py"]