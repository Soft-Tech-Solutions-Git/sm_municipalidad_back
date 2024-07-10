# app/apis/__init__.py

from flask import Blueprint

bp = Blueprint('api', __name__)

# Importar el módulo de API para registrar sus rutas en el blueprint
from . import home_api

# Ahora `bp` contendrá todas las rutas definidas en `home_api.py`
