# 🛡️ Dihya – Politique de Sécurité Frontend

## Objectifs
- Garantir la sécurité, la souveraineté et la conformité du frontend Dihya
- Couvrir toutes les vulnérabilités critiques (XSS, CSRF, CORS, injection, secrets, plugins, SEO)
- Multilingue (fr, en, ar, tzr)

## Méthodologie
- Sécurité by design : validation côté client, escape, CSP, CORS strict, anti-DDoS, rate limiting
- RGPD : anonymisation, consentement, logs auditables, suppression à la demande
- Accessibilité : navigation clavier, ARIA, contrastes, multilingue, fallback
- Souveraineté : fallback open source, auditabilité, logs, licence AGPL
- CI/CD : tests sécurité automatisés, audit de dépendances, SAST, lint, build, e2e

## Bonnes pratiques
- Jamais de secrets dans le code ou le frontend (utiliser .env, vault, secrets manager)
- Utiliser des librairies maintenues, auditées, open source
- Vérifier chaque contribution (lint, test, audit, accessibilité)
- Documenter chaque ajout (README, changelog, PR)

## Contribution
- Ajouter un test pour chaque vulnérabilité ou nouvelle fonctionnalité
- Documenter chaque scénario/langue
- Vérifier la conformité et la souveraineté

## Exemples d’intégration
- **React** : escape systématique, validation, hooks sécurité, helmet, CSP
- **CI/CD** : audit npm/yarn, Snyk, tests e2e, badge sécurité

## Contact
[security@dihya.io](mailto:security@dihya.io)
