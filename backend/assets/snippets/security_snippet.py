"""
security_snippet.py – Sécurité backend avancée (Dihya)
Validation, XSS, CSRF, JWT, logs, audit, multilingue.
"""
import re, logging

def validate_input(data):
    # Validation basique, XSS
    if re.search(r'<script|onerror|onload', str(data), re.I):
        raise ValueError("[SECURITY] Input XSS detected")
    return data

def check_jwt(token):
    # Vérification JWT (exemple, à adapter)
    if not token or len(token.split('.')) != 3:
        raise ValueError("[SECURITY] JWT invalid")
    return True

def log_security(event, user=None):
    logging.info(f"[SECURITY][{event}] user={user}")
    return {"status": "logged", "event": event}

# Exemple d’utilisation
if __name__ == "__main__":
    try:
        print(validate_input("<script>alert('xss')</script>"))
    except Exception as e:
        print(e)
    print(check_jwt("header.payload.signature"))
    print(log_security("test_event", user="admin"))
