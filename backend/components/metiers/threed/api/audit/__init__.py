# Point d'entrée du module audit

from .audit import audit_entity
# Expose les helpers, runners et hooks d’audit
__all__ = [
    'audit_entity',
    # Ajouter ici d’autres helpers/runners/hooks si besoin
]
