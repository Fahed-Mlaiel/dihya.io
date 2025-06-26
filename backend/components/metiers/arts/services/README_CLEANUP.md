# Nettoyage de la structure du dossier services

- Les fichiers `services_arts.py` et `services_arts.js` sont supprimés pour éviter toute confusion et redondance.
- Toute la logique avancée (agrégation, cycle de vie, audit, activation, désactivation, QA, CI/CD) est centralisée dans `services.py` (Python) et `services.js` (JS).
- Les helpers avancés sont dans `services_helper.py` et `services_helper.js`.
- Les fichiers principaux à utiliser sont :
  - `service_arts.py` / `service_arts.js` (logique métier principale)
  - `services.py` / `services.js` (gestion avancée)
  - `services_helper.py` / `services_helper.js` (helpers)
  - `services_controller.py` / `services_controller.js` (contrôleurs)
  - `api.py` / `api.js` (API)
  - `services_test.py` / `services.test.js` (tests)

## Synchronisation JS/Python et documentation intégrée assurées.
