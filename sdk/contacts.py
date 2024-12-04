from typing import List
from .api_client import APIClient
from .models import User, CreateUserRequest, CreateUserResponse

class ContactClient:
    def __init__(self, api_client: APIClient):
        """
        Initializes the UserClient.

        Args:
            api_client: An instance of the base API client.
        """
        self.api_client = api_client

    def create_contact(self, user_data: CreateUserRequest) -> CreateUserResponse:
        """
        Creates a new user.

        Args:
            user_data: Data for creating the user.

        Returns:
            A response containing the created user's details.
        """
        response = self.api_client.request("POST", "/users", data=user_data.dict())
        return CreateUserResponse(**response)
    
    def list_contacts(self) -> List[User]:
        """
        Retrieves a list of users.

        Returns:
            A list of User objects.
        """
        response = self.api_client.request("GET", "/users")
        return [User(**user) for user in response]


    def get_contact(self, user_id: int) -> User:
        """
        Retrieves a user by ID.

        Args:
            user_id: The ID of the user to retrieve.

        Returns:
            A User object.
        """
        response = self.api_client.request("GET", f"/users/{user_id}")
        return User(**response)
    
    def modify_contact(self, user_id: int) -> User:
        """
        Retrieves a user by ID.

        Args:
            user_id: The ID of the user to retrieve.

        Returns:
            A User object.
        """
        response = self.api_client.request("GET", f"/users/{user_id}")
        return User(**response)
    
    def remove_contact(self, user_id: int) -> User:
        """
        Retrieves a user by ID.

        Args:
            user_id: The ID of the user to retrieve.

        Returns:
            A User object.
        """
        response = self.api_client.request("GET", f"/users/{user_id}")
        return User(**response)
    
    