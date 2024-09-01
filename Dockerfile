FROM python:3.8.10

WORKDIR /code

ADD ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD ./src/* .

CMD [ "python3", "psychologist.py" ]
