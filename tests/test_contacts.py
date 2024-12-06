import pytest
import responses
import os
from sdk.client import APIClient
from sdk.endpoints import APIEndpoints
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://localhost:3000")

# Fixtures
@pytest.fixture
def client():
    return APIClient(base_url=BASE_URL, api_key=os.getenv("API_KEY", "there-is-no-key"))

@pytest.fixture
def api(client):
    return APIEndpoints(client)

# Test Cases for Contacts

@responses.activate
def test_create_contact(api):
    responses.add(
        responses.POST,
        BASE_URL + "/contacts",
        json={"id": "1", "name": "Dr. Eli Vance", "phone": "+1234567890"},
        status=201,
    )

    contact = api.create_contact(name="Dr. Eli Vance", phone="+1234567890")
    assert contact.id == "1"
    assert contact.name == "Dr. Eli Vance"

@responses.activate
def test_get_contacts(api):
    responses.add(
        responses.GET,
        BASE_URL + "/contacts",
        json={
            "contacts": [
                {"id": "1", "name": "Barney Calhoun", "phone": "+1234567890"},
                {"id": "2", "name": "Dr. Wallace Breen", "phone": "+9876543210"},
            ],
            "pageNumber": 0,
            "pageSize": 0
        },
        status=200,
    )

    contacts = api.get_contacts()
    assert len(contacts.contacts) == 2
    assert contacts.contacts[0].name == "Barney Calhoun"

@responses.activate
def test_update_contact(api):
    responses.add(
        responses.PATCH,
        BASE_URL + "/contacts/1",
        json={"id": "1", "name": "The Administrator", "phone": "+1234567890"},
        status=200,
    )

    contact = api.update_contact(contact_id="1", name="The Administrator", phone="+1234567890")
    assert contact.name == "The Administrator"

@responses.activate
def test_delete_contact(api):
    responses.add(
        responses.DELETE,
        BASE_URL + "/contacts/1",
        status=204,
    )

    response = api.delete_contact(contact_id="1")
    assert response is None
