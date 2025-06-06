# Multilingue – Django 3D API

Ce fichier documente la gestion multilingue des endpoints, serializers, logs, templates, tests, etc.

## Bonnes pratiques
- Traduire tous les messages, erreurs, logs, notifications (fr, en, ar, tzm)
- Tester l’internationalisation dans les tests unitaires et d’intégration

## Langues supportées (production)
- Français (fr), Anglais (en), Arabe (ar), Amazigh (tzm), Allemand (de), Chinois (zh), Japonais (ja), Coréen (ko), Néerlandais (nl), Hébreu (he), Persan (fa), Hindi (hi), Espagnol (es)

## Tests multilingues automatisés
- Tous les messages API, logs, erreurs, notifications sont testés dans les 13 langues
- Exemples dans `EXAMPLES_ADVANCED.md` et `tests.py`

## Accessibilité multilingue
- Tous les messages d’erreur sont accessibles (a11y), testés avec axe/Lighthouse/pa11y

## Plugins multilingues
- Les plugins peuvent déclarer leurs propres messages multilingues (voir `plugins.py`)

---

> Voir aussi : `README.md`, `EXAMPLES_ADVANCED.md`, guides dans `../../../../docs/`, badge multilingue dans la CI/CD.
