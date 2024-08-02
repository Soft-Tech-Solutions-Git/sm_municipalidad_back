from flask import Flask
from flask_cors import CORS
from config import Config
from .db.db import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    CORS(app, resources={r"/*": {"origins": "*"}})

    with app.app_context():
        from .models import SliderImage, Subtitle, StoryImage, News, User

        db.create_all()

        # Registrar blueprints
        from .routers.home import home_bp
        app.register_blueprint(home_bp, url_prefix="/home")

        from .routers.news import new_bp
        app.register_blueprint(new_bp, url_prefix="/new")

        from .routers.reu_def import main_bp
        app.register_blueprint(main_bp)

    return app


def reset_db(app):
    with app.app_context():
        db.drop_all()
        db.create_all()
