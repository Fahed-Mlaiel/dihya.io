"""
Mock-Utilities für Sicherheitstests (Dihya).
Stellt Hilfsfunktionen wie mock_role und mock_audit bereit, um Rollen und Audits im Testkontext zu simulieren.
"""

def mock_role(role_name):
    """Simuliert die Zuweisung einer Rolle im Testkontext (z.B. für Flask-Login oder ACL)."""
    # In echten Tests: Patchen Sie die aktuelle User-Session/Rolle.
    # Hier: Setzen Sie ein globales Flag oder Kontext, falls benötigt.
    # Für Flask: z.B. flask.g oder flask_login.current_user mocken.
    pass

def mock_audit(event, user=None):
    """Simuliert einen Audit-Log-Eintrag im Testkontext."""
    # In echten Tests: Logik für Audit-Events patchen oder aufzeichnen.
    pass

def get_jwt(user_id="test", role="user"):
    return f"fake-jwt-for-{user_id}-{role}"

def setup_test_user(user_id="test", role="user"):
    return {"user_id": user_id, "role": role}

def teardown_test_user(user_id="test"):
    return True
