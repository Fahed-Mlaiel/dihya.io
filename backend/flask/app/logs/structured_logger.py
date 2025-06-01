"""
Module de logger structuré pour Dihya Coding.

Permet de produire des logs structurés (JSON) adaptés à l’ingestion par des outils modernes
(ELK, Datadog, Loki, etc.), tout en respectant la confidentialité et la sécurité.

Bonnes pratiques :
- Ne jamais logger de données personnelles ou sensibles
- Structurer chaque log avec timestamp, niveau, module, message, et contexte métier
- Prévoir l’extensibilité (ajout de champs custom)
- Documenter l’usage du logger dans l’application

Exemple d’utilisation :
    from backend.flask.app.logs.structured_logger import get_logger
    logger = get_logger("mon_module")
    logger.info("Action réalisée", extra={"event": "user_login", "user_id": 123})
"""

import logging
import json
import sys
from datetime import datetime

class JsonFormatter(logging.Formatter):
    """
    Formatter pour logs JSON structurés.
    """
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "module": record.name,
            "message": record.getMessage(),
        }
        # Ajout de contexte métier si fourni via extra
        if hasattr(record, "event"):
            log_record["event"] = record.event
        if hasattr(record, "context"):
            log_record["context"] = record.context
        # Ajout d'autres champs extra
        if hasattr(record, "extra") and isinstance(record.extra, dict):
            log_record.update(record.extra)
        return json.dumps(log_record, ensure_ascii=False)

def get_logger(module_name: str):
    """
    Retourne un logger structuré pour le module donné.
    """
    logger = logging.getLogger(module_name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JsonFormatter())
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    return logger

# Exemple d’utilisation :
# logger = get_logger("app.security")
# logger.info("Tentative de connexion", extra={"event": "login_attempt", "ip": "127.0.0.1"})