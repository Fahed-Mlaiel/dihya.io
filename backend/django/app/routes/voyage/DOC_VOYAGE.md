# DOC_VOYAGE.md
# Documentation technique et métier générée automatiquement pour le module voyage.
# (Ce fichier est généré par le script gen_doc.sh)

## Présentation
Le module voyage gère la gestion, la réservation, l’audit et l’export RGPD des voyages (transport, hébergement, activités), avec conformité RGPD, accessibilité, sécurité, performance, plugins, templates métiers, tests exhaustifs, scripts robustes, et documentation multilingue.

## Endpoints principaux
- /voyage/reservations/ (CRUD réservations)
- /voyage/itineraires/ (CRUD itinéraires)
- /voyage/rgpd-export/ (export RGPD)

## Plugins & templates
- plugins.py : suggestion d’itinéraire
- templates.py : confirmation de réservation

## Scripts
- scripts/rgpd_export.sh, rgpd_cleanup.sh, backup_voyage.sh, run_tests.sh, gen_doc.sh, etc.

## Tests
- tests/ : unitaires, intégration, e2e, accessibilité, performance, plugins

## Conformité
- RGPD, accessibilité, sécurité, audit, multilingue, souveraineté numérique

## Voir aussi
- README_multilingue.md, README_accessibilite_rgpd.md, audit.py, i18n.py, fixtures.json
