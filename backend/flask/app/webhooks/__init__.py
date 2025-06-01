"""
Initialisation du module de gestion des webhooks pour Dihya Coding.

Ce package centralise la déclaration, la validation et la gestion sécurisée des webhooks entrants et sortants
pour l’intégration avec des services externes (paiement, notifications, CI/CD, etc.).

Bonnes pratiques :
- Déclarer chaque type de webhook dans un fichier dédié (ex : payment_webhooks.py, notification_webhooks.py).
- Valider systématiquement la signature, l’origine et le contenu de chaque webhook reçu.
- Logger les événements pour audit et traçabilité.
- Protéger les endpoints de webhook contre les abus (rate limiting, validation stricte).
- Documenter chaque webhook (usage, sécurité, format attendu).
- Prévoir des tests unitaires pour chaque handler de webhook.

Exemple d’import :
    from backend.flask.app.webhooks.payment_webhooks import handle_payment_event
"""
# Exemple d’import automatique (à compléter selon les fichiers créés)
# from .payment_webhooks import handle_payment_event
# from .notification_webhooks import handle_notification_event