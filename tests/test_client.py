import pytest
import responses
import os
from sdk.client import APIClient
from dotenv import load_dotenv

load_dotenv() 

BASE_URL = os.getenv("BASE_URL", "https://localhost:3000")
API_KEY = os.getenv("API_KEY", "there-is-no-key")

@pytest.fixture
def client():
    return APIClient(base_url=BASE_URL, api_key=API_KEY)

@responses.activate
def test_client_request_success(client):
    responses.add(
        responses.GET,
        BASE_URL+"/test",
        json={"success": True},
        status=200,
    )

    response = client.request("GET", "/test")
    assert response == {"success": True}

@responses.activate
def test_client_request_auth_header(client):
    responses.add(
        responses.GET,
        BASE_URL+"/auth-check",
        json={"auth": "ok"},
        status=200,
    )

    client.request("GET", "/auth-check")
    request_headers = responses.calls[0].request.headers
    assert "Authorization" in request_headers
    assert request_headers["Authorization"] == "Bearer " + API_KEY

@responses.activate
def test_client_request_raises_error(client):
    responses.add(
        responses.GET,
        BASE_URL+"/error",
        json={"error": "Something went wrong"},
        status=400,
    )

    with pytest.raises(Exception):
        client.request("GET", "/error")
