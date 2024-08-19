def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"<h1>Hello World!</h1>" in response.data
