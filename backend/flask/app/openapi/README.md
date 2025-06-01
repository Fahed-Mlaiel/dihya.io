# openapi

Documentation interne Dihya Coding.

## Objectif

Ce dossier centralise toutes les spécifications OpenAPI (Swagger) de la plateforme Dihya Coding, y compris les extensions, plugins et endpoints avancés.

## Bonnes pratiques

- Versionner chaque évolution de la spec (fichier daté ou versionné).
- Documenter chaque endpoint : paramètres, sécurité, validations, exemples de réponse.
- Utiliser les schémas OpenAPI pour garantir la cohérence des APIs.
- Protéger les endpoints critiques par des securitySchemes (JWT, OAuth2…).
- Mettre à jour la documentation à chaque ajout ou modification d’API.

## Structure recommandée

```
openapi/
├── README.md
├── openapi.yaml           # Spécification principale de l’API
├── extra_spec.yaml        # Extensions, plugins, endpoints avancés
└── ...                    # Autres specs ou versions si besoin
```

## Exemple d’utilisation

- Consulter [`openapi.yaml`](./openapi.yaml) pour la spec principale.
- Consulter [`extra_spec.yaml`](./extra_spec.yaml) pour les extensions/plugins.
- Générer la doc interactive avec Swagger UI ou Redoc.

---

*Ce dossier fait partie de la documentation technique interne Dihya Coding.*