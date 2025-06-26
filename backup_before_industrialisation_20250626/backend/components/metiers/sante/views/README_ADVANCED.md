/* global console */
# Vues Sante – Documentation Ultra Avancée

Ce dossier contient :
- Helpers JS et Python pour le rendu de vues
- Exemples de rendu HTML dynamique

## Exemples JS
```js
const { renderTitle } = require('./views_helper');
console.log(renderTitle('Titre'));
```

## Exemples Python
```python
from .views_helper import render_title
print(render_title('Titre'))
```

# Vues Sante – Guide Avancé

## Exemples d'utilisation

```js
const { renderSanteView } = require('./index');
const data = { name: 'Objetsante', status: 'active' };
console.log(renderSanteView(data));
```

## Accessibilité
- Toujours fournir des labels explicites
- Prévoir des alternatives textuelles pour les rendus sante

## Bonnes pratiques
- Séparer la logique de rendu et les helpers
- Tester chaque vue indépendamment
