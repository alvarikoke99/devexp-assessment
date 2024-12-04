from typing import List, Optional
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
            sender_number: The sender's phone number.
            recipient_id: The unique identifier of a Contact.
            content: The text content of the message.

        Returns:
            A response containing the created message details.
        """
        try:
            request_body = CreateMessageRequest(from_=sender_number, to=recipient_id, content=content)
        except ValidationError as e:
            print(e.errors())

        try:
            response = self.api_client.request("POST", "/messages", data=request_body)
        except HTTPError as httpe:
            print(httpe.errors())

        return Message(**response)


    def get_mesage(self, msg_id: str) -> User:
        """
        Retrieves a message by ID.

        Args:
            msg_id: The unique ID of the message to retrieve.

        Returns:
            A Message object.
        """
        try:
            response = self.api_client.request("GET", f"/messages/{msg_id}")
        except HTTPError as httpe:
            print(httpe.errors())

        return Message(**response)
    
    def list_messages(self, page: Optional[int] = None, limit: Optional[int] = None) -> List[Message]:
        """
        Retrieves a list of messages.

        Returns:
            A list of Message objects.
        """
        
        params = {}

        if page:
            if not isinstance(page, int) or page <= 0:
                raise ValueError(f"Invalid value for parameter \'page\': {page}. Must be a positive integer.")
            params["page"] = page

        if limit:
            if not isinstance(limit, int) or page <= 0:
                raise ValueError(f"Invalid value for parameter \'limit\': {limit}. Must be a positive integer.")
            params["limit"] = limit

        try:
            response = self.api_client.request("GET", "/messages", params=params)
        except HTTPError as httpe:
            print(httpe.errors())

        return [Message(**msg) for msg in response]
    