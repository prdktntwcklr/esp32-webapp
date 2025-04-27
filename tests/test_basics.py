"""
Confirms that the test app is started in "TESTING" mode.
"""


def test_app_is_testing(app):
    assert app.config['TESTING']
