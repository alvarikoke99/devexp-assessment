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

# Test Cases for Messages

@responses.activate
def test_get_messages(api):
    responses.add(
        responses.GET,
        BASE_URL + "/messages",
        json={
            "messages": [
                {
                    "from": "Gordon Freeman",
                    "content": "The right man in the wrong place can make all the difference.",
                    "id": "1",
                    "status": "queued",
                    "createdAt": "2024-12-04T13:33:24.361Z",
                    "to": {"name": "Alyx Vance", "phone": "+123", "id": "123"},
                }
            ],
            "page": 1,
            "quantityPerPage": 10,
        },
        status=200,
    )

    messages = api.get_messages(page=1, per_page=10)
    assert len(messages.messages) == 1
    assert messages.messages[0].content == "The right man in the wrong place can make all the difference."

@responses.activate
def test_send_message(api):
    responses.add(
        responses.POST,
        BASE_URL + "/messages",
        json={
            "from": "Chell",
            "content": "The cake is a lie.",
            "id": "1",
            "status": "queued",
            "createdAt": "2024-12-04T13:33:24.361Z",
            "to": {"name": "GLaDOS", "phone": "+123", "id": "123"},
        },
        status=201,
    )

    message = api.send_message(
        from_="Chell",
        to={"name": "GLaDOS", "phone": "+123", "id": "123"},
        content="The cake is a lie.",
    )
    assert message.id == "1"
    assert message.status == "queued"

@responses.activate
def test_get_message_by_id(api):
    responses.add(
        responses.GET,
        BASE_URL + "/messages/1",
        json={
            "from": "Wheatley",
            "content": "This is the part where he kills you.",
            "id": "1",
            "status": "queued",
            "createdAt": "2024-12-04T13:33:24.361Z",
            "to": {"name": "The Companion Cube", "phone": "+123", "id": "123"},
        },
        status=200,
    )

    message = api.get_message_by_id("1")
    assert message.id == "1"
    assert message.content == "This is the part where he kills you."
