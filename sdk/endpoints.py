from .client import APIClient
from .models import Contact, ContactListResponse, Message, MessagesResponse
from typing import Optional

class APIEndpoints:
    def __init__(self, client: APIClient):
        self.client = client

    # MESSAGE ENDPOINTS

    def send_message(self, from_: str, to: str, content: str) -> Message:
        """
        Send a new message.

        Args:
            from_ (str): Sender ID.
            to (str): Recipient id.
            content (str): Message content.

        Returns:
            Message: Parsed response as a Pydantic model.
        """
        payload = {
            "from": from_,
            "to": {
                "id": to
            },
            "content": content,
        }
        response = self.client.request(
            method="POST",
            endpoint="/messages",
            json=payload,
        )
        return Message.model_validate(response)

    def get_messages(self, page: Optional[int] = None, per_page: Optional[int] = None) -> MessagesResponse:
        """
        Fetch messages with pagination.

        Args:
            page (int): Page number.
            per_page (int): Number of messages per page.

        Returns:
            MessagesResponse: Parsed response as a Pydantic model.
        """
        params = {}

        if page:
            params["page"] = page
        if page:
            params["per_page"] = per_page

        response = self.client.request(
            method="GET",
            endpoint="/messages",
            params=params,
        )
        return MessagesResponse.model_validate(response)
    
    def get_message_by_id(self, msg_id: str) -> Message:
        """
        Fetch details of a specific message.

        Args:
            msg_id (str): ID of the message.

        Returns:
            Message: Parsed response as a Pydantic model.
        """
        response = self.client.request(
            method="GET",
            endpoint=f"/messages/{msg_id}",
        )
        return Message.model_validate(response)

    # CONTACT ENDPOINTS

    def get_contacts(self, page: Optional[int] = None, per_page: Optional[int] = None) -> ContactListResponse:
        """
        Fetch a list of contacts with pagination.

        Args:
            page (int): Page number.
            per_page (int): Number of contacts per page.

        Returns:
            ContactListResponse: Parsed response as a Pydantic model.
        """
        params = {}

        if page:
            params["page"] = page
        if page:
            params["per_page"] = per_page

        response = self.client.request(
            method="GET",
            endpoint="/contacts",
            params=params,
        )
        return ContactListResponse.model_validate(response)

    def get_contact(self, contact_id: str) -> Contact:
        """
        Fetch details of a specific contact.

        Args:
            contact_id (str): ID of the contact.

        Returns:
            ContactResponse: Parsed response as a Pydantic model.
        """
        response = self.client.request(
            method="GET",
            endpoint=f"/contacts/{contact_id}",
        )
        return Contact.model_validate(response)

    def create_contact(self, name: str, phone: str) -> Contact:
        """
        Create a new contact.

        Args:
            name (str): Contact name.
            phone (str): Contact phone number.

        Returns:
            Contact: The created contact as a Pydantic model.
        """
        payload = {"name": name, "phone": phone}
        response = self.client.request(
            method="POST",
            endpoint="/contacts",
            json=payload,
        )
        return Contact.model_validate(response)

    def update_contact(self, contact_id: str, name: str, phone: str) -> Contact:
        """
        Update an existing contact.

        Args:
            contact_id (str): ID of the contact to update.
            name (str): New contact name.
            phone (str): New contact phone number.

        Returns:
            Contact: The updated contact as a Pydantic model.
        """
        payload = {"name": name, "phone": phone}
        response = self.client.request(
            method="PATCH",
            endpoint=f"/contacts/{contact_id}",
            json=payload,
        )
        return Contact.model_validate(response)

    def delete_contact(self, contact_id: str) -> None:
        """
        Delete a specific contact.

        Args:
            contact_id (str): ID of the contact to delete.

        Returns:
            None
        """
        self.client.request(
            method="DELETE",
            endpoint=f"/contacts/{contact_id}",
        )
