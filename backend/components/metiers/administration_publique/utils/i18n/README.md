# Dossier i18n – Module threed

Ce dossier regroupe les utilitaires d’internationalisation (i18n) et de traduction pour le module métier Threed (3D).

## Contenu
- `i18n.js` / `i18n.py` : Fonctions de traduction, fallback multilingue, helpers i18n.
- `index.js`, `__init__.py`, `__init__.js` : Points d’entrée centralisés pour l’import et l’intégration CI/CD.
- Tests unitaires et d’intégration JS & Python pour chaque utilitaire.

## Conformité & Sécurité
- Respect RGPD : pas de stockage de données personnelles dans les helpers i18n.
- Accessibilité : helpers compatibles avec les besoins multilingues et accessibles.
- Souveraineté numérique : code open source, aucune dépendance à des services externes propriétaires.
- Sécurité : helpers testés, auditables, robustes.

## Tests & Qualité
- Couverture de tests exhaustive (unitaires, intégration, edge cases).
- Intégration continue (CI/CD) : chaque modification déclenche les tests automatiques.

## Exemples d’usage
- Traduction fallback : `i18n('Bonjour', 'en')` → `[EN] Bonjour`
- Fallback inconnu : `i18n('Test', 'es')` → `Test`

## Documentation avancée
- Voir guides RGPD, sécurité, accessibilité, i18n dans le dossier `guides/` du module threed.

# i18n – Structure avancée et synchronisation JS/Python

Ce module fournit une structure professionnelle pour l’internationalisation métier, la traçabilité, la conformité et l’intégration CI/CD.

## Structure modulaire
- `core/` : logique métier principale (i18n.js, i18n.py, tests)
- `helpers/` : helpers i18n (fonctions utilitaires, tests, README)
- `fallback/` : fallback i18n (gestion d’échec, tests, README)
- `samples/` : exemples d’utilisation, helpers, cas métiers
- Fichiers d’organisation/init : `__init__.js`, `__init__.py`, `index.js`, `index.test.js`, `index.test.py`, `__init__.test.js`, `__init__.test.py`

## Synchronisation JS/Python
- Tous les sous-modules sont exposés via les points d’entrée JS (`__init__.js`, `index.js`) et Python (`__init__.py`)
- Importation centralisée :
  - JS : `const i18n = require('./utils/i18n');`
  - Python : `from .utils.i18n import *`

## Bonnes pratiques
- Un helper = une fonction réutilisable, testée, documentée
- Un fallback = une solution de secours robuste, testée
- Le core = la logique métier principale, testée
- Ajoutez des tests d'intégration dans chaque sous-dossier si besoin
- Respectez la conformité, la traçabilité et la logique métier

## Exemples d’utilisation

### JS
```js
const { sampleI18n } = require('./samples/sample_i18n_helper');
sampleI18n('fr', 'Bonjour');
```

### Python
```python
from .samples.sample_i18n_helper import sample_i18n
sample_i18n('fr', 'Bonjour')
```

## CI/CD & Audit
- Tous les points d’entrée et helpers sont testés (import, unitaires, intégration)
- Structure prête pour audit automatique et documentation continue
- Conforme aux exigences métier et sécurité

---
Pour toute extension, créez un sous-dossier dédié (ex : `adapters/`, `formats/`, etc.) selon la logique métier.
