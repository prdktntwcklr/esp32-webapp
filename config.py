import os


class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'very complicated string'
    UPLOAD_FOLDER = 'app/static/files/'
    ALLOWED_EXTENSIONS = ['bin']  # allowed file extensions for uploads
    MAX_CONTENT_LENGTH = 1 * 1000 * 1000  # limit max file sizes to 1MB


class TestingConfig(Config):
    TESTING = True


config = {
    'testing': TestingConfig,
    'default': Config
}
