from flask import Blueprint

auth = Blueprint('author',__name__)

from . import views, forms