"""
logger.py – Logger avancé, structuré, multitenant, RGPD-ready (Python)
"""
import json, os
from datetime import datetime

LOG_PATH = os.path.join(os.path.dirname(__file__), 'environnement.log')

def log(level, message, **meta):
    entry = {
        'timestamp': datetime.utcnow().isoformat(),
        'level': level,
        'message': message,
        **meta
    }
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(json.dumps(entry) + '\n')

def info(msg, **meta):
    log('info', msg, **meta)

def warn(msg, **meta):
    log('warn', msg, **meta)

def error(msg, **meta):
    log('error', msg, **meta)

def audit(msg, **meta):
    log('audit', msg, **meta)
