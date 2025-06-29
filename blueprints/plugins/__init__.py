"""
Initialisation des blueprints Plugins (Python)
Expose tous les générateurs de plugins ultra avancés : audit, extension dynamique, hooks, doc, exemples.
"""
from .audit.audit_plugin import run_audit, register_audit_hook

__all__ = ['run_audit', 'register_audit_hook']

# Exemple d’utilisation :
# from blueprints.plugins import run_audit, register_audit_hook
# @register_audit_hook
def alert(event):
    ...
# run_audit(user="admin", action="delete", data={"id": 1})
