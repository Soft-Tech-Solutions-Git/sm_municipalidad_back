from flask import Blueprint, request, jsonify

# from app.services import home_service
# from ..models import SliderImage, Subtitle, StoryImage

# from .. import db

main_bp = Blueprint("main_bp", __name__)


@main_bp.route("/")
def index():
    return jsonify({"message": "Esta es una ruta al iniciar la app"})
