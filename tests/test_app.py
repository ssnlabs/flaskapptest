import pytest
import sys
import os

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import the app from the root directory
from app import app  # Importing the app from the root directory

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    # Test that the home route works and returns the expected text
    response = client.get('/')
    assert response.status_code == 200
    assert b"vicky punda" in response.data  # Check if the response contains 'vicky punda'
