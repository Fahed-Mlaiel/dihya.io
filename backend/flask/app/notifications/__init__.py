"""
Initialisation du module de gestion des notifications pour Dihya Coding.

Ce package centralise la déclaration, l’envoi et la gestion des notifications (email, push, SMS, etc.)
pour garantir une communication fiable et sécurisée avec les utilisateurs.

Bonnes pratiques :
- Déclarer chaque canal de notification dans un fichier dédié (ex : email.py, push.py, sms.py).
- Valider et filtrer les contenus envoyés pour éviter les injections ou abus.
- Logger les notifications envoyées pour audit et traçabilité.
- Protéger les fonctions critiques par des vérifications de permissions.
- Prévoir des tests unitaires pour chaque canal de notification.
- Respecter la confidentialité et la conformité RGPD (ne jamais exposer d’informations sensibles).

Exemple d’import :
    from backend.flask.app.notifications.email import send_notification_email
    from backend.flask.app.notifications.push import send_push_notification
"""
# Exemple d’import automatique (à compléter selon les fichiers créés)
# from .email import send_notification_email
# from .push import send_push_notification
# from .sms import send_sms_notification