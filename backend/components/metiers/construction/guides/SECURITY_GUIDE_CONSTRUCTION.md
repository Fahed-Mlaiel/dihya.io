# Guide Sécurité Construction

Consignes de sécurité pour le métier Construction.

## Sécurité applicative
- RBAC (roles, permissions, accès granulaire)
- Logs d’audit pour chaque action critique
- WAF, anti-DDOS, rate limiting, CORS strict
- Plugins validés et signés

## Bonnes pratiques
- Mise à jour régulière des dépendances (npm audit, pip-audit)
- Tests de pénétration (voir PENETRATION_TEST_REPORT.md)
- CI/CD : scans de sécurité automatisés à chaque build

## Checklist sécurité
- Authentification forte (MFA, JWT, OAuth2)
- Monitoring et alerting (logs, alertes, dashboards)
- Export des incidents (voir INCIDENTS_GUIDE.md)

## Outils
- OWASP ZAP, Snyk, Bandit, npm audit, pip-audit
