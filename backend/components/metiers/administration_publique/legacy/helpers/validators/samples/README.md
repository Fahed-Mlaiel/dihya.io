# Samples – Legacy Helpers Validators

Ce dossier contient des exemples d’utilisation (samples) pour les helpers de validation legacy du module `threed`. Il est structuré pour permettre une découverte automatique, des tests unitaires exhaustifs et une documentation générée automatiquement.

## Structure du dossier

- `__init__.py` : Point d’entrée Python du sous-module samples.
- `__init__.test.py` : Test d’import du point d’entrée.
- `sample_validator.py` : Exemple concret d’implémentation d’un helper de validation legacy.
- `sample_validator.test.py` : Test unitaire associé au sample principal.
- `sample_validator.js` : Version JS synchronisée du sample (si applicable).
- `sample_validator.test.js` : Test unitaire JS du sample (si applicable).

## Exemples d’utilisation

```python
from backend.components.metiers.threed.legacy.helpers.validators.samples import sample_validator
result = sample_validator.validate_legacy_sample(data)
```

## Bonnes pratiques
- Tous les samples sont testés (Python & JS).
- Synchronisation JS/Python assurée.
- Prêt pour CI/CD et documentation automatique.
- Respect de la logique métier et du cahier des charges.

## CI/CD & Documentation
- Les tests sont automatiquement détectés et exécutés.
- La documentation de chaque sample est générée à partir de ce README et des docstrings.

## Conformité
- Structure modulaire, sans doublons, 100% testée, prête pour audit.
- Respect strict des conventions du projet `threed`.
