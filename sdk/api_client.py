import requests
from typing import Optional

class APIClient:
    def __init__(self, base_url: str, api_key: str):
        """
        Initializes the API client.
        
        Args:
            base_url: The base URL of the API (e.g., https://api.example.com).
            api_key: The API key for authentication.
        """
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})

    def request(self, method: str, endpoint: str, params: Optional[dict] = None, data: Optional[dict] = None) -> dict:
        """
        Sends an HTTP request.

        Args:
            method: HTTP method (GET, POST, etc.).
            endpoint: API endpoint (relative path).
            params: Query parameters for the request.
            data: Payload for the request.

        Returns:
            Response JSON data or raises an exception.
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, params=params, json=data)
        response.raise_for_status()
        return response.json()
