# Exemples métiers – Atoms

- `Button.jsx` : Bouton accessible, multilingue, versionné
- `Input.jsx` : Champ de saisie avec validation RGPD
- `Icon.jsx` : Icône universelle, compatible thème et accessibilité

## Exemple d’intégration
```js
import Button from './Button.jsx';
import Input from './Input.jsx';

function Formulaire() {
  return (
    <form>
      <Input label="Nom" />
      <Button label="Envoyer" />
    </form>
  );
}
```
