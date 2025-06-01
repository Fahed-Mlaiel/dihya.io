# Dossier `middleware/` — Backend Dihya Coding

Ce dossier contient tous les middlewares personnalisés utilisés pour sécuriser, contrôler et améliorer le backend Dihya Coding.

## Bonnes pratiques Dihya Coding

- **Centralisation** : tous les middlewares (CORS, rate limiting, audit, etc.) sont regroupés ici pour une gestion claire et évolutive.
- **Configuration stricte** : chaque middleware doit être paramétré pour éviter les failles de sécurité (ex : whitelist CORS, limites de requêtes…).
- **Extensibilité** : prévoir l’ajout facile de nouveaux middlewares sans modifier la logique métier.
- **Sécurité** : ne jamais activer un middleware critique sans validation de sa configuration.
- **Documentation** : chaque middleware doit être documenté (usage, paramètres, exemples).

## Exemples de middlewares présents

- `cors.py` : gestion fine des politiques CORS (origines, headers, credentials…)
- `rate_limit.py` : protection contre les abus (DoS, brute force…) par limitation de requêtes
- `__init__.py` : point d’entrée pour l’enregistrement centralisé des middlewares dans l’app Flask

## Utilisation

Dans votre `create_app()` ou `app/__init__.py` :

```python
from middleware import register_middlewares

def create_app():
    app = Flask(__name__)
    register_middlewares(app)
    # ...
    return app
```

---

*Ce dossier fait partie de la documentation technique interne Dihya Coding.*