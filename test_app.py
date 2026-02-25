import pytest
from app import app

@pytest.fixture
def client():
    """Flask app test client"""  # ✅ QUOTES ADDED
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test homepage loads"""  # ✅ QUOTES ADDED
    response = client.get('/')
    assert response.status_code == 200

def test_signup_missing_data(client):
    """Test signup with missing email"""  # ✅ QUOTES ADDED
    response = client.post('/api/signup', json={"password": "test123"})
    assert response.status_code == 400
    assert "error" in response.json

def test_protected_route_no_token(client):
    """Test protected route without token"""  # ✅ QUOTES ADDED
    response = client.get('/api/protected')
    assert response.status_code == 401
