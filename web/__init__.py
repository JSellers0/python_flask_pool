from flask import Flask
from web.config import Config

from web.routes import pool

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(pool)

    return app