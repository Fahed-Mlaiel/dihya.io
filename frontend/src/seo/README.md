# 🕸️ SEO – Dihya Coding

Ce dossier regroupe tous les modules et outils SEO pour Dihya Coding : gestion des balises, accessibilité, indexabilité, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Optimiser le référencement naturel (SEO) de toutes les pages et composants de l’application
- Garantir la conformité RGPD, la sécurité, l’auditabilité et la robustesse des pratiques SEO
- Permettre l’extension facile à de nouveaux outils, tests ou stratégies SEO

---

## 📁 Structure recommandée

- `metaManager.js` : Gestion dynamique des balises meta, titres, descriptions, canonical, etc.
- `sitemapGen.js` : Générateur de sitemap XML (indexabilité, logs, RGPD)
- `robotsGen.js` : Générateur de robots.txt (contrôle d’indexation)
- `tests/` : Scripts de tests SEO (unitaires, intégration, e2e)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité & RGPD** : Pas de données personnelles dans les balises/meta, logs anonymisés, consentement utilisateur pour les logs, droit à l’oubli (purge).
- **Auditabilité** : Historique local des modifications SEO, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouveaux modules, balises ou stratégies SEO.
- **Robustesse** : Gestion des erreurs, fallback sur balises minimales, monitoring de l’indexabilité.
- **SEO** : Titres, descriptions, canonical, robots.txt et sitemap adaptés à chaque page.
- **Documentation** : Docstring JSDoc pour chaque module, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
import { setMetaTags } from './metaManager';

// Définir dynamiquement les balises meta pour une page
setMetaTags({
  title: 'Accueil – Dihya Coding',
  description: 'Plateforme de génération de code moderne, sécurisée et conforme RGPD.',
  canonical: 'https://dihya.app/',
  robots: 'index, follow'
});
```

---

## 📚 Documentation associée

- [metaManager.js](./metaManager.js)
- [sitemapGen.js](./sitemapGen.js)
- [robotsGen.js](./robotsGen.js)
- [tests/](./tests/README.md)
- [Sécurité & RGPD](../docs/security.md)
- [Utils](../utils/README.md)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : SEO moderne, robuste, extensible et conforme RGPD pour chaque génération.**