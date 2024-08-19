def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<h1>ESP32 Binary Analyzer</h1>" in response.data
