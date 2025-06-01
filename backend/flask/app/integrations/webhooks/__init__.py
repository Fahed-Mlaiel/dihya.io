"""
Initialisation du module de gestion des webhooks d’intégration pour Dihya Coding.

Ce package centralise la déclaration, la validation et la gestion sécurisée des webhooks utilisés pour intégrer des services externes
(ERP, CRM, outils de paiement, outils de communication, etc.).

Bonnes pratiques :
- Déclarer chaque intégration de webhook dans un fichier dédié (ex : erp_webhooks.py, crm_webhooks.py).
- Valider systématiquement la signature, l’origine et le contenu de chaque webhook reçu.
- Logger tous les événements pour audit et traçabilité.
- Protéger les endpoints de webhook contre les abus (rate limiting, validation stricte, authentification si possible).
- Documenter chaque webhook (usage, sécurité, format attendu, exemples).
- Prévoir des tests unitaires pour chaque handler de webhook.

Exemple d’import :
    from backend.flask.app.integrations.webhooks.erp_webhooks import handle_erp_event
    from backend.flask.app.integrations.webhooks.crm_webhooks import handle_crm_event
"""
# Exemple d’import automatique (à compléter selon les fichiers créés)
# from .erp_webhooks import handle_erp_event
# from .crm_webhooks import handle_crm_event