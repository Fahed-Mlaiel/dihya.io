"""
Dihya – Audit pour le module Médias
- Logging, conformité RGPD
"""
import logging
from .models import Media
from django.utils import timezone

def log_media_action(user, action, details=None):
    logging.info(f"[AUDIT][MEDIAS] {action} by {user}: {details}")
