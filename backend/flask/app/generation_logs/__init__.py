"""
Module de traçabilité des générations – Dihya Coding

Ce module centralise les fonctions de logging et d’audit pour chaque génération automatique.
Il garantit la transparence, la conformité RGPD, la souveraineté et la sécurité des logs.

Bonnes pratiques :
- Ne jamais logger de données sensibles (mot de passe, token, spec brute)
- Horodater chaque événement de génération
- Permettre l’audit, l’export et la purge des logs
- Utiliser un format structuré (JSON)
- Prévoir l’extensibilité pour d’autres systèmes de logs (Notion, IPFS, etc.)
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any

LOGS_DIR = Path(__file__).parent
LOG_FILE = LOGS_DIR / "generation.log"

def log_generation_event(
    user_id: Optional[str],
    needs: Dict[str, Any],
    code: Dict[str, str],
    status: str = "success",
    error: Optional[str] = None,
    extra: Optional[Dict[str, Any]] = None
):
    """
    Loggue un événement de génération automatique.

    Args:
        user_id (str): ID utilisateur (ou None).
        needs (dict): Besoins analysés (jamais le spec brut).
        code (dict): Fichiers générés (seulement les noms, pas le contenu).
        status (str): "success" ou "error".
        error (str, optional): Message d’erreur si échec.
        extra (dict, optional): Métadonnées additionnelles (ex : plugin, template…).
    """
    event = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "user_id": user_id,
        "project_name": needs.get("project_name", "N/A"),
        "stack": needs.get("stack", "N/A"),
        "files": list(code.keys()),
        "status": status,
        "error": error,
        "plugins": needs.get("plugins", []),
        "template": needs.get("template", None)
    }
    if extra:
        event.update(extra)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")
    except Exception as e:
        logging.error(f"Erreur lors du logging de génération : {e}")

def export_generation_logs(destination_path: str):
    """
    Exporte tous les logs de génération vers un fichier externe.

    Args:
        destination_path (str): Chemin du fichier export.
    """
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as src, open(destination_path, "w", encoding="utf-8") as dst:
            dst.write(src.read())
    except Exception as e:
        logging.error(f"Erreur lors de l’export des logs : {e}")

def purge_generation_logs():
    """
    Purge tous les logs de génération (conformité RGPD).
    Cette opération est irréversible.
    """
    try:
        open(LOG_FILE, "w").close()
        logging.info("Tous les logs de génération ont été purgés (RGPD).")
    except Exception as e:
        logging.error(f"Erreur lors de la purge des logs : {e}")

def get_generation_logs(limit: Optional[int] = None) -> list:
    """
    Récupère les logs de génération pour audit ou affichage.

    Args:
        limit (int, optional): Nombre maximum de logs à retourner (None = tout).

    Returns:
        list: Liste des événements de génération (dictionnaires).
    """
    logs = []
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    logs.append(json.loads(line))
                except Exception:
                    continue
        if limit:
            return logs[-limit:]
        return logs
    except FileNotFoundError:
        return []
    except Exception as e:
        logging.error(f"Erreur lors de la lecture des logs : {e}")
        return []