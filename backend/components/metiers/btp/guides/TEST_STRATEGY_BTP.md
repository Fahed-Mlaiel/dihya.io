# Stratégie de Test BTP

Stratégies de tests unitaires, d’intégration et E2E pour le BTP.

## Checklist tests
- Tests unitaires (validation, sécurité, RGPD, plugins)
- Tests d’intégration (API REST/GraphQL, multitenancy, audit, accessibilité)
- Tests E2E (scénarios réels, CI/CD, multilingue)
- Plugins de test (mock, audit, RGPD, accessibilité)
- Export et anonymisation des jeux de tests
- Auditabilité des résultats, logs structurés
- Multilingue : assertions, logs, rapports

## Exemples
```python
def test_btp_main():
    assert 'chantier' in {'chantier': 'test'}
```
