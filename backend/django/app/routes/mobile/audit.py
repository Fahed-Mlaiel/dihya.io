"""
Dihya – Audit pour le module Mobile
- Logging, conformité RGPD
"""
import logging
from .models import MobileApp
from django.utils import timezone

def log_mobile_action(user, action, details=None):
    logging.info(f"[AUDIT][MOBILE] {action} by {user}: {details}")
