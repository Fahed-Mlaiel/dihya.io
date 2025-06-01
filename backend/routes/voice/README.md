# Voix – Dihya Backend

Ce dossier gère les routes pour la synthèse vocale, la reconnaissance vocale et l’intégration IA/VR/AR.

## Fonctionnalités
- Transcription multilingue (fr, en, ar, ...)
- Synthèse vocale (TTS) et reconnaissance (ASR)
- Sécurité (JWT, audit, RGPD)
- Plugins IA (fallback LLaMA, Mixtral, Mistral)
- WebSocket pour streaming temps réel

## Utilisation
Importer les routes dans votre app FastAPI :

```python
from .routes import router as voice_router
```

## Extension
Ajoutez vos modules vocaux ici, ils seront auto-chargés.

## Sécurité
- Logs d’audit
- RGPD
- Export des logs
