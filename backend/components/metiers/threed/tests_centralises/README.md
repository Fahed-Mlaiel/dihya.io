# tests_centralises – Tests ultra avancés (clé en main)

Ce dossier regroupe tous les tests unitaires, d’intégration et de conformité pour le module Threed (JS & Python).

- `__init__.js` : initialisation continue, découverte automatique des tests JS
- `__init__.py` : initialisation continue, découverte automatique des tests Python
- Sous-dossiers : chaque sous-module (rgpd, plugins, templates, etc.) est centralisé et extensible

Respecte la logique métier (tests uniquement), la structure modulaire et le cahier des charges Dihya.
Synchronisation JS/Python, documentation automatique, auditabilité CI/CD, extension facile, documentation à chaque niveau.

## Structure
- `rgpd/` : tests RGPD ultra avancés
- `plugins/` : tests plugins ultra avancés
- `templates/` : tests templates ultra avancés
- ... autres sous-modules centralisés

## Initialisation & Découverte
Chaque sous-module possède des scripts d’initialisation (__init__.py, __init__.js) pour la découverte automatique des tests et l’intégration CI/CD.

## Exécution
- Python : utiliser `pytest` à la racine de ce dossier
- JS : utiliser `jest` ou `npm test` à la racine de ce dossier

## Documentation
La documentation est générée automatiquement et synchronisée avec le code métier.

> Architecture prête pour extension, audit, synchronisation JS/Python, et industrialisation des tests centralisés.
