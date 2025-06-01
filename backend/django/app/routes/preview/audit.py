"""
Dihya – Audit pour le module Preview
- Logging, conformité RGPD
"""
import logging
from .models import Preview
from django.utils import timezone

def log_preview_action(user, action, details=None):
    logging.info(f"[AUDIT][PREVIEW] {action} by {user}: {details}")
