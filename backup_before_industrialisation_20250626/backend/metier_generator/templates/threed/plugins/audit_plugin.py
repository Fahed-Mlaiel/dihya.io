"""
Plugin d'audit avancé.
"""


def log_action(action, user):
    """Log une action utilisateur pour l'audit."""
    print(f"[AUDIT] {user}: {action}")
