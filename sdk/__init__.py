from .api_client import APIClient
from .contacts import ContactClient

class SDK:
    def __init__(self, base_url: str, api_key: str):
        """
        Initializes the SDK.

        Args:
            base_url: The base URL of the API.
            api_key: The API key for authentication.
        """
        self.api_client = APIClient(base_url, api_key)
        self.users = ContactClient(self.api_client)