from my_app import app


def test_app():
    with app.app.test_client() as client:
        response = client.get("/hello")
        assert response.status_code == 200
        assert response.get_json() == {"hello": "World"}
