# README – Tests unitaires des fixtures voice (Python & JS, synchronisés)

Ce dossier contient des tests unitaires pour tous les helpers, mocks et validateurs de fixtures Python et JavaScript, synchronisés et conformes au cahier des charges Dihya.

- `helpers/` : tests des helpers métiers (JS & Python)
- `validators/` : tests des validateurs (JS & Python)
- `mocks/` : tests des mocks (JS & Python)
- `core/` : tests des générateurs et modèles (JS & Python)

## Exécution (Python)

```bash
pytest .
```

## Exécution (JS)

```bash
npm test
```

## Bonnes pratiques

- Couvrir tous les points d’entrée (`__init__`, `index`, samples)
- Tester la synchronisation JS/Python et la conformité RGPD/accessibilité
- Ajouter des edge cases et des tests d’intégration à chaque évolution
