from starlette.testclient import TestClient


def test_swagger_endpoint(app_client: TestClient):
    response = app_client.get("/swagger")
    assert response.status_code == 200


def test_swagger_json_endpoint(app_client: TestClient):
    response = app_client.get("/swagger.json")
    assert response.status_code == 200
