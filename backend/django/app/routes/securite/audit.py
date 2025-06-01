"""
Dihya – Audit pour le module Sécurité
- Logging, conformité RGPD
"""
import logging
from .models import IncidentSecurite
from django.utils import timezone

def log_securite_action(user, action, details=None):
    logging.info(f"[AUDIT][SECURITE] {action} by {user}: {details}")
