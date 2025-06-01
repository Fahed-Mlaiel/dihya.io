# Dashboard Conformité & Monitoring – Dihya

Ce dashboard synthétise les indicateurs de conformité, accessibilité, audit, RGPD, multilingue, plugins, sécurité, CI/CD, incidents, SLA.

## 🏅 Badge conformité

![Badge conformité](badge_conformite.svg)

## 📊 Indicateurs clés

- **Dernier build CI/CD** : `{{ build_date }}`
- **Statut conformité** : `{{ badge_status }}`
- **Langues supportées** : fr, en, ar, ber, de, zh, ja, ko, nl, he, fa, hi, es
- **Tests compliance** : `{{ compliance_tests }}`
- **Incidents détectés** : `{{ incidents }}`
- **Dernier audit RGPD** : `{{ last_audit }}`
- **Plugins actifs** : `{{ plugins }}`

## 📈 Graphiques (exemple)

```mermaid
pie title Tests Compliance
    "Succès" : {{ compliance_success }}
    "Échecs" : {{ compliance_fail }}
```

## 📝 Logs & rapports

- [Rapport monitoring CI/CD](../../../../monitoring_report.md)
- [Logs d’audit](../../../../Dihya/backend/assets/logs/)
- [Rapports RGPD](../../rgpd/)
- [Rapports provenance](../../provenance/)

## 🔗 Dashboard global

- [Dashboard global conformité/monitoring](../../../dashboard_global.md)

---

> Ce dashboard est généré automatiquement à chaque build CI/CD pour garantir la conformité, la souveraineté, l’accessibilité et l’auditabilité de Dihya.
