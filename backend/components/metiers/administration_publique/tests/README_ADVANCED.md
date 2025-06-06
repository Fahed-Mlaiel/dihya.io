# Tests Threed – Guide Avancé

## Stratégie
- Couvrir 100% du code (JS & Python)
- Tester chaque module indépendamment (utils, plugins, services, templates, fixtures, guides, legacy, etc.)
- Automatiser les tests (CI/CD, GitHub Actions, Docker)
- Générer des rapports de couverture (pytest-cov, jest, etc.)
- Vérifier la conformité RGPD, accessibilité, sécurité, souveraineté numérique

## Exemples d'exécution

### Python
```bash
pytest --cov=../ --cov-report=term-missing
```

### JavaScript
```bash
npm test -- --coverage
```

## Extension
- Ajouter de nouveaux tests à chaque évolution métier
- Documenter chaque scénario de test
- Utiliser des fixtures et mocks pour isoler les tests

## Bonnes pratiques
- Isoler les tests
- Générer des rapports automatisés (HTML, XML, Markdown)
- Intégrer les tests dans la CI/CD
- Garder la structure synchronisée avec les autres modules métiers
