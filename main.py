from sdk import MySDK
from sdk.models import CreateUserRequest

# Initialize the SDK
sdk = MySDK(base_url="https://api.example.com", api_key="your_api_key")

# Create a user
new_user = sdk.users.create_user(
    CreateUserRequest(name="Alice", email="alice@example.com", age=30)
)
print("Created user:", new_user)

# Get a user by ID
user = sdk.users.get_user(user_id=new_user.id)
print("Fetched user:", user)

# List all users
users = sdk.users.list_users()
print("All users:", users)
