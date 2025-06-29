"""
Blueprint plugin d’audit (Python)
Plugin d’audit ultra avancé : hooks, extension dynamique, journalisation, alertes, doc, exemples.
"""
from typing import Callable, Any, Dict

audit_hooks = []

def register_audit_hook(hook: Callable[[Dict], Any]):
    audit_hooks.append(hook)
    return hook

def run_audit(user: str, action: str = "", data: Dict = None):
    event = {"user": user, "action": action, "data": data or {}}
    print(f"[AUDIT] {event}")
    for hook in audit_hooks:
        hook(event)
    return event

# Exemple d’utilisation :
# @register_audit_hook
def alert_on_admin(event):
    if event["user"] == "admin":
        print("[ALERTE] Action admin détectée !")

# run_audit(user="admin", action="delete", data={"id": 1})
