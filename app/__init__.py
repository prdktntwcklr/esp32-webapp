"""
Creates and configures the Flask application instance.
"""

# pylint: disable=import-outside-toplevel

from flask import Flask
from config import config


def create_app(config_name="default"):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
