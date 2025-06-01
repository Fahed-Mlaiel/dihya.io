# Exemples d’utilisation avancés du core Dihya

## 1. Utilisation avancée avec Flask (Python)

```python
from Dihya.backend.core.app import create_app
from flask import request

app = create_app()

@app.route('/api/secure-data')
@require_role('admin')
def secure_data():
    return {'data': 'secret', 'lang': request.headers.get('X-Dihya-Lang', 'fr')}

if __name__ == '__main__':
    app.run(debug=True)
```

## 2. Utilisation avancée avec Express (Node.js)

```js
const express = require('express');
const core = require('./backend/core');
const app = express();

app.use(core.securityHeaders);
app.use('/api/secure', core.rbac('admin'), (req, res) => {
  res.json({ data: 'secret', lang: core.getLang(req) });
});

app.listen(8000, () => core.log('info', 'Serveur Express démarré', { service: 'core' }));
```

## 3. Plugins dynamiques (Python)

```python
# Dans Dihya/backend/plugins/mon_plugin.py

def register_plugin(app):
    @app.route('/api/mon_plugin')
    def mon_plugin():
        return {'plugin': 'ok'}
```

## 4. Plugins dynamiques (Node.js)

```js
// Dans Dihya/backend/plugins/mon_plugin.js
module.exports = (app) => {
  app.get('/api/mon_plugin', (req, res) => res.json({ plugin: 'ok' }));
};
```

## 5. Utilisation CI/CD (GitHub Actions)

```yaml
jobs:
  test-core:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Installer dépendances Python
        run: pip install -r requirements-dev.txt
      - name: Lancer les tests core Python
        run: pytest Dihya/backend/core/tests/ --maxfail=1 --disable-warnings -v
      - name: Installer dépendances Node.js
        run: npm ci
      - name: Lancer les tests core Node.js
        run: npm run test:core
```
