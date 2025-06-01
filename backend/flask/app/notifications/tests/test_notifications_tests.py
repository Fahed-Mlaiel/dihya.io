"""
Tests unitaires pour le service de notifications internes Dihya Coding.
Couvre : création, validation, lecture, suppression, sécurité.
"""

import pytest
from backend.flask.app.notifications import models

@pytest.fixture(autouse=True)
def clear_store():
    models.NOTIFICATIONS_STORE.clear()

def test_create_and_list_notification():
    user_id = "user1"
    notif = models.Notification(user_id, "info", "Bienvenue sur Dihya !")
    models.add_notification(notif)
    notifs = models.get_user_notifications(user_id)
    assert len(notifs) == 1
    assert notifs[0].content == "Bienvenue sur Dihya !"
    assert notifs[0].notif_type == "info"
    assert not notifs[0].read

def test_validation_ok():
    data = {"user_id": "user2", "notif_type": "success", "content": "Opération réussie"}
    assert models.Notification.validate(data) is True

def test_validation_fail_type():
    data = {"user_id": "user2", "notif_type": "autre", "content": "Erreur"}
    with pytest.raises(ValueError):
        models.Notification.validate(data)

def test_validation_fail_content():
    data = {"user_id": "user2", "notif_type": "info", "content": ""}
    with pytest.raises(ValueError):
        models.Notification.validate(data)

def test_mark_notification_read():
    notif = models.Notification("user3", "error", "Erreur détectée")
    models.add_notification(notif)
    assert not notif.read
    models.mark_notification_read(notif)
    assert notif.read

def test_clear_user_notifications():
    notif1 = models.Notification("user4", "info", "A")
    notif2 = models.Notification("user4", "success", "B")
    models.add_notification(notif1)
    models.add_notification(notif2)
    assert len(models.get_user_notifications("user4")) == 2
    models.clear_user_notifications("user4")
    assert len(models.get_user_notifications("user4")) == 0
