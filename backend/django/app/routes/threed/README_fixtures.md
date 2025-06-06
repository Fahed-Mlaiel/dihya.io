# Fixtures – Django 3D API

Ce fichier documente l’utilisation des fixtures pour les tests et la conformité RGPD.

## Objectifs
- Fournir des jeux de données anonymisés, multilingues, RGPD-ready
- Tester l’import/export, la purge, la suppression logique

## Bonnes pratiques
- Toujours anonymiser les fixtures de test
- Couvrir tous les cas critiques (fr, en, ar, tzm)

## Exemple
- Fichiers de test dans `tests.py` et `models.py`

## RGPD & anonymisation
- Toutes les fixtures sont anonymisées, RGPD-ready, multilingues
- Suppression logique et export RGPD testés automatiquement

## Plugins & métiers
- Fixtures pour plugins métiers, extensions, marketplace
- Exemples dans `EXAMPLES_ADVANCED.md`

## Multitenant
- Jeux de données pour plusieurs tenants simulés

---

> Voir aussi : `README.md`, `EXAMPLES_ADVANCED.md`, guides RGPD, audit, plugins, multilingue, accessibilité.
