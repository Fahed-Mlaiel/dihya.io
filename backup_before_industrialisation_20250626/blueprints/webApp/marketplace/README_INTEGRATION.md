# Guide d’intégration du marketplace (clé en main)

## Utilisation dans une page React
```jsx
import Marketplace from './Marketplace';

export default function MarketplacePage() {
  return <Marketplace />;
}
```

## Ajout dynamique de templates/plugins
```js
import { addTemplate } from './gestion_templates';
addTemplate({ name: 'ERP Retail', secteur: 'Retail', version: '1.0.0' });

import { addPlugin } from './gestion_plugins';
addPlugin({ name: 'Monitoring Pro', type: 'monitoring', version: '1.0.0' });
```

## Administration avancée
```jsx
import MarketplaceAdmin from './MarketplaceAdmin';

export default function AdminMarketplace() {
  return <MarketplaceAdmin />;
}
```

## Extension automatique (exemple)
```js
addPlugin({ name: 'AI Assistant', type: 'ia', version: '1.0.0', features: ['chatbot', 'analyse prédictive'] });
```

## Audit, logs, CI/CD
- Tous les ajouts/suppressions sont logués et audités.
- Prêt pour l’intégration continue, l’automatisation, la personnalisation.
