# Dihya Frontend – Tests (exemple)

Ce dossier contient des exemples de tests unitaires, d’intégration, e2e et accessibilité pour le frontend Dihya.

Exemple de test unitaire (Jest) :

```js
import { render, screen } from '@testing-library/react';
import App from '../../App';
test('affiche le texte de bienvenue', () => {
  render(<App />);
  expect(screen.getByText(/Hello, Dihya Frontend!/i)).toBeInTheDocument();
});
```

Utilisation : voir README principal et src/tests/README.md
