# Politique gamer Dihya

## Sécurité
- Authentification JWT obligatoire
- Validation stricte des entrées (XSS, injection, CSRF)
- Audit de toutes les actions sensibles
- Limitation de débit, WAF, anti-DDOS

## RGPD
- Consentement explicite pour la collecte de données
- Droit à l’oubli, export des données
- Anonymisation des logs

## Rôles
- admin : gestion totale
- joueur : accès aux matchs et scores
- invité : navigation

## Plugins
- Ajoutés via API/CLI, sandboxés

## Internationalisation
- Support multilingue dynamique

## SEO
- Sitemap, robots.txt, logs structurés

## Tests
- Unitaire, intégration, e2e, mocks

## Déploiement
- Docker, K8s, GitHub Actions, fallback local

