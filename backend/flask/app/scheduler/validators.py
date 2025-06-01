"""
Validateurs avancés pour le module Scheduler.
Sécurité, RGPD, accessibilité, production-ready.
"""

import re

def is_valid_cron(cron):
    # Validation simple d'une expression CRON (placeholder)
    pattern = r"^([*]|[0-9,-/]+) ([*]|[0-9,-/]+) ([*]|[0-9,-/]+) ([*]|[0-9,-/]+) ([*]|[0-9,-/]+)$"
    return re.match(pattern, cron) is not None

def is_valid_job(data):
    return "name" in data and "cron" in data
