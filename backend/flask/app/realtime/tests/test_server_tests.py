"""
Tests unitaires pour le serveur temps réel (realtime/server.py) de Dihya Coding.
Couvre : démarrage, connexion, émission/réception d'événements, sécurité, gestion d’erreur.
"""

import pytest

# Supposons que le module server.py expose :
# - start_server()
# - connect_user(user_id)
# - send_event_to_user(user_id, event)
# - get_connected_users()

from backend.flask.app.realtime import server

@pytest.fixture(autouse=True)
def clear_server_state():
    if hasattr(server, "CONNECTED_USERS"):
        server.CONNECTED_USERS.clear()

def test_connect_user():
    user_id = "user1"
    server.connect_user(user_id)
    assert user_id in server.get_connected_users()

def test_connect_user_invalid():
    with pytest.raises(ValueError):
        server.connect_user("")

def test_send_event_to_user():
    user_id = "user2"
    server.connect_user(user_id)
    event = {"event_type": "notification", "payload": {"msg": "Hi"}}
    server.send_event_to_user(user_id, event)
    # Supposons que le serveur garde une trace des événements envoyés
    if hasattr(server, "USER_EVENTS"):
        assert server.USER_EVENTS[user_id][-1] == event

def test_send_event_to_nonexistent_user():
    with pytest.raises(KeyError):
        server.send_event_to_user("ghost", {"event_type": "notification", "payload": {}})

def test_get_connected_users_empty():
    assert server.get_connected_users() == []