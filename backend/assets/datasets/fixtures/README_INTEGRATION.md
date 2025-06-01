# Intégration automatique des fixtures générées

Ce dossier contient les fixtures générées automatiquement à partir des datasets (/assets/datasets/fixtures) pour les tests unitaires, d'intégration et e2e.

## Utilisation dans les tests Python

- Importez la fixture souhaitée dans vos tests :

```python
from Dihya.backend.assets.datasets.fixtures.users_sample_fixture import users_sample
```
- Utilisez-la comme argument de fonction de test avec pytest :

```python
def test_users_sample(users_sample):
    assert len(users_sample) > 0
```

## Automatisation CI/CD

Les tests utilisant ces fixtures sont automatiquement exécutés dans les pipelines GitHub Actions (voir `.github/workflows/test.yml`).

## Types de fixtures disponibles
- users_sample_fixture
- transactions_sample_fixture
- audit_events_sample_fixture

## Conformité
- Multilingue, RGPD, anonymisation, structure validée automatiquement.
- Génération et validation automatisées via `generate_fixtures.py` et `validate_datasets.py`.
