# README_tests.md – Tests, sécurité, conformité, CI/CD, API, RGPD, audit, accessibilité, monitoring, fallback IA, multitenancy, rôles, i18n, documentation intégrée

## Structure des templates métiers
- **finance_template.py** : Métier finance, anonymisation RGPD, audit, API, multitenancy, rôles, fallback IA, i18n, accessibilité
- **industrie_template.py** : Métier industrie, anonymisation RGPD, audit, API, multitenancy, rôles, fallback IA, i18n, accessibilité
- **rh_template.py** : Métier RH, anonymisation RGPD, audit, API, multitenancy, rôles, fallback IA, i18n, accessibilité
- **sante_template.py** : Métier santé, anonymisation RGPD, audit, API, multitenancy, rôles, fallback IA, i18n, accessibilité
- **api.py** : API REST/GraphQL ultra avancée pour tous les templates métiers (import dynamique, sécurité, audit, RGPD, i18n, monitoring, fallback IA, multitenancy, rôles, documentation intégrée)
- **tests_templates.py** : Tests automatisés ultra avancés (pytest, sécurité, RGPD, audit, anonymisation, conformité, CI/CD)

## Exécution des tests

```bash
# Depuis le dossier templates
pytest tests_templates.py
```

## Points de conformité et sécurité
- **RGPD** : anonymisation systématique, logs d’audit, conformité, documentation intégrée
- **Audit** : logs horodatés, monitoring, fallback IA, multitenancy, rôles, accessibilité
- **CI/CD** : tests automatisés, API testable, documentation, monitoring
- **i18n** : prise en charge multilingue (paramètre lang)
- **Documentation** : docstring, endpoint /doc, README, README_ultra.md

## API Métier (FastAPI)
- `/api/template/{domain}/process` : traitement métier, audit, RGPD, i18n, multitenancy, rôles
- `/api/template/{domain}/anonymize` : anonymisation RGPD
- `/api/template/{domain}/doc` : documentation intégrée

## Bonnes pratiques
- Sécurité maximale, aucun TODO, conformité RGPD, auditabilité, accessibilité, monitoring, fallback IA, multitenancy, rôles, i18n, documentation intégrée, tests complets, CI/CD.
