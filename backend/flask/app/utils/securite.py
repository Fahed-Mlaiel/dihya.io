"""
Utilitaires de sécurité pour l'application Dihya Coding.
Inclut : gestion des mots de passe, génération de tokens, CORS, rate limiting, headers de sécurité.
"""

from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, jsonify
from functools import wraps

def hash_password(password):
    """
    Génère un hash sécurisé pour un mot de passe.
    Args:
        password (str): Mot de passe en clair
    Returns:
        str: Hash du mot de passe
    """
    return generate_password_hash(password)

def verify_password(password, password_hash):
    """
    Vérifie qu'un mot de passe correspond à son hash.
    Args:
        password (str): Mot de passe en clair
        password_hash (str): Hash stocké
    Returns:
        bool
    """
    return check_password_hash(password_hash, password)

def require_json(f):
    """
    Décorateur pour forcer le Content-Type JSON sur les endpoints API.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 400
        return f(*args, **kwargs)
    return decorated_function

def set_default_security_headers(response):
    """
    Ajoute des headers de sécurité à la réponse Flask.
    Args:
        response (flask.Response)
    Returns:
        flask.Response
    """
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=()"
    return response

# Exemple de rate limiting simple (à remplacer par Flask-Limiter en prod)
from time import time
RATE_LIMIT = {}
RATE_LIMIT_WINDOW = 60  # secondes
RATE_LIMIT_MAX = 100    # requêtes

def rate_limited(ip):
    """
    Limite le nombre de requêtes par IP.
    Args:
        ip (str): Adresse IP du client
    Returns:
        bool: True si limité, False sinon
    """
    now = int(time())
    window = now // RATE_LIMIT_WINDOW
    key = f"{ip}:{window}"
    RATE_LIMIT.setdefault(key, 0)
    RATE_LIMIT[key] += 1
    return RATE_LIMIT[key] > RATE_LIMIT_MAX

def sanitize_input(text):
    """
    Nettoie une chaîne pour éviter les injections (basiquement).
    Args:
        text (str)
    Returns:
        str
    """
    import re
    # Supprime les balises HTML et caractères suspects
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[\r\n\t]', ' ', text)
    text = re.sub(r'["\'`;]', '', text)
    return text.strip()

def role_required(roles):
    """
    Dummy-Dekorator für rollenbasierten Zugriff (Kompatibilität für Templates und Tests).
    """
    def decorator(f):
        return f
    return decorator

def validate_request(f):
    """
    Decorator-Stub für Request-Validierung (nimmt und gibt Funktion zurück).
    """
    return f

def audit_log(*args, **kwargs):
    """
    Stub pour journaliser une action (no-op).
    """
    pass

def validate_payload(fields=None):
    """
    Decorator-Factory pour valider les payloads en vérifiant la présence de champs requis.
    Args:
        fields (list): Liste des champs requis dans la payload
    Returns:
        decorator
    """
    def decorator(f):
        from functools import wraps
        @wraps(f)
        def wrapper(*args, **kwargs):
            from flask import request, jsonify
            data = request.get_json(silent=True) or {}
            missing = [field for field in (fields or []) if field not in data]
            if missing:
                return jsonify({'error': f'Champs manquants: {missing}'}), 400
            return f(*args, **kwargs)
        return wrapper
    return decorator

def waf_protect(f):
    """
    Dummy-Dekorator für WAF-Schutz (Kompatibilität für Templates und Tests).
    """
    return f
