"""
Defines the "main" blueprint for the Flask application.
"""

# pylint: disable=wrong-import-position

from flask import Blueprint

main = Blueprint("main", __name__)

from . import views  # noqa: F401, E402
