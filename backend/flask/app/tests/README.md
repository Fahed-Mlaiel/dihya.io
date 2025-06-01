# tests/ — Tests unitaires et d'intégration Backend Flask Dihya Coding

Ce dossier contient tous les tests pour le backend Flask de Dihya Coding.

## Organisation

- **test_main.py** : Tests des routes publiques (accueil, healthcheck, info, ping, echo, SEO).
- **test_auth.py** : Tests des routes d'authentification (inscription, connexion, refresh, logout).
- **test_user.py** : Tests des routes de gestion utilisateur (CRUD, profil, rôles).
- **test_routes.py** : Tests d'intégration pour la présence, la sécurité et les méthodes autorisées sur les routes.
- **conftest.py** : Fixtures et configuration globale pour pytest.
- **__init__.py** : Initialisation du package de tests.

## Bonnes pratiques

- Utiliser **pytest** pour tous les tests.
- Organiser les tests par module/fonctionnalité.
- Utiliser des fixtures pour isoler les tests et garantir leur indépendance.
- Nettoyer la base de données ou les ressources entre chaque test.
- Documenter chaque test avec une docstring claire.
- Séparer les tests unitaires, d'intégration et de sécurité.
- Couvrir les cas d'erreur, de sécurité et de validation.

## Exécution des tests

Depuis le dossier `app` :

```bash
pytest
## Exemple d'utilisation

```python
# Voir la documentation du module pour un exemple précis
```

