# Validateurs – Dihya Backend

Ce dossier contient les validateurs pour les routes de l’API Dihya (REST/GraphQL).

## Objectif
- Sécuriser et valider toutes les entrées/sorties (type, format, sécurité, RGPD)
- Support multilingue (fr, en, ar, etc.)
- Extensible via plugins

## Exemples de validateurs
- JWT, rôles, CORS, anti-DDOS, WAF
- Schémas Pydantic/Marshmallow
- Validation dynamique selon le contexte métier

## Utilisation
Importer les validateurs dans vos routes :

```python
from .routes import validate_project_creation
```

## Internationalisation
Tous les messages d’erreur sont multilingues (fr, en, ar, ...).

## Sécurité
- Logs d’audit
- Anonymisation RGPD
- Export des logs

## Extension
Ajoutez vos validateurs dans ce dossier, ils seront automatiquement chargés.
