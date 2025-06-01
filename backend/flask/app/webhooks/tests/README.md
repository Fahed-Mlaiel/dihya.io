# tests/ — Tests unitaires webhooks (Dihya Coding)

Ce dossier regroupe les tests unitaires pour tous les handlers de webhooks du backend Flask Dihya Coding.

## Objectif

- Vérifier la robustesse, la sécurité et la conformité RGPD/OWASP des endpoints de webhooks (paiement, notifications, etc.).
- Garantir la non-régression et la traçabilité des intégrations externes.
- Faciliter l’audit, la maintenance et l’évolution des handlers de webhooks.

## Bonnes pratiques

- Un fichier de test par type de webhook (`test_payment_webhooks.py`, `test_notification_webhooks.py`, etc.).
- Couvrir tous les cas d’usage, y compris les erreurs, signatures invalides, payloads corrompus, etc.
- Ne jamais stocker ou logguer de secrets réels ou de données personnelles dans les tests.
- Utiliser des mocks ou des fixtures pour isoler les dépendances externes.
- Documenter chaque test avec une docstring claire.
- Exécuter les tests automatiquement en CI/CD.

## Exemple de structure

- `test_payment_webhooks.py` : tests pour la gestion des notifications de paiement.
- `test_notification_webhooks.py` : tests pour la gestion des notifications externes.

## Exemple d’exécution

```bash
pytest .