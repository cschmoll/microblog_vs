from flask import Blueprint

bp = Blueprint('errors', __name__, template_folder= 'templates')

from app_package.errors import handlers