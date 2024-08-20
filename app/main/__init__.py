from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, filters  # noqa: F401, E402
