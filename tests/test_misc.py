from app.main.views import is_file_allowed


def test_is_file_allowed(app):
    allowed_extensions = app.config["ALLOWED_EXTENSIONS"]

    assert is_file_allowed("file.bin", allowed_extensions)
    assert is_file_allowed("file.test.bin", allowed_extensions)
    assert not is_file_allowed("file.elf", allowed_extensions)
    assert not is_file_allowed("file.bin.bak", allowed_extensions)
    assert not is_file_allowed("file", allowed_extensions)
    assert not is_file_allowed("", allowed_extensions)
