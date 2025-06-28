"""
utils_helper.py - Fonctions utilitaires avancées pour Arts (Python)
"""

import copy
from datetime import datetime


def format_date(date):
    return datetime.fromisoformat(date).isoformat()


def is_object(obj):
    return isinstance(obj, dict)


def deep_clone(obj):
    return copy.deepcopy(obj)
