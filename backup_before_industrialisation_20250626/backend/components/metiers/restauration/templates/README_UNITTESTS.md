/* global console */
# README – Tests unitaires des templates RestauratioN

Ce dossier contient des tests unitaires pour tous les templates Jinja2, HTML, JSON, XML, JS.

## Python (pytest + Jinja2)
```python
import pytest
from jinja2 import Environment, FileSystemLoader

def test_rapport_audit_template():
    env = Environment(loader=FileSystemLoader('backend/components/metiers/restauration/templates'))
    template = env.get_template('rapport_audit.html.j2')
    result = template.render(date='2025-06-03', result='OK')
    assert '2025-06-03' in result
    assert 'OK' in result
```

## JS (Node.js)
```js
const fs = require('fs');
const rapport = fs.readFileSync('./rapport_audit.html.j2', 'utf8');
console.assert(rapport.includes('{{ date }}'));
```

## Bonnes pratiques
- Tester le rendu de chaque template avec des données valides et extrêmes
- Vérifier la sécurité (XSS, injection)
- Synchroniser les tests JS/Python
