# Exemples d’utilisation avancés – Tests DB Dihya

## 1. Générer un rapport de couverture automatisé

```bash
pytest --cov=. --cov-report=xml --cov-report=html
# Résultat : coverage_db.xml, htmlcov/index.html
```

## 2. Intégration CI/CD (GitHub Actions)

```yaml
jobs:
  test-db:
    name: 🗄️ Test DB (unit, integration, e2e, couverture)
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Installer dépendances Python
        run: pip install pytest pytest-cov
      - name: Lancer tous les tests DB + couverture
        run: |
          cd Dihya/backend/db/tests
          pytest --cov=. --cov-report=xml --cov-report=html
      - name: Archiver le rapport de couverture
        uses: actions/upload-artifact@v4
        with:
          name: db-coverage
          path: |
            Dihya/backend/db/tests/coverage_db.xml
            Dihya/backend/db/tests/htmlcov/
```

## 3. Reporting manuel

```bash
# Générer un rapport HTML lisible
pytest --cov=. --cov-report=html
xdg-open htmlcov/index.html
```

## 4. Exécution des tests e2e (performance, triggers, vues)

```bash
pytest test_e2e_db.py
```
