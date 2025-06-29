# README_EXEMPLES.md – Locales

## Exemples d’intégration métier

### Import d’une locale
```js
import fr from './fr.json';
```

### Utilisation dans un composant
```js
import { useTranslation } from '../../hooks/useTranslation';
const { t } = useTranslation();
<t('accueil') />
```

### Ajout d’une nouvelle langue
```js
// Ajouter xx.js et xx.json, puis référencer dans i18n.js
```
