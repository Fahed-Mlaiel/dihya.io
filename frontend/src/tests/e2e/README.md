# 🧪 Tests End-to-End (E2E) – Dihya Coding

Ce dossier regroupe tous les tests end-to-end (E2E) pour la plateforme **Dihya Coding**. Ces tests garantissent la conformité au cahier des charges : génération multi-stack, sécurité, RGPD, auditabilité, extensibilité, robustesse, UX, i18n, souveraineté numérique et documentation claire.

---

## 🚀 Objectifs des tests E2E

- **Valider** le fonctionnement global des services et templates métiers générés automatiquement (frontend, backend, API, plugins…)
- **Garantir** la sécurité, la conformité RGPD, l’auditabilité, la robustesse et la souveraineté numérique
- **Tester** l’extensibilité (ajout de nouveaux métiers, plugins, stacks, langues…)
- **Assurer** une expérience utilisateur moderne, multilingue, accessible et personnalisable

---

## 📁 Structure recommandée

- `generation.e2e.js` : Génération de code, markdown, images, logs, RGPD, plugins
- `auth.e2e.js` : Authentification (inscription, login, logout, rôles, logs, RGPD)
- `seo.e2e.js` : SEO (balises, accessibilité, indexabilité, logs, RGPD)
- `ecommerce.e2e.js` : E-commerce (produits, panier, paiement, logs, RGPD)
- `education.e2e.js` : Éducation (cours, modules, quiz, logs, RGPD)
- `README.md` : Présentation, bonnes pratiques, exemples, liens

---

## 🛡️ Bonnes pratiques Dihya Coding

- **Sécurité & RGPD** : Consentement utilisateur simulé, anonymisation des logs, droit à l’oubli (purge), pas de données sensibles dans les tests ou les logs
- **Auditabilité** : Chaque test est commenté, logs vérifiés et effaçables, historique des tests, conformité AGPL
- **Extensibilité** : Ajout facile de nouveaux tests, métiers, stacks, plugins, langues, scénarios
- **Robustesse** : Gestion des erreurs, tests de fallback, vérification des comportements inattendus, résilience
- **Souveraineté** : Tests de fallback open source, backup, décentralisation, logs horodatés
- **SEO & Accessibilité** : Vérification des balises, accessibilité, indexabilité, multilingue/dialectes
- **Documentation** : Docstring JSDoc pour chaque test, exemples d’utilisation, liens vers guides

---

## 📝 Exemple d’utilisation

```js
import { generate } from '../../services/generationService';

describe('Génération – E2E', () => {
  it('génère du code source sécurisé', () => {
    const result = generate({ type: 'code', options: { language: 'js', content: 'let x = 1;' } });
    expect(result.success).toBe(true);
  });
});
```

---

## 📚 Documentation associée

- [generation.e2e.js](./generation.e2e.js) – Génération multi-stack, logs, RGPD, plugins
- [auth.e2e.js](./auth.e2e.js) – Authentification, rôles, sécurité, logs
- [seo.e2e.js](./seo.e2e.js) – SEO, accessibilité, indexabilité
- [ecommerce.e2e.js](./ecommerce.e2e.js) – E-commerce, paiement, logs
- [education.e2e.js](./education.e2e.js) – Éducation, quiz, logs
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

## 🏷️ Branding & Souveraineté

- **Nom** : Dihya Coding
- **Thème** : héritage amazigh + modernité tech
- **Slogan** : "De l’idée au code, en toute souveraineté."
- **Licence** : AGPL, open-source, logs horodatés, auditabilité

---

> **Dihya Coding : tests E2E modernes, robustes, extensibles, souverains et conformes RGPD pour chaque génération.**