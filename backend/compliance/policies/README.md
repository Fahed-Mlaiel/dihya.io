# Politiques de confidentialité & CGU – Dihya Compliance

Ce dossier regroupe toutes les politiques légales, CGU, privacy policies, mentions légales et leur gestion automatisée pour la plateforme Dihya Coding.

## 📚 Contenu du dossier

- **privacy_policy_*.md** : Politique de confidentialité multilingue (fr, en, ar, tzm, de, zh, ja, ko, nl, he, fa, hi, es)
- **cgu_*.md** : Conditions Générales d’Utilisation multilingues
- **legal_*.md** : Mentions légales multilingues
- **api_export_policies.py** : Politique d’export API (sécurité, RGPD, audit, plugins, i18n, REST/GraphQL)
- **EXAMPLES_API.md** : Exemples d’utilisation API, plugins, audit, tests

## 🛡️ Sécurité & conformité

- Sécurité maximale : CORS, JWT, validation stricte, audit, WAF, anti-DDOS, anonymisation RGPD
- Multitenancy, gestion des rôles (admin, user, invité)
- Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Extensible via plugins (ajout API/CLI)
- Auditabilité : logs structurés, export, anonymisation, accès exportable
- Conformité RGPD, portabilité, droit à l’oubli

## 🔗 Liens utiles

- [Guide RGPD](../../../LEGAL_COMPLIANCE_GUIDE.md)
- [Guide sécurité](../../../securite.md)
- [Guide audit](../../../AUDIT_LOGGING_GUIDE.md)
- [API OpenAPI](../../../openapi.yaml)
- [README global](../../../README.md)

## 📖 Documentation interactive OpenAPI/Swagger

- La documentation interactive de l’API d’export conforme RGPD, sécurité, plugins, audit, multilingue est générée automatiquement :
  - [openapi_export_policies.yaml](./openapi_export_policies.yaml)
  - Compatible Swagger UI, Redoc, Postman, GraphQL Playground
  - Authentification JWT, CORS, WAF, anti-DDOS, auditabilité, anonymisation, plugins, fallback IA
  - Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)

### Exemple d’utilisation Swagger UI

```bash
# Lancer un serveur local de documentation interactive (nécessite swagger-ui ou redoc-cli)
npx swagger-ui-watcher ./openapi_export_policies.yaml
# ou
npx redoc-cli serve ./openapi_export_policies.yaml
```

- Documentation également intégrée dans les routes FastAPI/GraphQL (voir exemples dans api_export_policies.py)

## 🧑‍💻 Bonnes pratiques

- Documenter chaque modification (audit, logs, reviewers)
- Traduire chaque politique dans toutes les langues supportées
- Tester chaque endpoint d’export (unit, intégration, e2e)
- Utiliser les plugins pour anonymisation, conformité, extension
- Ne jamais stocker de données sensibles sans consentement explicite

## 📝 Exemples d’utilisation

Voir le fichier [EXAMPLES_API.md](./EXAMPLES_API.md) pour des exemples d’appels API, d’export, de plugins RGPD, de logs d’audit, etc.

---

> **Dihya Coding : conformité, sécurité, auditabilité, extensibilité et souveraineté numérique pour chaque projet.**
