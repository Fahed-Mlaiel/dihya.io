# Politique de sécurité Dihya

## Exigences principales
- CORS strict, whitelist dynamique, logs d'accès.
- Authentification JWT, refresh token, rotation, blacklist.
- Validation stricte des entrées (type hints, pydantic/django forms).
- Audit logging (toutes actions sensibles, export CSV/JSON, anonymisation RGPD).
- WAF intégré (OWASP Top 10, anti-DDOS, anti-bot, rate limiting).
- Sécurité GraphQL (depth limiting, introspection off en prod).
- Plugins de sécurité extensibles (API/CLI).
- Multitenancy et RBAC avancé (admin, user, invité, custom roles).
- Internationalisation dynamique (fr, en, ar, tzm, de, zh, ja, ko, nl, he, fa, hi, es).
- Conformité RGPD, logs exportables, anonymisation, consentement explicite.

## Bonnes pratiques
- Jamais de secret en dur, rotation automatique.
- Tests automatisés pour chaque règle de sécurité.
- Documentation intégrée (docstring, README, policy.md).
- Déploiement sécurisé (GitHub Actions, Docker, K8s, fallback local).

---

# Dihya Security Policy (EN)

See above for all requirements and best practices. All security rules are enforced and tested automatically.
