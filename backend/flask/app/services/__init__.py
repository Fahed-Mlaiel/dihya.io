"""
Initialisation des services pour l'application Dihya Coding.

Ce module centralise l'import et l'organisation des services métiers (auth, user, mail, notifications, social_auth, etc.)
pour garantir une architecture claire, modulaire et extensible.

Bonnes pratiques :
- Importer explicitement chaque service utile ici.
- Ne jamais exposer de secrets ou de logique sensible dans ce module.
- Documenter chaque ajout de service pour faciliter la maintenance.
"""

from .auth_service import register_user, authenticate_user
from .user_service import (
    get_user_by_id, get_all_users, update_user, delete_user
)
from .mail import send_email
from .notifications import send_notification
from .social_auth import handle_social_login
# Ajouter ici d'autres services métiers si besoin (ex : plugins, analytics, etc.).