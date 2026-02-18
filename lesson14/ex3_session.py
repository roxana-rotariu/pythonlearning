import requests
import time

session = requests.Session()
session.headers.update({"User-Agent": "lesson14-session"})

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2"
]

print("=== Using session ===")
for url in urls:
    start = time.time()
    r = session.get(url)
    end = time.time()
    print(f"URL: {url}, status: {r.status_code}, time: {end-start:.4f}s")

print("\n=== Without session ===")
for url in urls:
    start = time.time()
    r = requests.get(url)
    end = time.time()
    print(f"URL: {url}, status: {r.status_code}, time: {end-start:.4f}s")
