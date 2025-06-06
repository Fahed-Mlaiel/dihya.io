# Tests d’intégration multi-modules Threed

Ce dossier est destiné à accueillir les tests d’intégration couvrant plusieurs modules métier (API, services, plugins, templates, etc.).

- Placer ici les tests d’intégration transverses, scénarios bout-en-bout, tests de synchronisation JS/Python, etc.

# Tests d’intégration des points d’entrée globaux (index/init)

Ce dossier regroupe les tests d’intégration pour les points d’entrée globaux du module Threed :
- `index.test.js`, `index.test.py` : tests d’intégration JS/Python pour index.js/index.py
- `init.test.js`, `init.test.py` : tests d’intégration JS/Python pour init.js/init.py

Ces tests garantissent la cohérence, la synchronisation et la conformité des points d’entrée globaux du module.
