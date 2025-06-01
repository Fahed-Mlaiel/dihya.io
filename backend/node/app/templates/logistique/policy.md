# Politique de sécurité et conformité – Logistique

Ce document définit les règles de sécurité, conformité RGPD, accessibilité, auditabilité, et bonnes pratiques pour les modules logistiques du projet Dihya.

## Sécurité
- Authentification JWT obligatoire
- CORS strict (origines autorisées dynamiques)
- Validation stricte des entrées (type, format, taille)
- Journalisation structurée (logs d'accès, erreurs, actions)
- Protection WAF, anti-DDOS, anti-XSS, anti-CSRF

## RGPD & Auditabilité
- Anonymisation des données sensibles
- Export des accès et logs sur demande
- Droit à l'oubli, portabilité
- Consentement explicite pour la collecte de données

## Accessibilité
- API compatible avec les lecteurs d'écran et outils d'accessibilité
- Documentation multilingue

## Extension
- Ajout de plugins ou modules via API/CLI

## Tests
- Couverture unitaire, intégration, e2e > 95%
- CI/CD obligatoire (GitHub Actions, Docker, K8s)

## Contact
Pour toute question, contactez l'équipe Dihya.
