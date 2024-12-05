import requests
from typing import Optional

class APIClient:
    def __init__(self, base_url: str, api_key: Optional[str] = None):
        """
        Initializes the API client.
        
        Args:
            base_url: The base URL of the API (e.g., https://api.example.com).
            api_key: The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()

        if self.api_key:
            self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})

    def request(self, method: str, endpoint: str, params: dict = None, json: dict = None):
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
        response = self.session.request(method=method, url=url, params=params, json=json)
        response.raise_for_status()  # Raise an error for HTTP 4xx/5xx
        return response.json()
