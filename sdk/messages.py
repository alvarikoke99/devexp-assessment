from typing import List
from .api_client import APIClient
from .models import User, CreateMessageRequest, Message
from pydantic import ValidationError
from requests import HTTPError

class MessageClient:
    def __init__(self, api_client: APIClient):
        """
        Initializes the UserClient.

        Args:
            api_client: An instance of the base API client.
        """
        self.api_client = api_client

    def create_message(self, sender_number: str, recipient_id: str, content: str) -> Message:
        """
        Creates a new message

        Args:
            sender_number: The sender's phone number
            recipient_id: The unique identifier of a Contact
            content: The text content of the message

        Returns:
            A response containing the created user's details.
        """
        request_body = {
            "from": sender_number,
            "content": content,
            "to": {
                "id": recipient_id
            }
        }

        try:
            response = self.api_client.request("POST", "/users", data=request_body)
        except HTTPError as httpe:
            print(httpe.errors())

        return Message(**response)


    def get_mesage(self, user_id: int) -> User:
        """
        Retrieves a user by ID.

        Args:
            user_id: The ID of the user to retrieve.

        Returns:
            A User object.
        """
        response = self.api_client.request("GET", f"/users/{user_id}")
        return User(**response)
    
    def list_messages(self) -> List[User]:
        """
        Retrieves a list of users.

        Returns:
            A list of User objects.
        """
        response = self.api_client.request("GET", "/users")
        return [User(**user) for user in response]
    