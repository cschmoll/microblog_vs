from flask import Blueprint

bp = Blueprint('search', __name__, template_folder= 'templates')

from app_package.search import search