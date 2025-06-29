# Exemples métiers i18n

## Exemple 1 : Affichage multilingue
```js
import { t, setLanguage } from './i18n';
setLanguage('es');
console.log(t('welcome'));
```

## Exemple 2 : Détection automatique de la langue
```js
import { localeUtils } from './localeUtils';
const userLang = localeUtils.detectLanguage();
```

## Exemple 3 : Traduction automatique
```js
import { autoTranslate } from './autoTranslate';
autoTranslate('Hello', 'ar');
```
