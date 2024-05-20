from flask import Blueprint

bp = Blueprint('bp', __name__)

from .routers import home