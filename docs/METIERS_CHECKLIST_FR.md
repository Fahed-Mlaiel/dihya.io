# Checklist Métiers (FR) – Dihya Coding

Ce document détaille les points de contrôle par métier pour garantir la conformité, la sécurité, la performance et l’extensibilité du projet.

## Checklist globale
- [ ] Sécurité maximale (CORS, JWT, WAF, anti-DDOS, audit, anonymisation RGPD)
- [ ] Internationalisation dynamique (fr, en, ar, de, etc.)
- [ ] Accessibilité (WCAG 2.1 AA, audit axe/Lighthouse)
- [ ] Multitenancy, gestion des rôles (admin, user, invité)
- [ ] Plugins extensibles, sandboxés, audités
- [ ] Génération automatique de projets (web, mobile, IA, etc.)
- [ ] Tests complets (unitaires, intégration, e2e, mocks, fixtures)
- [ ] Déploiement CI/CD (GitHub Actions, Docker, K8s, fallback local)
- [ ] Documentation exhaustive, multilingue, à jour
- [ ] Logs structurés, exportables, auditables
- [ ] Conformité RGPD, export/anonymisation, logs d’accès
- [ ] SEO backend (robots, sitemap, logs)

## Checklist par métier
- IA : fallback open source, auditabilité, explainabilité, sécurité des modèles
- VR/AR : performance, accessibilité, compatibilité device, logs
- Web/mobile : responsive, SEO, accessibilité, i18n, sécurité
- Sécurité : WAF, anti-DDOS, logs, audit, RGPD, tests de pénétration
- Plugins : API/CLI, sandbox, audit, documentation, tests

---

À valider à chaque release.
