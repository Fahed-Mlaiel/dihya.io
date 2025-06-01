# Documentation API Backend Dihya Coding

Ce dossier contient la documentation de l’API backend générée par la plateforme Dihya Coding.

## Contenu

- **openapi.yaml** : Spécification OpenAPI 3.0 de l’API (Swagger), décrivant toutes les routes, schémas, méthodes, sécurité, etc.
- **README.md** : Ce fichier d’explication et de bonnes pratiques.

## Bonnes pratiques

- Maintenir la spécification OpenAPI à jour à chaque modification des routes ou des schémas.
- Documenter chaque endpoint : méthode, paramètres, schéma de requête/réponse, codes d’erreur.
- Décrire les mécanismes de sécurité (authentification JWT, rôles, CORS, etc.).
- Générer automatiquement la documentation interactive (Swagger UI, Redoc…) à partir de `openapi.yaml`.
- Tester la conformité de l’API avec la spécification (lint, CI/CD).
- Traduire la documentation si besoin (i18n).
- Ne jamais exposer d’informations sensibles ou de secrets dans la documentation publique.
- Ajouter des exemples d’utilisation pour chaque endpoint critique.

## Exemple d’utilisation

- Pour visualiser la doc API :  
  Utiliser [Swagger Editor](https://editor.swagger.io/) ou intégrer Swagger UI dans le frontend/admin.
- Pour générer des clients API :  
  Utiliser `openapi-generator` ou `swagger-codegen` avec le fichier `openapi.yaml`.
- Pour tester la conformité :  
  Intégrer un linter OpenAPI dans la CI/CD (ex : `swagger-cli validate openapi.yaml`).

## Sécurité

- Ne jamais exposer d’informations sensibles dans la documentation publique.
- Documenter les bonnes pratiques d’authentification et de gestion des droits.
- Préciser les scopes et rôles nécessaires pour chaque route protégée.

---

**Équipe Dihya Coding**