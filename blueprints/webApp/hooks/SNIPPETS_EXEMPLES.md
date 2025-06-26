# Exemples de snippets pour les hooks

## Authentification
```js
import { useAuth } from './useAuth';
const { user, login, logout } = useAuth();
```

## Thème
```js
import { useTheme } from './useTheme';
const { theme, setTheme } = useTheme();
```

## Traduction
```js
import { useTranslation } from './useTranslation';
const { t, language } = useTranslation();
```

## Marketplace
```js
import { useMarketplace } from './useMarketplace';
const { items, addItem } = useMarketplace();
```

## Notification
```js
import { useNotification } from './useNotification';
const { notify } = useNotification();
```
