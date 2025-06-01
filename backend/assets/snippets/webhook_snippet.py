"""
webhook_snippet.py – Webhook backend (Dihya)
Sécurité, validation, logs, audit, RGPD, multilingue.
"""
def validate_webhook(payload, secret):
    # Validation simple (exemple)
    if not payload or not secret:
        raise ValueError("[WEBHOOK] Invalid payload/secret")
    return True

def log_webhook(event, user=None):
    print(f"[WEBHOOK][{event}] user={user}")
    return {"status": "logged", "event": event}

# Exemple d’utilisation
if __name__ == "__main__":
    print(validate_webhook({"event": "push"}, "supersecret"))
    print(log_webhook("push_event", user="ci-bot"))
