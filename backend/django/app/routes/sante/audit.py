"""
Dihya – Audit pour le module Santé
- Logging, conformité RGPD
"""
import logging
from .models import Patient
from django.utils import timezone

def log_sante_action(user, action, details=None):
    logging.info(f"[AUDIT][SANTE] {action} by {user}: {details}")
