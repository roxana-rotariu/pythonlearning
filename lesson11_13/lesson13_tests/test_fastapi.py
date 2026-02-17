from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_sum_route():
    response = client.get("/sum?a=2&b=3")
    assert response.status_code == 200
    data = response.json()
    assert data["result"] == 5
