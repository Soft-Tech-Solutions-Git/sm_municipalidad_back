from ..models import SliderImage
from ..db.db import db


def add_slider_image(image_url):
    new_image = SliderImage(image_url=image_url)
    db.session.add(new_image)
    db.session.commit()
    return new_image


def get_slider_images():
    return SliderImage.query.all()


def update_slider_image(image_id, image_url):
    image = SliderImage.query.get(image_id)
    if not image:
        return None
    image.image_url = image_url
    db.session.commit()
    return image


def delete_slider_image(image_id):
    image = SliderImage.query.get(image_id)
    if not image:
        return None
    db.session.delete(image)
    db.session.commit()
    return image
