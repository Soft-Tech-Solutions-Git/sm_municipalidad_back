from flask import Blueprint, request, jsonify

from app.services import home_service
from ..models import SliderImage, Subtitle, StoryImage

from .. import db

home_bp = Blueprint("home_api", __name__)


@home_bp.route("/")
def index():
    return jsonify({"message": "Esto es home_bp"})


@home_bp.route("/slider", methods=["POST"])
def add_slider_image():
    data = request.json
    new_image = home_service.add_slider_image(data["image_url"])
    return jsonify({"message": "Slider image added", "id": new_image.id}), 201


# # CRUD para SliderImage
# @home_bp.route('/slider', methods=['POST'])
# def add_slider_image():
#     data = request.json
#     new_image = SliderImage(image_url=data['image_url'])
#     db.session.add(new_image)
#     db.session.commit()
#     return jsonify({"message": "Slider image added"}), 201


@home_bp.route("/slider/<int:id>", methods=["PUT"])
def update_slider_image(id):
    data = request.json
    image = SliderImage.query.get(id)
    if image is None:
        return jsonify({"error": "Not found"}), 404
    image.image_url = data["image_url"]
    db.session.commit()
    return jsonify({"message": "Slider image updated"}), 200


@home_bp.route("/slider/<int:id>", methods=["DELETE"])
def delete_slider_image(id):
    image = SliderImage.query.get(id)
    if image is None:
        return jsonify({"error": "Not found"}), 404
    db.session.delete(image)
    db.session.commit()
    return jsonify({"message": "Slider image deleted"}), 200


# CRUD para Subtitle
@home_bp.route("/subtitle", methods=["POST"])
def add_subtitle():
    data = request.json
    new_subtitle = Subtitle(text=data["text"])
    db.session.add(new_subtitle)
    db.session.commit()
    return jsonify({"message": "Subtitle added"}), 201


@home_bp.route("/subtitle/<int:id>", methods=["PUT"])
def update_subtitle(id):
    data = request.json
    subtitle = Subtitle.query.get(id)
    if subtitle is None:
        return jsonify({"error": "Not found"}), 404
    subtitle.text = data["text"]
    db.session.commit()
    return jsonify({"message": "Subtitle updated"}), 200


@home_bp.route("/subtitle/<int:id>", methods=["DELETE"])
def delete_subtitle(id):
    subtitle = Subtitle.query.get(id)
    if subtitle is None:
        return jsonify({"error": "Not found"}), 404
    db.session.delete(subtitle)
    db.session.commit()
    return jsonify({"message": "Subtitle deleted"}), 200


# CRUD para StoryImage
@home_bp.route("/stories", methods=["POST"])
def add_story_image():
    data = request.json
    new_image = StoryImage(image_url=data["image_url"])
    db.session.add(new_image)
    db.session.commit()
    return jsonify({"message": "Story image added"}), 201


@home_bp.route("/stories/<int:id>", methods=["PUT"])
def update_story_image(id):
    data = request.json
    image = StoryImage.query.get(id)
    if image is None:
        return jsonify({"error": "Not found"}), 404
    image.image_url = data["image_url"]
    db.session.commit()
    return jsonify({"message": "Story image updated"}), 200


@home_bp.route("/stories/<int:id>", methods=["DELETE"])
def delete_story_image(id):
    image = StoryImage.query.get(id)
    if image is None:
        return jsonify({"error": "Not found"}), 404
    db.session.delete(image)
    db.session.commit()
    return jsonify({"message": "Story image deleted"}), 200
