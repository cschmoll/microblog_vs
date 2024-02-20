import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    load_dotenv()
  
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #WTF_CSRF_ENABLED = False
    #SQLALCHEMY_DATABASE_URI = os.environ['DB_CONNECTION_STRING']
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    MAIL_SERVER = os.environ['MAIL_SERVER']
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['admin@reflex82.de', 'cagschmoll@gmail.com', 'cschmoll@hotmail.de']
    MAIL_SERVER_GMAIL = os.environ['MAIL_SERVER_GMAIL']
    MAIL_USERNAME_GMAIL = os.environ.get('MAIL_USERNAME_GMAIL')
    MAIL_PASSWORD_GMAIL = os.environ.get('MAIL_PASSWORD_GMAIL')
    POSTS_PER_PAGE = 2