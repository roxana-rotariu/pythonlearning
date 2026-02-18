import requests
from requests.adapters import HTTPAdapter, Retry

class JsonPlaceholderClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        # Creează un session pentru toate request-urile
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "User-Agent": "JsonPlaceholderClient/1.0"
        })
        # Retry logic pentru erori temporare
        retries = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["GET", "POST"]
        )
        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        self.timeout = 5  # timeout în secunde

    def get_post(self, post_id):
        url = f"{self.BASE_URL}/posts/{post_id}"
        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    def create_post(self, data):
        url = f"{self.BASE_URL}/posts"
        response = self.session.post(url, json=data, timeout=self.timeout)
        response.raise_for_status()
        return response.json()
