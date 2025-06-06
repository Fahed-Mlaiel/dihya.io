# Module accessibilité – API Threed

Ce dossier regroupe tous les modules, helpers, hooks et tests liés à l’accessibilité pour l’API Threed (JS & Python).

## Structure modulaire professionnelle
- `accessibility.js` / `accessibility.py` : logique d’accessibilité, vérification, logs, hooks, conformité WCAG/ARIA/RGAA
- `accessibility.test.js` / `accessibility.test.py` : tests unitaires et d’intégration synchronisés JS/Python
- `__init__.js` / `__init__.py` : points d’entrée modulaires, exposant explicitement les helpers et hooks
- `__init__.test.js` / `__init__.test.py` : tests d’intégration des points d’entrée

## Bonnes pratiques & conformité
- Respect strict des standards WCAG, ARIA, RGAA, RGPD
- Couverture de tous les endpoints critiques (audit accessibilité, logs, hooks)
- Synchronisation JS/Python : toute logique métier doit exister dans les deux langages
- Documentation et typage de chaque helper et test
- Intégration à la CI/CD et à l’audit global (tests automatiques, auditabilité, logs)
- Aucun code métier dans les points d’entrée : tout doit passer par les helpers

## Exemples d’utilisation

### JS
```js
const { checkAccessibility } = require('./accessibility');
const entity = { label: 'Bouton valider' };
if (checkAccessibility(entity)) {
  // Accessible, log ou suite du traitement
}
```

### Python
```python
from .accessibility import check_accessibility
entity = {'label': 'Bouton valider'}
if check_accessibility(entity):
    # Accessible, log ou suite du traitement
```

## Tests & CI/CD
- Chaque helper est testé unitairement et en intégration (voir fichiers `.test.js` et `.test.py`)
- Les tests sont synchronisés JS/Python et intégrés à la CI/CD
- Toute modification déclenche l’audit automatique

## Audit & extension
- Ce module est auditable, extensible, et conforme aux exigences métier Threed
- Pour toute extension, ajouter le helper dans `accessibility.js`/`.py` et l’exposer dans `__init__`
- Voir guides RGPD, accessibilité, audit dans le dossier `guides/` du projet

---
Pour toute question, voir le README principal du module ou contacter l’équipe métier Threed.
