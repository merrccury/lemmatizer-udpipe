FROM python:3.9-alpine

RUN apk add build-base

RUN python3 -m pip install --upgrade pip

WORKDIR app

COPY app .

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "-w 4", "-b", "0.0.0.0:8000", "app:app"]
