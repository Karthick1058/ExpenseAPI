
from flask import Blueprint

expense = Blueprint('expense', __name__)

from . import views