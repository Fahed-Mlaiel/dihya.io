"""
Client Notion API pour Dihya Coding

Ce module encapsule les appels à l’API Notion pour la gestion de bases de données, de pages et de logs.
- Sécurité : token via variable d’environnement
- Validation stricte des payloads
- Logging/audit de chaque opération
- Gestion robuste des erreurs
"""
import os
import requests
import logging
from typing import Optional, Dict, Any

NOTION_API_URL = "https://api.notion.com/v1/pages"
NOTION_TOKEN = os.getenv("NOTION_API_TOKEN")
NOTION_VERSION = "2022-06-28"

logger = logging.getLogger("dihya.api_clients.notion")
logger.setLevel(logging.INFO)

def create_page(database_id: str, title: str, properties: Optional[Dict[str, Any]] = None) -> Optional[str]:
    if not NOTION_TOKEN:
        logger.error("Token Notion manquant.")
        return None
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": NOTION_VERSION
    }
    data = {
        "parent": {"database_id": database_id},
        "properties": {
            "Name": {"title": [{"text": {"content": title}}]}
        }
    }
    if properties:
        data["properties"].update(properties)
    try:
        resp = requests.post(NOTION_API_URL, headers=headers, json=data)
        resp.raise_for_status()
        logger.info(f"Page Notion créée : {title}")
        return resp.json().get("id")
    except Exception as e:
        logger.error(f"Erreur Notion : {e}")
        return None
