from sdk import APIClient, APIEndpoints

# Initialize the client
client = APIClient(base_url="https://localhost:3000", api_key="there-is-no-key")

# Initialize API endpoints
api = APIEndpoints(client)

new_contact1 = api.create_contact(name="Carmack", phone="+987654321", email="johnCarmack@idsoft.com")
print(f"Created Contact ID: {new_contact1.id}")

new_contact2 = api.create_contact(name="Romero", phone="+123456789", email="johnRomero@idsoft.com")
print(f"Created Contact ID: {new_contact2.id}")

new_message = api.send_message(
    from_=new_contact1.id,
    to={"name": "Romero", "phone": "+1234567890", "id": new_contact2.id},
    content="Hello there!",
)
print(f"Message sent with ID: {new_message.id}")

response = api.get_messages(page=1, per_page=10)
for message in response.messages:
    print(f"From: {message.from_}, Content: {message.content}")

contacts = api.get_contacts(page=1, per_page=10)
for contact in contacts.contacts:
    print(f"Contact Name: {contact.name}, Phone: {contact.phone}")

contact = api.get_contact(contact_id=new_contact1.id)
print(f"Contact: {contact.contact.name}, Email: {contact.contact.email}")

updated_contact = api.update_contact(contact_id=new_contact1.id, phone="+789654321")
print(f"Updated Contact Phone: {updated_contact.phone}")

api.delete_contact(contact_id=new_contact1.id)
print("Contact deleted successfully.")