import requests
from unittest.mock import patch

@patch("requests.get")
def test_mock_api(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 10, "title": "mocked"}
    
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)
    
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 10
    assert data["title"] == "mocked"
