from flask import request, current_app
import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from logging.handlers import SMTPHandler 
from flask_mail import Mail
from flask_moment import Moment
from flask_babel import Babel
from flask_babel import lazy_gettext as _l
from elasticsearch import Elasticsearch
#import smtplib


def get_locale():
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
moment = Moment()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')
babel = Babel()

def create_app(config_class=Config):

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    babel.init_app(app, locale_selector=get_locale)

    app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
        if app.config['ELASTICSEARCH_URL'] else None

    from app_package.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app_package.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from app_package.search import bp as search_bp
    app.register_blueprint(search_bp)

    from app_package.main import bp as main_bp
    app.register_blueprint(main_bp)

    if not app.debug and not app.testing:
    #versenden einer Mail über mein Gmail Konto
    #server = smtplib.SMTP(app.config['MAIL_SERVER_GMAIL'], app.config['MAIL_PORT'])
    #server.starttls()
    #server.login(app.config['MAIL_USERNAME_GMAIL'], app.config['MAIL_PASSWORD_GMAIL'])
    #server.sendmail(app.config['MAIL_USERNAME_GMAIL'], app.config['ADMINS'], 'Mail sent from program')

        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                fromaddr='no-reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'], 
                subject='Microblog Failure',
                credentials=auth, secure=secure)
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
            os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                    backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info(_l('Microblog startup'))

    return app

from app_package import models