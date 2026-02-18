from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_login():
    # Register
    r = client.post("/users/register", json={"email":"x@y.com","password":"123"})
    assert r.status_code == 200
    assert r.json()["email"] == "x@y.com"

    # Login
    r2 = client.post("/users/login", json={"email":"x@y.com","password":"123"})
    assert r2.status_code == 200
    assert "token" in r2.json()
