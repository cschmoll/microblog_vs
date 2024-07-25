FROM python:slim

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn pymysql cryptography
#RUN pip install gunicorn psycopg2 cryptography

COPY app_package app_package
COPY migrations migrations
COPY microblog.py config.py boot.sh ./
RUN chmod a+x boot.sh

ENV FLASK_APP microblog.py
#RUN flask translate compile

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]