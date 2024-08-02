from flask import current_app
from sqlalchemy import text

from app.functions import convert_image_to_base64, save_and_compress_image
from ..models import SliderImage, Subtitle
from ..db.db import db


# SLIDER
def add_slider_image(author_id, files, display):
    upload_folder = current_app.config["UPLOAD_FOLDER"]

    for key in files:
        if "image" in key:
            file = files[key]
            image_path = save_and_compress_image(file, upload_folder)
            if image_path:
                img_n = {
                    "image_url": image_path,
                    "user_id": author_id,
                    "display": display,
                }
                new_slider_img = SliderImage(**img_n)
                db.session.add(new_slider_img)
                db.session.commit()


def get_slider_image(display):
    procedure_call = text("CALL GetSliderImages(:display)")
    result = db.session.execute(procedure_call, {"display": display}).mappings().all()

    if not result:
        return None

    slider = []
    for row in result:
        image_path = row["image_path"]
        image_base64 = convert_image_to_base64(image_path) if image_path else None

        slider_data = {
            "id": row["slider_id"],
            "image": image_base64,
        }
        slider.append(slider_data)

    return slider


# def update_slider_image(image_id, image_url):
#     image = SliderImage.query.get(image_id)
#     if not image:
#         return None
#     image.image_url = image_url
#     db.session.commit()
#     return image


# def delete_slider_image(image_id):
#     image = SliderImage.query.get(image_id)
#     if not image:
#         return None
#     db.session.delete(image)
#     db.session.commit()
#     return image


# SUBTITLE
def add_subtitle(author_id, text):
    subtitle = {"text": text, "user_id": author_id}
    new_subtitle = Subtitle(**subtitle)
    db.session.add(new_subtitle)
    db.session.commit()


def get_subtitle():
    procedure_call = text("CALL GetSubtitle")
    result = db.session.execute(procedure_call).mappings().all()
    row = result[0]
    return row["text"]


# HISTORIA
