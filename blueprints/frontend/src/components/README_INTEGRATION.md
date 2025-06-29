# Guide d’intégration des composants

## Exemple Next.js/React
```js
import { Button } from './atoms';
import { Form } from './molecules';
import { Navbar } from './organisms';
import { MainTemplate } from './templates';

function App() {
  return (
    <MainTemplate>
      <Navbar />
      <Form />
      <Button label="Envoyer" />
    </MainTemplate>
  );
}
```

## Exemple d’intégration métier
```js
import ThemeSwitcher from './ThemeSwitcher.jsx';
import LanguageSwitcher from './LanguageSwitcher.jsx';

function Header() {
  return (
    <div>
      <ThemeSwitcher />
      <LanguageSwitcher />
    </div>
  );
}
```

## Convention Lead Dev
- Utiliser les composants globaux, jamais de duplication dans les features
- Respecter atomicité, accessibilité, typage, multilingue, branding
- Documenter chaque intégration métier réelle
