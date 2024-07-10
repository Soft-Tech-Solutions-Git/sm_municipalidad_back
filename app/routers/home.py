from flask import Blueprint, render_template
from ..models import SliderImage, Subtitle, StoryImage
from ..db import db

bp = Blueprint('home', __name__)

@bp.route('/')
def home():
    slider_images = SliderImage.query.all()
    subtitle = Subtitle.query.first()
    story_images = StoryImage.query.all()
    
    slider_images_data = [{'id': img.id, 'image_url': img.image_url} for img in slider_images]
    story_images_data = [{'id': img.id, 'image_url': img.image_url} for img in story_images]
    subtitle_data = {'id': subtitle.id, 'text': subtitle.text} if subtitle else None
    
    return {
        'slider_images': slider_images_data,
        'subtitle': subtitle_data,
        'story_images': story_images_data
    }
