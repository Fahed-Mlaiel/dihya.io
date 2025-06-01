# Voyage – Dihya Backend

Ce dossier gère les routes pour la gestion de projets de voyage (IA, VR, AR, etc.).

## Fonctionnalités
- Création, modification, suppression de projets de voyage
- Sécurité (JWT, rôles, audit, RGPD)
- Multilingue (fr, en, ar, ...)
- Plugins IA (recommandations, génération d’itinéraires)

## Utilisation
Importer les routes dans votre app FastAPI :

```python
from .routes import router as voyage_router
```

## Extension
Ajoutez vos modules de voyage ici, ils seront auto-chargés.

## Sécurité
- Logs d’audit
- RGPD
- Export des logs
