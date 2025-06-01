"""
Fonctions utilitaires partagées backend Dihya (Flask)
- Sécurité, RGPD, multilingue, audit, plugins, extensibilité, CI/CD-ready
"""
import json
import logging
from flask import request

SUPPORTED_LANGS = ['fr', 'en', 'ar', 'tzm', 'de', 'zh', 'ja', 'ko', 'nl', 'he', 'fa', 'hi', 'es']

def get_lang():
    lang = request.headers.get('X-Dihya-Lang', 'fr')
    return lang if lang in SUPPORTED_LANGS else 'fr'

def log_structured(level, message, **kwargs):
    entry = {
        'timestamp': logging.Formatter().formatTime(logging.makeLogRecord({})),
        'level': level,
        'message': message,
        **kwargs
    }
    logging.log(getattr(logging, level.upper(), logging.INFO), json.dumps(entry, ensure_ascii=False))
    return entry

def validate_schema(data, schema):
    # Validation JSON Schema (mock, à remplacer par jsonschema)
    for key in schema:
        if key not in data:
            raise ValueError(f"Champ manquant : {key}")
    return True
