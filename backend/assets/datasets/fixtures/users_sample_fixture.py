import pytest

@pytest.fixture
def users_sample():
    return [
  {
    "id": 1,
    "username": "user1",
    "email": "user1@example.com",
    "role": "admin",
    "lang": "fr"
  },
  {
    "id": 2,
    "username": "user2",
    "email": "user2@example.com",
    "role": "user",
    "lang": "en"
  }
]
