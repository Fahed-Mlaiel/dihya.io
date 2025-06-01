# e2e/ — Tests end-to-end (E2E) backend (Dihya Coding)

Ce dossier regroupe les tests end-to-end (E2E) pour le backend Flask Dihya Coding.

## Objectif

- Vérifier le fonctionnement global de l’application dans des scénarios proches de la réalité utilisateur.
- Tester les parcours critiques de bout en bout (authentification, génération, notifications, etc.).
- Détecter les régressions et les problèmes d’intégration multi-couches.

## Bonnes pratiques

- Organiser les tests par parcours ou fonctionnalité (`test_signup_e2e.py`, `test_generate_e2e.py`, etc.).
- Utiliser des environnements isolés et des jeux de données anonymisés.
- Nettoyer l’environnement de test avant/après chaque scénario.
- Documenter chaque test (but, étapes, sécurité, cas limites).
- Automatiser l’exécution des tests E2E dans la CI/CD.
- Logger les résultats et anomalies pour audit et amélioration continue.

## Exemple de structure

- `test_signup_e2e.py` : test E2E du parcours d’inscription.
- `test_generate_e2e.py` : test E2E de la génération de projet.
- `test_notifications_e2e.py` : test E2E de la réception de notifications.

## Exemple d’utilisation

```bash
pytest app/tests/e2e/