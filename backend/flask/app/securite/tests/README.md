# tests/ — Tests unitaires sécurité (Dihya Coding)

Ce dossier regroupe les tests unitaires pour tous les helpers de sécurité du backend Flask Dihya Coding.

## Objectif

- Vérifier la robustesse, la conformité et la sécurité des modules critiques (`secrets`, `integrity`, `crypto`, `acl`, etc.).
- Garantir la non-régression et la conformité RGPD/OWASP des helpers de sécurité.
- Faciliter l’audit, la maintenance et l’évolution des mécanismes de sécurité.

## Bonnes pratiques

- Un fichier de test par module de sécurité (`test_secrets.py`, `test_integrity.py`, etc.).
- Couvrir tous les cas d’usage, y compris les erreurs et cas limites.
- Ne jamais stocker ou logguer de secrets réels dans les tests.
- Utiliser des mocks ou des fixtures pour isoler les dépendances externes.
- Documenter chaque test avec une docstring claire.
- Exécuter les tests automatiquement en CI/CD.

## Exemple de structure

- `test_secrets.py` : tests pour la gestion sécurisée des secrets.
- `test_integrity.py` : tests pour la vérification d’intégrité (hash, HMAC).
- `test_crypto.py` : tests pour le chiffrement/déchiffrement.
- `test_acl.py` : tests pour la gestion des ACL et permissions.

## Exemple d’exécution

```bash
pytest .