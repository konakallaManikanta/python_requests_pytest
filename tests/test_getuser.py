import pytest
from utils.api_client import APIClient
import uuid

@pytest.fixture(scope= 'module')
def api_client():
    return APIClient()

def test_get_users(api_client):
    response = api_client.get('users')
    #print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_users(api_client, load_user_data):
    # user_data = {
    #     "name": "Prasanth",
    #     "username": "qa user",
    #     "email": "test@gmail.com"
    # }
    user_data = load_user_data["new_user"]
    unique_email = f"{uuid.uuid4().hex[:8]}@gmail.com"
    print(unique_email)
    user_data["email"] = unique_email

    response = api_client.post("users", user_data)
    #print(response.json())
    assert response.status_code == 201

def test_update_user(api_client):
    user_data = {
        "name": "Prasanth K",
        "username": "qa user",
        "email": "test@gmail.com"
    }
    response = api_client.put("users/1", user_data)
    #print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == "Prasanth K"

def test_delete_user(api_client):
    response = api_client.delete("users/1")
    print(response.json())
    assert response.status_code == 200
    
