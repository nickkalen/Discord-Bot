FROM python:3.6-alpine
COPY requirements.txt requirements.txt
COPY movies.py movies.py
COPY passwords.py passwords.py
RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["./movies.py"]