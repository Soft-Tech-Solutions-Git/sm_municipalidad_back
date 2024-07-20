from flask import Flask
from config import Config
from .db.db import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from .models import SliderImage, Subtitle, StoryImage

        db.create_all()

        # Registrar blueprints
        from .routers.home import home_bp

        app.register_blueprint(home_bp, url_prefix="/home")

        from .routers.reu_def import main_bp

        app.register_blueprint(main_bp)

    return app
