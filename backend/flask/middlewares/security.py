"""
Middlewares de sécurité avancés pour Dihya Coding Backend
Inclut WAF, anti-DDOS, validation, audit, logs, plugins, RGPD.
"""
from flask import request, abort
import logging
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Limiteur anti-DDOS global
limiter = Limiter(key_func=get_remote_address, default_limits=["100/minute"])

def waf_protect(req):
    # Protection basique OWASP Top 10 (exemple)
    if any(x in req.path for x in ['..', '<script', 'DROP TABLE']):
        abort(403, 'WAF: forbidden')

def anti_ddos(req):
    # Limiteur Flask-Limiter (déjà appliqué globalement)
    pass

def validate_request(req):
    # Validation schéma, anti-injection (exemple simplifié)
    if req.method in ['POST', 'PUT'] and req.is_json:
        data = req.get_json()
        if isinstance(data, dict) and any('DROP' in str(v) for v in data.values()):
            abort(400, 'Invalid input')
