import requests
from requests.adapters import HTTPAdapter, Retry

url = "https://invalid.url.typicode.com"  # URL invalid pentru test

session = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[502, 503, 504])
adapter = HTTPAdapter(max_retries=retries)
session.mount("http://", adapter)
session.mount("https://", adapter)

try:
    response = session.get(url)
except requests.exceptions.RequestException as e:
    print("Request failed after retries:", e)
