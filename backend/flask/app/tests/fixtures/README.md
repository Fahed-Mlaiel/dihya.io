# fixtures/ — Jeux de données et mocks de test (Dihya Coding)

Ce dossier regroupe les jeux de données, mocks et fixtures utilisés pour les tests du backend Flask Dihya Coding.

## Objectif

- Fournir des données de test réalistes, anonymisées et reproductibles pour les tests unitaires, d’intégration et E2E.
- Centraliser la création de mocks pour les services externes (API, emails, stockage, etc.).
- Faciliter la maintenance et l’extension des scénarios de test.

## Bonnes pratiques

- Organiser les fixtures par domaine ou module (`user_fixtures.py`, `project_fixtures.py`, etc.).
- Utiliser des données anonymisées et jamais de secrets réels.
- Documenter chaque fixture (usage, structure, sécurité).
- Prévoir des helpers pour générer dynamiquement des jeux de données variés.
- Nettoyer l’environnement de test avant/après chaque scénario utilisant des fixtures.
- Versionner les jeux de données critiques pour la reproductibilité.

## Exemple de structure

- `user_fixtures.py` : utilisateurs de test.
- `project_fixtures.py` : projets de test.
- `mock_services.py` : mocks pour les services externes (emails, paiements, etc.).

## Exemple d’utilisation

```python
from app.tests.fixtures.user_fixtures import create_test_user

def test_signup(client):
    user = create_test_user()
    response = client.post("/api/signup", json=user)
    assert response.status_code == 201