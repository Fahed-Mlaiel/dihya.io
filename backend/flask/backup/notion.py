"""
Module de backup automatique sur Notion API pour Dihya Coding.

Ce module permet de sauvegarder des informations critiques (logs, métadonnées, inventaire, etc.)
dans une base Notion, afin d'assurer la résilience et la traçabilité du projet.

Bonnes pratiques :
- Ne jamais stocker de données sensibles ou de secrets dans Notion.
- Protéger le token d'accès Notion via les variables d'environnement.
- Logger chaque opération de backup avec horodatage.
- Gérer les erreurs et les quotas API Notion.
- Respecter la politique de confidentialité et la souveraineté des données.

Exemple d'utilisation :
    from backup.notion import backup_to_notion
    backup_to_notion("Backup automatique du {date}", {"type": "db", "status": "ok"})

"""

import os
import requests
from datetime import datetime

NOTION_TOKEN = os.getenv("NOTION_API_TOKEN")
NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

def backup_to_notion(message, metadata=None):
    """
    Sauvegarde un message et des métadonnées dans une base Notion.
    """
    if not NOTION_TOKEN or not NOTION_DATABASE_ID:
        print("Token Notion ou Database ID manquant.")
        return False

    url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    data = {
        "parent": { "database_id": NOTION_DATABASE_ID },
        "properties": {
            "Name": {
                "title": [
                    { "text": { "content": f"Backup Dihya {datetime.utcnow().isoformat()}" } }
                ]
            },
            "Message": {
                "rich_text": [
                    { "text": { "content": message } }
                ]
            },
            "Horodatage": {
                "date": { "start": datetime.utcnow().isoformat() }
            }
        }
    }
    if metadata:
        for key, value in metadata.items():
            data["properties"][key] = {"rich_text": [{"text": {"content": str(value)}}]}

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200 or response.status_code == 201:
        print("Backup vers Notion réussi.")
        return True
    else:
        print(f"Erreur backup Notion : {response.status_code} - {response.text}")
        return False