"""
Hooks audit threed (Python)
"""


def before_audit(action, user):
    # Logique avant audit
    return {"action": action, "user": user}


def after_audit(action, user):
    # Logique après audit
    return {"action": action, "user": user}
