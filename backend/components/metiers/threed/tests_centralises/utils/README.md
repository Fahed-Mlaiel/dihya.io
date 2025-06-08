# utils – Tests ultra avancés (clé en main)

Ce dossier regroupe tous les tests unitaires, d’intégration et de conformité pour les utilitaires du module Threed (JS & Python).

- `index.js` : point d’entrée unique, auto-discovery, exports dynamiques JS ultra avancé
- `__init__.js` : initialisation continue, découverte automatique des tests JS
- `__init__.py` : initialisation continue, découverte automatique des tests Python
- Sous-dossiers : chaque sous-module (validators, views, etc.) est centralisé et extensible

Respecte la logique métier (tests uniquement), la structure modulaire et le cahier des charges Dihya.
Synchronisation JS/Python, documentation automatique, auditabilité CI/CD, extension facile, documentation à chaque niveau.

> Architecture prête pour extension, audit, synchronisation JS/Python, et industrialisation des tests utilitaires.
