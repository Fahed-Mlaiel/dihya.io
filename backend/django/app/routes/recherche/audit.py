"""
Dihya – Audit pour le module Recherche
- Logging, conformité RGPD
"""
import logging
from .models import RequeteRecherche
from django.utils import timezone

def log_recherche_action(user, action, details=None):
    logging.info(f"[AUDIT][RECHERCHE] {action} by {user}: {details}")
