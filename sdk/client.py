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
            json: Payload for the request.

        Returns:
            Response JSON data or raises an exception.
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.request(method=method, url=url, params=params, json=json)
            response.raise_for_status()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP Error occurred: {http_err}")
            print(f"Response Body: {response.text}")
            raise
        
        if response.status_code == 204:
            return None 
        
        try:
            return response.json()
        except ValueError:
            raise ValueError(f"Failed to parse JSON response for {response.url}: {response.text}")
