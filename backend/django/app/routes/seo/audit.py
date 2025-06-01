"""
Dihya – Audit pour le module SEO
- Logging, conformité RGPD
"""
import logging
from .models import PageSEO
from django.utils import timezone

def log_seo_action(user, action, details=None):
    logging.info(f"[AUDIT][SEO] {action} by {user}: {details}")
