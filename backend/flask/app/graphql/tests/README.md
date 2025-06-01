# graphql/tests — Tests unitaires des resolvers GraphQL Dihya Coding

Ce dossier contient les tests unitaires pour les resolvers GraphQL du backend Dihya Coding.

## Objectif

- Vérifier la conformité des requêtes et des schémas GraphQL.
- Garantir la sécurité des accès (rôles, permissions) pour chaque resolver.
- Tester la robustesse des réponses et la gestion des erreurs.
- Prévenir toute fuite de données sensibles dans les réponses GraphQL.

## Bonnes pratiques

- Isoler chaque test pour éviter les effets de bord (utiliser des fixtures pour le contexte utilisateur).
- Couvrir tous les cas critiques : validation des arguments, permissions, erreurs, edge cases.
- Ne jamais inclure de secrets ou de données sensibles dans les tests ou les réponses.
- Documenter chaque test avec une docstring claire.
- Simuler différents rôles utilisateurs (admin, user, invité…) pour tester la sécurité.

## Exemple d’exécution

```bash
pytest app/graphql/tests/