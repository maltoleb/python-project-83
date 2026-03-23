from page_analyzer.app import app


def test_index():
    app.config["Testing"] = True
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
