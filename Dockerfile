FROM python:3.14-slim

WORKDIR /code

ADD ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD ./src/* .

CMD [ "python3", "psychologist.py" ]
