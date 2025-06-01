# 🧪 Tests SEO – Dihya Coding

Ce dossier regroupe tous les scripts et modules de tests SEO pour Dihya Coding : validation des balises, accessibilité, indexabilité, robustesse, conformité RGPD, auditabilité, extensibilité et documentation claire.

---

## 🚀 Objectifs

- Vérifier la qualité SEO des pages et composants (balises, titres, descriptions, accessibilité, indexabilité…)
- Garantir la robustesse, la conformité RGPD et l’auditabilité des tests SEO
- Permettre l’extension facile à de nouveaux scénarios ou frameworks de tests SEO

---

## 📁 Structure recommandée

- `unit/` : Tests unitaires des fonctions SEO (balises, meta, etc.)
- `integration/` : Tests d’intégration (parcours SEO, accessibilité)
- `e2e/` : Tests end-to-end (indexabilité, robots, sitemap)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité & RGPD** : Pas de données personnelles dans les jeux de tests, logs anonymisés, consentement utilisateur pour les tests en production, droit à l’oubli (purge).
- **Auditabilité** : Historique local des campagnes de tests, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouveaux scénarios, modules ou frameworks de tests SEO.
- **Robustesse** : Gestion des erreurs, tests reproductibles, feedback détaillé.
- **SEO** : Documentation claire et structurée pour chaque type de test.
- **Documentation** : Docstring JSDoc pour chaque script de test, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
// Exemple de test unitaire de balise title
import { getPageTitle } from '../utils/seo';

test('balise title présente', () => {
  expect(getPageTitle('<title>Dihya Coding</title>')).toBe('Dihya Coding');
});
```

---

## 📚 Documentation associée

- [unit/](./unit/)
- [integration/](./integration/)
- [e2e/](./e2e/)
- [Sécurité & RGPD](../../docs/security.md)
- [Utils](../../utils/README.md)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : tests SEO modernes, robustes, extensibles et conformes RGPD pour chaque génération.**