"""
Dihya – Audit pour le module Ressources Humaines
- Logging, conformité RGPD
"""
import logging
from .models import Employe
from django.utils import timezone

def log_rh_action(user, action, details=None):
    logging.info(f"[AUDIT][RH] {action} by {user}: {details}")
