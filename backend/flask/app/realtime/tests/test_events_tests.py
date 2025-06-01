"""
Tests unitaires pour la gestion des événements temps réel (realtime) dans Dihya Coding.
Couvre : validation des événements, émission, réception, gestion d’erreur, sécurité.
"""

import pytest

# Supposons que le module events.py expose les fonctions suivantes :
# - validate_event(data)
# - emit_event(event_type, payload, user_id)
# - get_user_events(user_id)

from backend.flask.app.realtime import events

@pytest.fixture(autouse=True)
def clear_events_store():
    if hasattr(events, "EVENTS_STORE"):
        events.EVENTS_STORE.clear()

def test_validate_event_ok():
    data = {"event_type": "notification", "payload": {"msg": "Hello"}, "user_id": "user1"}
    assert events.validate_event(data) is True

def test_validate_event_missing_type():
    data = {"payload": {"msg": "Hello"}, "user_id": "user1"}
    with pytest.raises(ValueError):
        events.validate_event(data)

def test_validate_event_invalid_payload():
    data = {"event_type": "notification", "payload": "notadict", "user_id": "user1"}
    with pytest.raises(ValueError):
        events.validate_event(data)

def test_emit_and_get_user_events():
    user_id = "user2"
    event_type = "update"
    payload = {"field": "status", "value": "ok"}
    events.emit_event(event_type, payload, user_id)
    user_events = events.get_user_events(user_id)
    assert len(user_events) == 1
    assert user_events[0]["event_type"] == event_type
    assert user_events[0]["payload"] == payload

def test_emit_event_invalid_type():
    with pytest.raises(ValueError):
        events.emit_event("", {"msg": "fail"}, "user3")

def test_emit_event_invalid_user():
    with pytest.raises(ValueError):
        events.emit_event("notification", {"msg": "fail"}, "")

def test_get_user_events_empty():
    assert events.get_user_events("nouser") == []