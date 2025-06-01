# 🧩 Tests unitaires – Dihya Coding

Ce dossier regroupe tous les tests unitaires pour la plateforme **Dihya Coding**. Ces tests garantissent la conformité au cahier des charges : sécurité, robustesse, RGPD, auditabilité, extensibilité, UX, i18n, souveraineté numérique et documentation claire.

---

## 🚀 Objectifs des tests unitaires

- **Valider** chaque fonction, service, composant ou template métier de façon isolée (frontend, backend, API, IA…)
- **Garantir** la sécurité, la conformité RGPD, l’auditabilité, la robustesse et la souveraineté numérique du code métier
- **Tester** l’extensibilité (ajout de nouveaux métiers, modules, plugins, stacks, langues…)
- **Assurer** une expérience développeur moderne, multilingue, accessible et personnalisable

---

## 📁 Structure recommandée

- `*.unit.js` : Un fichier par module, service ou template testé (ex : `generation.unit.js`, `auth.unit.js`, `seo.unit.js`, `template_sport.unit.js`, etc.)
- `README.md` : Présentation, bonnes pratiques, exemples, liens

---

## 🛡️ Bonnes pratiques Dihya Coding

- **Sécurité & RGPD** : Pas de données sensibles dans les tests ou les logs, anonymisation des logs si besoin, droit à l’oubli (purge)
- **Auditabilité** : Chaque test est commenté, logs vérifiés et effaçables, historique des tests, conformité AGPL
- **Extensibilité** : Ajout facile de nouveaux tests unitaires, métiers, modules, stacks, plugins, langues, scénarios
- **Robustesse** : Gestion des erreurs, tests de fallback, vérification des comportements inattendus, résilience
- **Souveraineté** : Tests de fallback open source, backup, décentralisation, logs horodatés
- **SEO & Accessibilité** : Vérification des fonctions liées au SEO, accessibilité, multilingue/dialectes
- **Documentation** : Docstring JSDoc pour chaque test, exemples d’utilisation, liens vers guides

---

## 📝 Exemple d’utilisation

```js
import { sanitize } from '../../services/generationService';

describe('sanitize', () => {
  it('supprime les caractères dangereux', () => {
    expect(sanitize('<script>alert(1)</script>')).not.toContain('<');
    expect(sanitize('texte normal')).toBe('texte normal');
  });
});
```

---

## 📚 Documentation associée

- [generation.unit.js](./generation.unit.js) – Fonctions de génération, sécurité, logs
- [auth.unit.js](./auth.unit.js) – Authentification, rôles, sécurité
- [seo.unit.js](./seo.unit.js) – SEO, accessibilité, balises
- [template_sport.unit.js](./template_sport.unit.js) – Template métier Sport
- [template_tourisme.unit.js](./template_tourisme.unit.js) – Template métier Tourisme
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

## 🏷️ Branding & Souveraineté

- **Nom** : Dihya Coding
- **Thème** : héritage amazigh + modernité tech
- **Slogan** : "De l’idée au code, en toute souveraineté."
- **Licence** : AGPL, open-source, logs horodatés, auditabilité

---

> **Dihya Coding : tests unitaires modernes, robustes, extensibles, souverains et conformes RGPD pour chaque génération.**