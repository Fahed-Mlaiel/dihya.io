"""
Dihya – Audit pour le module Restauration
- Logging, conformité RGPD
"""
import logging
from .models import Restaurant
from django.utils import timezone

def log_restauration_action(user, action, details=None):
    logging.info(f"[AUDIT][RESTAURATION] {action} by {user}: {details}")
