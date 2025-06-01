# routes/tests — Tests unitaires des routes de génération Dihya Coding

Ce dossier contient les tests unitaires pour la route de génération automatique (`/api/generate`) du backend Dihya Coding.

## Objectif

- Vérifier la conformité de l’API de génération (validation des entrées, structure des réponses).
- Garantir la sécurité (authentification, rôles, non-fuite de données sensibles).
- Tester la robustesse de la génération (succès, erreurs, edge cases).
- Prévenir les régressions lors des évolutions du code.

## Bonnes pratiques

- Isoler chaque test pour éviter les effets de bord (utiliser des fixtures pour les utilisateurs et les payloads).
- Couvrir tous les cas critiques : entrées manquantes, type inconnu, accès non autorisé, etc.
- Ne jamais inclure de secrets ou de données sensibles dans les tests ou les réponses.
- Documenter chaque test avec une docstring claire.
- Simuler différents rôles utilisateurs pour tester la sécurité.

## Exemple d’exécution

```bash
pytest app/routes/tests/