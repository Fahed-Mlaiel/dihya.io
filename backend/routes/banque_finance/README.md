# API Banque/Finance – Dihya Backend

Ce module expose des endpoints ultra avancés pour la gestion bancaire et financière : consultation de solde, virements, audit, conformité RGPD, extension plugin, etc.

## Fonctionnalités principales
- API REST sécurisée (JWT, RBAC, audit logging)
- Multilingue (fr, en, ar, amazigh)
- Conformité RGPD (logs, export, anonymisation)
- Extensible (plugins, hooks, templates métiers)
- Documentation OpenAPI, tests unitaires et intégration

## Endpoints principaux
- `GET /account/<username>` : consultation du solde (sécurisé, multilingue, audit)
- (À compléter) : virement, audit, export RGPD, gestion des rôles, etc.

## Sécurité & conformité
- Authentification JWT, gestion des rôles (admin, user, auditor)
- Audit logging horodaté, journalisation RGPD
- Limitation de débit, CORS, CSP, fallback open source

## Exemples d’utilisation
```bash
curl -H "Authorization: Bearer <token>" \
     "https://api.dihya.io/account/alice?lang=fr"
```

## Extension & personnalisation
- Ajoutez vos propres endpoints via plugins (voir dossier plugins/)
- Personnalisez les messages i18n dans le code

## Tests
- Couverture unitaire et intégration (voir tests/unit/ et tests/integration/)
- Exemples de tests multilingues, RBAC, RGPD

## Documentation
- OpenAPI : voir backend/app/openapi/
- Guide RGPD : voir compliance/audit_rgpd.py
- Guide sécurité : voir firewall/waf_middleware.py

---

> Ce module respecte le cahier des charges Dihya : sécurité, souveraineté, accessibilité, multilingue, extensibilité, conformité RGPD, performance, tests, documentation exhaustive.
