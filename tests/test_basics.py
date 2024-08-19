def test_app_is_testing(app):
    assert app.config['TESTING']
