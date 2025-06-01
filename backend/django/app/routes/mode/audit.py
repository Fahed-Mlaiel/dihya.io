"""
Dihya – Audit pour le module Mode
- Logging, conformité RGPD
"""
import logging
from .models import Collection
from django.utils import timezone

def log_mode_action(user, action, details=None):
    logging.info(f"[AUDIT][MODE] {action} by {user}: {details}")
