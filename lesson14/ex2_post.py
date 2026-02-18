import requests

url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Hello",
    "body": "This is Roxana",
    "userId": 1
}

response = requests.post(url, json=payload)
print("Status code:", response.status_code)
print("Response JSON:", response.json())
