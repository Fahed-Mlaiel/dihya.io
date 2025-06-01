"""
Dihya – Audit pour le module Publicité
- Logging, conformité RGPD
"""
import logging
from .models import CampagnePublicitaire
from django.utils import timezone

def log_publicite_action(user, action, details=None):
    logging.info(f"[AUDIT][PUBLICITE] {action} by {user}: {details}")
