from flask import Blueprint, request, jsonify

from app.services import home_service

home_bp = Blueprint("home_api", __name__)


# SLIDER
@home_bp.route("/add", methods=["POST"])
def add_slider_image():
    files = request.files
    author_id = int(request.form.get("author_id"))
    display = request.form.get("display")
    home_service.add_slider_image(author_id, files, display)
    return jsonify({"message": "Slider image added"}), 200


@home_bp.route("/getslider/<display>", methods=["GET"])
def get_slider_image(display):
    sliders = home_service.get_slider_image(display)
    if sliders is not None:
        return jsonify({"sliders": sliders}), 200


# SUBTITLE
@home_bp.route("/subtitle", methods=["POST"])
def add_subtitle():
    author_id = int(request.form.get("author_id"))
    text = request.form.get("text")
    home_service.add_subtitle(author_id, text)
    return jsonify({"message": "Subtitle added"}), 200


@home_bp.route("/getsubtitle", methods=["GET"])
def get_subtitle():
    subtitle = home_service.get_subtitle()
    return jsonify({"subtitle": subtitle}), 200


# HISTORIA
@home_bp.route("/story", methods=["POST"])
def add_story():
    file = request.files["image"]
    author_id = int(request.form.get("author_id"))
    fecha_hora_baja = request.form.get("fecha_hora_baja")
    home_service.add_story(file, author_id, fecha_hora_baja)
    return jsonify({"message": "Story image added"}), 200


@home_bp.route("/getstory", methods=["GET"])
def get_story():
    story = home_service.get_story()
    return jsonify({"story: ": story}), 200
