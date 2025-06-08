# README – Tests ultra avancés pour fixtures/samples

Ce dossier regroupe tous les tests unitaires, d’intégration et de conformité pour fixtures/samples (JS & Python).

- Respecte la logique métier, la structure modulaire et le cahier des charges Dihya.
- Synchronisation JS/Python, documentation automatique, auditabilité CI/CD.
- Découverte automatique, initialisation clé en main, prêt pour pipelines CI/CD.
- Exemples d’utilisation et structure extensible pour tous les samples métiers.

## Structure
- `samples.test.js` / `samples.test.py` : tests ultra avancés JS/Python pour chaque sample
- `__init__.js` / `__init__.py` : initialisation, auto-discovery, exécution clé en main

## Exécution
- Python : `pytest` dans ce dossier
- JS : `jest` ou `npm test` dans ce dossier

## Documentation
La documentation est générée automatiquement et synchronisée avec le code métier. Voir le README racine pour la stratégie globale.
