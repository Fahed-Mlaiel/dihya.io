"""
Dihya – Audit pour le module Science
- Logging, conformité RGPD
"""
import logging
from .models import ProjetScientifique
from django.utils import timezone

def log_science_action(user, action, details=None):
    logging.info(f"[AUDIT][SCIENCE] {action} by {user}: {details}")
