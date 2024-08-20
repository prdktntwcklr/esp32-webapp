import os


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very complicated string'
    UPLOAD_FOLDER = 'app/static/files/'


class TestingConfig(Config):
    TESTING = True


config = {
    'testing': TestingConfig,
    'default': Config
}
