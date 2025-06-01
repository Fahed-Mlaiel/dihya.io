"""
Module de healthcheck pour la surveillance du backend Dihya Coding.

Ce module fournit des fonctions pour vérifier la disponibilité et l'intégrité des services critiques
(base de données, API, stockage, etc.) du backend.

Bonnes pratiques :
- Ne jamais exposer d'informations sensibles dans les réponses de healthcheck.
- Retourner uniquement l'état (OK/KO) et éventuellement un horodatage.
- Prévoir des tests pour chaque dépendance critique (DB, API externes, stockage).
- Logger chaque healthcheck KO pour audit.
- Utiliser ce module dans une route dédiée (ex: /health) protégée si besoin.

Exemple d'utilisation :
    from monitoring.healthcheck import check_all_services
    status = check_all_services()
"""

import os
import sqlite3
from datetime import datetime

DB_PATH = os.getenv("DIHYA_DB_PATH", "dihya.db")

def check_database():
    """Vérifie la connexion à la base de données SQLite."""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.execute("SELECT 1")
        conn.close()
        return True
    except Exception:
        return False

def check_all_services():
    """
    Vérifie l'état de tous les services critiques.
    :return: dict avec le statut de chaque service et un horodatage.
    """
    status = {
        "database": check_database(),
        "timestamp": datetime.utcnow().isoformat()
    }
    # Ajouter ici d'autres checks (API externes, stockage, etc.)
    return status

def healthcheck_hook(event, sector=None):
    """Injecte la logique métier et le secteur dans l’événement de healthcheck."""
    event['sector'] = sector or 'default'
    return event

# Export DWeb/IPFS (mock)
def export_healthchecks_to_ipfs():
    """Exporte les résultats de healthcheck sur IPFS (mock/demo)."""
    # TODO: Intégration réelle IPFS
    return True
