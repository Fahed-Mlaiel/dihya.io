# Exemples métiers de composants

- `ThemeSwitcher.jsx` : Composant de changement de thème (dark/light, amazigh, etc.)
- `LanguageSwitcher.jsx` : Sélecteur de langue multilingue
- `VoiceInput.jsx` : Entrée vocale avec reconnaissance multilingue
- `ChatAssistant.jsx` : Assistant IA intégré

## Exemple d’intégration
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

## Exemple métier réel
```js
import ChatAssistant from './ChatAssistant.jsx';

function SupportWidget() {
  return <ChatAssistant secteur="banque" langue="fr" />;
}
```

## Convention Lead Dev
- Exemples métiers réels, multilingues, accessibilité, branding
- Documenter chaque nouveau composant métier
