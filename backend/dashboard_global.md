# Dashboard Global Conformité & Monitoring – Dihya

Ce dashboard centralise les indicateurs clés de conformité, sécurité, accessibilité, RGPD, multilingue, plugins, CI/CD, incidents, auditabilité pour l’ensemble de la plateforme Dihya (backend, core, DB, plugins, etc.).

## 🏅 Badges de conformité & couverture

- **Conformité backend** : ![Badge conformité backend](backend/compliance/reports/badge_conformite.svg)
- **Conformité core** : ![Badge conformité core](backend/compliance/reports/badge_conformite.svg)
- **Couverture tests DB** : ![Badge couverture DB](backend/db/tests/coverage_db_badge.svg)

## 📊 Indicateurs globaux

- **Dernier build CI/CD** : `{{ build_date }}`
- **Statut global conformité** : `{{ global_status }}`
- **Langues supportées** : fr, en, ar, ber, de, zh, ja, ko, nl, he, fa, hi, es
- **Tests compliance** : `{{ compliance_tests }}`
- **Tests core** : `{{ core_tests }}`
- **Tests DB** : `{{ db_tests }}`
- **Incidents détectés** : `{{ incidents }}`
- **Plugins actifs** : `{{ plugins }}`
- **Dernier audit RGPD** : `{{ last_audit }}`

## 📈 Graphiques globaux (exemple)

```mermaid
pie title Répartition des tests
    "Compliance" : {{ compliance_success }}
    "Core" : {{ core_success }}
    "DB" : {{ db_success }}
    "Échecs" : {{ global_fail }}
```

## 📝 Logs & rapports globaux

- [Rapport monitoring CI/CD](../../monitoring_report.md)
- [Logs d’audit globaux](../backend/assets/logs/)
- [Rapports RGPD](../backend/compliance/rgpd/)
- [Rapports DB](../backend/db/migrations/)

---

> Ce dashboard est généré automatiquement à chaque build CI/CD pour garantir la conformité, la sécurité, l’accessibilité et l’auditabilité de toute la plateforme Dihya.
