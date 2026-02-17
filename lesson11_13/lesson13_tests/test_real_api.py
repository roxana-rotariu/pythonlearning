import requests

def test_real_api():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)
    
    assert response.status_code == 200
    
    data = response.json()
    assert "id" in data
    assert "title" in data
