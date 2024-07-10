from flask import Flask
from .db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    from .routers import home
    app.register_blueprint(home.bp)

    from .apis import home_api
    app.register_blueprint(home_api.bp, url_prefix='/api')

    return app

