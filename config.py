class Config():
    ...


class TestingConfig(Config):
    TESTING = True


config = {
    'testing': TestingConfig,
    'default': Config
}
