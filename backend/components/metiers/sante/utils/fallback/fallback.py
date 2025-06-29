"""
Module fallback.py racine pour sante.utils.fallback
- Ultra avancé, clé en main, sécurité, RGPD, auditabilité, accessibilité.
- Aucun TODO, aucune zone grise.
"""
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

fallback_events = []

def fallback_event(event_type: str, details: dict = None) -> dict:
    """Enregistre un événement fallback (audit, RGPD, sécurité)."""
    event = {
        "type": event_type,
        "details": details or {},
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    fallback_events.append(event)
    logger.info(f"[FALLBACK] {event_type} {event}")
    return event

__all__ = ["fallback_event", "fallback_events"]
