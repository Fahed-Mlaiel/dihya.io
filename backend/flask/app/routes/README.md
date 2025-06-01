# routes/ — Définition des routes Backend Flask Dihya Coding

Ce dossier contient tous les modules de routes (blueprints) pour l’API Flask de Dihya Coding.

## Contenu

- **main.py** : Routes publiques (accueil, healthcheck, info, ping, echo, SEO).
- **auth.py** : Routes d’authentification (inscription, connexion, refresh, logout).
- **user.py** : Routes de gestion des utilisateurs (CRUD, profil, rôles).
- **generate.py** : Route de génération automatique de projet (IA, fallback, preview).
- **__init__.py** : Initialisation et déclaration des blueprints.

## Bonnes pratiques

- Organiser les routes par fonctionnalité dans des blueprints séparés.
- Documenter chaque route avec une docstring et, si possible, un schéma OpenAPI.
- Protéger les routes sensibles avec des décorateurs d’authentification/autorisation (JWT, rôles).
- Valider toutes les entrées utilisateur via des schémas Marshmallow ou des validateurs dédiés.
- Retourner des réponses JSON claires et standardisées (code, message, data).
- Gérer proprement les erreurs (404, 401, 403, 422, etc.) via le module error_handling.
- Séparer la logique métier dans les services, pas dans les routes.
- Logger chaque action critique (login, génération, suppression, etc.) pour audit.

## Exemple d’utilisation

```python
from app.routes import main, auth, user, generate

app.register_blueprint(main)
app.register_blueprint(auth, url_prefix="/api/auth")
app.register_blueprint(user, url_prefix="/api/users")
app.register_blueprint(generate, url_prefix="/api/generate")
```

## Sécurité

- Toujours authentifier les routes sensibles (JWT, OAuth2).
- Contrôler les permissions selon le rôle utilisateur.
- Ne jamais exposer de données sensibles dans les réponses ou logs.
- Valider et filtrer toutes les entrées utilisateur.

---

**Équipe Dihya Coding**