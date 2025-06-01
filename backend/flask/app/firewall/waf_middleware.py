"""
Middleware Web Application Firewall (WAF) custom pour Dihya Coding.

Ce module protège l’API contre les attaques courantes (injections, XSS, scans, brute force, etc.)
en filtrant les requêtes suspectes selon des règles dynamiques et extensibles.

Bonnes pratiques :
- Ne jamais exposer de détails techniques sur les blocages dans la réponse
- Logger chaque tentative bloquée pour audit
- Permettre l’ajout facile de nouvelles règles
- Optimiser la performance (contrôles rapides)
"""

from flask import request, abort, current_app
import re
import logging

# Exemple de patterns à bloquer (à enrichir selon besoins)
SQLI_PATTERNS = [
    r"(\%27)|(\')|(\-\-)|(\%23)|(#)",  # SQL injection basique
    r"(\b(select|union|insert|update|delete|drop|alter|create)\b)",  # mots-clés SQL
]
XSS_PATTERNS = [
    r"(<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>)",  # balises <script>
    r"((javascript:|onerror=|onload=)[^\s]*)",  # JS inline
]

BLACKLISTED_IPS = set()  # À alimenter dynamiquement (ex: depuis Redis ou DB)

def waf_middleware(app):
    """
    Initialise le middleware WAF sur l’application Flask.
    À appeler dans create_app().
    """
    @app.before_request
    def waf_check():
        # 1. Filtrage IP
        remote_ip = request.remote_addr
        if remote_ip in BLACKLISTED_IPS:
            log_block("IP blacklistée", remote_ip)
            abort(403)

        # 2. Détection d’injection SQL/XSS dans les paramètres
        for value in list(request.values.values()) + list(request.headers.values()):
            if any(re.search(pat, value, re.IGNORECASE) for pat in SQLI_PATTERNS):
                log_block("Tentative injection SQL", remote_ip, value)
                abort(403)
            if any(re.search(pat, value, re.IGNORECASE) for pat in XSS_PATTERNS):
                log_block("Tentative XSS", remote_ip, value)
                abort(403)

        # 3. Blocage de certains user-agents connus pour le scan
        ua = request.headers.get("User-Agent", "")
        if re.search(r"(sqlmap|nikto|fuzz|acunetix|wpscan)", ua, re.IGNORECASE):
            log_block("User-Agent suspect", remote_ip, ua)
            abort(403)

        # 4. (Extensible) : Ajouter ici d’autres règles métier

def log_block(reason, ip, detail=None):
    """
    Loggue chaque tentative bloquée pour audit.
    """
    msg = f"[WAF] Blocage: {reason} | IP: {ip}"
    if detail:
        msg += f" | Détail: {detail[:100]}"
    logger = logging.getLogger("waf")
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
        logger.addHandler(handler)
    logger.warning(msg)