import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello(client):
    """Test the hello endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['message'] == 'Hello, Flask!'


def test_test_endpoint(client):
    """Test the /api/test endpoint"""
    response = client.get('/api/test')
    assert response.status_code == 200
    assert response.json['status'] == 'success'
    assert response.json['data'] == 'Test endpoint'


def test_get_user(client):
    """Test the /api/users/<user_id> endpoint"""
    response = client.get('/api/users/123')
    assert response.status_code == 200
    assert response.json['user_id'] == 123
    assert response.json['name'] == 'User 123'


def test_invalid_user_id(client):
    """Test with invalid user_id (string instead of int)"""
    response = client.get('/api/users/abc')
    assert response.status_code == 404


def test_content_type(client):
    """Test that content type is JSON"""
    response = client.get('/')
    assert response.content_type == 'application/json'
