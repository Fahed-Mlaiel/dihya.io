# Santé

## Description
Ce module métier gère les fonctionnalités spécifiques au secteur Santé (Health).

- Règles métier principales :
- RGPD renforcé
- Validation ordonnance obligatoire


- Plugins activés : analytics, rgpd, paiement
- Dépendances : pandas, flask-health
- RGPD : Oui

## Templates utilisés
- Backend : template_sante.py
- Frontend : template_sante.jsx
- Mobile : template_sante_flutter.dart
- DevOps : Dockerfile.sante

## Tests spécifiques
- test_rgpd.py
- test_ordonnance.py


## Composants frontend associés
- CardSante
- FormOrdonnance


## Documentation
- README_SANTE.md


## Options DevOps
- Dockerfile.sante
- ci_sante.yml


---
*Ce fichier est généré automatiquement à partir de la source de vérité centrale.*