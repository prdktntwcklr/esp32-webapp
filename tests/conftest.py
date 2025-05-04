"""
Pytest fixtures for setting up the Flask application and test environment.
"""

import pytest

from app import create_app


# pylint: disable=redefined-outer-name

@pytest.fixture()
def app():
    app = create_app("testing")

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def jinja(app):
    return app.jinja_env
