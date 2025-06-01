# DOC_VOICE.md
# Documentation technique et métier générée automatiquement pour le module voice.
# (Ce fichier est généré par le script gen_doc.sh)

## Présentation
Le module voice gère l’upload, la gestion, la transcription et l’audit de fichiers audio multilingues, avec conformité RGPD, accessibilité, sécurité, performance, plugins, templates métiers, tests exhaustifs, scripts robustes, et documentation multilingue.

## Endpoints principaux
- /voice/audiofiles/ (CRUD fichiers audio)
- /voice/transcriptions/ (CRUD transcriptions)
- /voice/rgpd-export/ (export RGPD)

## Plugins & templates
- plugins.py : analyse de sentiment
- templates.py : rapport de transcription
- templates_rgpd.py : export RGPD

## Scripts
- scripts/rgpd_export.sh, rgpd_cleanup.sh, backup_voice.sh, run_tests.sh, gen_doc.sh, etc.

## Tests
- tests/ : unitaires, intégration, e2e, accessibilité, performance, plugins

## Conformité
- RGPD, accessibilité, sécurité, audit, multilingue, souveraineté numérique

## Voir aussi
- README_multilingue.md, README_accessibilite_rgpd.md, audit.py, i18n.py, fixtures.json
