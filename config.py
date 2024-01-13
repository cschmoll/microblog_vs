import os
from dotenv import load_dotenv

class Config:

    load_dotenv()
  
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #WTF_CSRF_ENABLED = False
    #SQLALCHEMY_DATABASE_URI = os.environ['DB_CONNECTION_STRING'] or 'sqlite:///' + os.path.join(basedir, 'app.db')
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DB_CONNECTION_STRING')
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://careersv2_user:1VllDv0yWPA2C4pV6tqqMLgKQyHuhjv5@dpg-cl76m2qvokcc73bvdve0-a.frankfurt-postgres.render.com/careersv2'
    SQLALCHEMY_DATABASE_URI = os.environ['DB_CONNECTION_STRING']
    print('URI : ', SQLALCHEMY_DATABASE_URI)
    #MAIL_SERVER = os.environ.get('MAIL_SERVER')
    #MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    #MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    #MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    #MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT = '587'
    MAIL_USE_TLS = 'STARTTLS'
    MAIL_USERNAME = 'cschmoll@hotmail.de'
    MAIL_PASSWORD = '12345678'
    ADMINS = ['cschmoll@hotmail.de']