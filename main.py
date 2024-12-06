from sdk import APIClient, APIEndpoints
import os
from dotenv import load_dotenv

load_dotenv() 


# Initialize the client
client = APIClient(base_url=os.getenv("BASE_URL", "http://localhost:3000"), api_key=os.getenv("API_KEY", "there-is-no-key"))

# Initialize API endpoints
api = APIEndpoints(client)

new_contact1 = api.create_contact(name="Carmack", phone="+11234567890")
print(f"Created Contact 1: {new_contact1.id}")

new_contact2 = api.create_contact(name="Romero", phone="+10987654321")
print(f"Created Contact 2: {new_contact2.id}")
print("-------------------------------------------")

new_message = api.send_message(
    from_=new_contact1.id,
    to=new_contact2.id,
    content="Hello there!",
)
print(f"Message sent with ID: {new_message.id}")
print("Current messages: ")

response = api.get_messages(page=1, per_page=10)
for message in response.messages:
    print(f"-> ID: {message.id} From: {message.from_}, To: {message.to} Content: {message.content}")

print("-------------------------------------------")

print("Current contacts: ")
contacts = api.get_contacts(page=1, per_page=10)
for contact in contacts.contacts:
    print(f"-> ID: {contact.id} Contact Name: {contact.name}, Phone: {contact.phone}")

print("-------------------------------------------")

contact = api.get_contact(contact_id=new_contact1.id)
print(f"Contact: {contact.name}, Phone: {contact.phone}")

updated_contact = api.update_contact(contact_id=new_contact1.id, name=new_contact1.name, phone="+11234567898")
print(f"Updated Contact Phone: {updated_contact.phone}")

contact = api.get_contact(contact_id=new_contact1.id)
print(f"Contact: {contact.name}, Phone: {contact.phone}")

api.delete_contact(contact_id=updated_contact.id)
print("Contact deleted successfully.")