import os
from dotenv import load_dotenv

class Config:

    load_dotenv()
  
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ['DB_CONNECTION_STRING']
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['cschmoll@hotmail.de']