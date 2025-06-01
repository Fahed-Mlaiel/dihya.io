# utils/tests — Tests unitaires des utilitaires backend Dihya Coding

Ce dossier contient les tests unitaires pour tous les helpers/utilitaires du backend Dihya Coding (exceptions, validation, sécurité, CORS, mailing, etc.).

## Objectif

- Garantir la robustesse, la sécurité et la conformité des fonctions utilitaires.
- Prévenir les régressions lors des évolutions du code.
- Couvrir tous les cas critiques : erreurs, edge cases, sécurité, conformité métier.

## Bonnes pratiques

- Isoler chaque test pour éviter les effets de bord (utiliser des fixtures pour les cas critiques).
- Ne jamais inclure de secrets ou de données sensibles dans les tests ou les messages d’erreur.
- Documenter chaque test avec une docstring claire.
- Couvrir les helpers critiques : exceptions personnalisées, validation, sécurité, CORS, mailing, etc.

## Exemple d’exécution

```bash
pytest app/utils/tests/