# Intégration des polices dans le code

## Exemple Next.js/React
```js
import { OpenSans } from './index.js';
const style = { fontFamily: 'Open Sans, Arial, sans-serif' };
<h1 style={style}>Bienvenue</h1>
```

## Intégration dans ThemeProvider
```js
export const theme = {
  fonts: {
    primary: 'Open Sans, Arial, sans-serif',
    secondary: 'Roboto, Arial, sans-serif'
  }
};
```
