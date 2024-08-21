from pathlib import Path

# get the resources folder in the tests folder
resources = Path(__file__).parent / "resources"


def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<h1>ESP32 Binary Analyzer</h1>" in response.data


def test_bin_file(client):
    response = client.post(
        '/', data=dict({"file": (resources / 'hello_world.bin').open('rb')})
    )

    assert response.status_code == 200
    assert b"Detected image type: ESP32" in response.data


def test_elf_file(client):
    response = client.post(
        '/', data=dict({'file': (resources / 'hello_world.elf').open('rb')}),
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Invalid file type (allowed: bin)" in response.data


def test_fake_bin_file(client):
    response = client.post(
        '/', data=dict({'file': (resources / 'fake_bin.bin').open('rb')})
    )

    assert response.status_code == 200
    assert b"This is not a valid image" in response.data


def test_no_file(client):
    response = client.post(
        '/', data=dict({'file': None}), follow_redirects=True
    )

    assert response.status_code == 200
    assert b"No file found" in response.data


def test_large_file(client):
    response = client.post(
        '/', data=dict({'file': (resources / 'large_file.bin').open('rb')}),
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"File is too large (max: 1.0MB)" in response.data
