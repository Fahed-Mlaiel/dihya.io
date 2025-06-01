# Dashboard Conformité & Monitoring – Core Backend Dihya

Ce dashboard synthétise les indicateurs de conformité, sécurité, accessibilité, audit, RGPD, multilingue, plugins, CI/CD, incidents pour le cœur backend.

## 🏅 Badge conformité

![Badge conformité](../compliance/reports/badge_conformite.svg)

## 📊 Indicateurs clés (core)

- **Dernier build CI/CD** : `{{ build_date }}`
- **Statut conformité** : `{{ badge_status }}`
- **Langues supportées** : fr, en, ar, ber, de, zh, ja, ko, nl, he, fa, hi, es
- **Tests core** : `{{ core_tests }}`
- **Incidents détectés** : `{{ incidents }}`
- **Plugins actifs** : `{{ plugins }}`
- **Dernier audit sécurité** : `{{ last_audit }}`

## 📈 Graphiques (exemple)

```mermaid
pie title Tests Core
    "Succès" : {{ core_success }}
    "Échecs" : {{ core_fail }}
```

## 📝 Logs & rapports

- [Rapport monitoring core](../../../../monitoring_report.md)
- [Logs d’audit core](../../assets/logs/)
- [Rapports RGPD core](../../compliance/rgpd/)

## 🔗 Dashboard global

- [Dashboard global conformité/monitoring](../../dashboard_global.md)

---

> Ce dashboard est généré automatiquement à chaque build CI/CD pour garantir la conformité, la sécurité, l’accessibilité et l’auditabilité du core backend Dihya.
