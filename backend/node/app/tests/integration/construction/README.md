# README – Tests d’intégration Construction (IA/VR/AR)

Ce dossier contient les tests d’intégration avancés pour la gestion de projets IA, VR, AR dans le secteur de la construction.

## Exigences et conformité
- **Sécurité** : CORS, JWT, WAF, anti-DDOS, validation, audit, logging
- **RGPD** : anonymisation, consentement, auditabilité, export
- **Accessibilité** : WCAG 2.2, multilingue (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- **RBAC & Multitenancy** : gestion des rôles, isolation des données
- **Plugins & Fallback IA** : extensibilité, LLaMA/Mixtral/Mistral
- **SEO backend** : logs structurés, robots, sitemap dynamique
- **CI/CD** : tests automatisés, pipelines, Codespaces/Linux-ready

## Structure
- `test_construction.js` : tests d’intégration complets (sécurité, RGPD, accessibilité, i18n, plugins, audit, fallback IA, RBAC, multitenancy, SEO backend, CI/CD)

## Contribution
- Respecter la sécurité, la RGPD, l’accessibilité, la documentation intégrée
- Ajouter des exemples, guides, et tests multilingues
- CI/CD et auditabilité obligatoires

## Guides
- Lancer les tests : `npm run test:integration -- construction`
- Ajouter un plugin : voir plugins/README.md
- Ajouter une langue : voir i18n/README.md

## Documentation intégrée
Chaque test inclut : sécurité, RGPD, accessibilité, multilingue, CI/CD, audit, plugins, fallback IA, SEO backend, exemples, guides, contribution.
