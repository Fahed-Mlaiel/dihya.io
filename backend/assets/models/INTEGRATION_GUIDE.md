# Dihya Backend Assets – Guide d’intégration des modèles IA

Ce dossier contient les modèles IA open source (Mixtral, LLaMA, Ollama, etc.) utilisés côté backend Dihya.

## Bonnes pratiques
- Utilisez uniquement des modèles open source, documentés, versionnés.
- Vérifiez l’intégrité (hash SHA-256) avant toute utilisation en production.
- Respectez la RGPD : pas de données personnelles dans les modèles, anonymisation systématique.
- Documentez chaque modèle (README, métadonnées multilingues, RGPD, licence).
- Intégrez les modèles via des scripts Python/Node.js sécurisés, auditables, multilingues.
- Privilégiez la souveraineté numérique : hébergez les modèles sur vos propres serveurs ou dans des clouds souverains.

## Exemples d’intégration
- Python : voir `main.py`, `ai_services.py`, ou les modules backend Dihya.
- Node.js : voir `index.js`, `ai_plugin.js`.

## Sécurité & conformité
- Vérifiez la conformité RGPD et la traçabilité de chaque modèle.
- Archivez les versions et les métadonnées pour chaque déploiement.

## Contact
Pour toute question : support@dihya.ai
