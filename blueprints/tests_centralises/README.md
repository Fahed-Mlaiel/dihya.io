# Tests centralisés (tests_centralises)

Ce dossier contient les tests ultra avancés, centralisés et structurés pour tous les blueprints métiers.

## Fonctionnalités
- Découverte automatique des tests (Node.js & Python)
- Exécution de toutes les suites de tests avec reporting détaillé
- Intégration CI/CD prête à l'emploi
- Exemples de tests pour chaque domaine métier

## Exécution

### Node.js
```js
const { runAllTests } = require('./tests_centralises');
const results = runAllTests();
console.log(results);
```

### Python
```python
from tests_centralises import run_all_tests
result = run_all_tests()
print(result)
```

## Bonnes pratiques
- Ajoutez vos tests dans ce dossier pour chaque nouveau blueprint métier
- Utilisez les runners fournis pour automatiser la validation

