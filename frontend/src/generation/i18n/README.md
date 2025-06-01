# i18n
# 🌍 i18n – Dihya Coding

Ce dossier regroupe tous les modules de gestion de l’internationalisation (i18n), de la traduction automatique et du support des dialectes pour Dihya Coding.  
Chaque module garantit : design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Centraliser la gestion des traductions, détections de langue et dialectes pour tous les modules générés
- Garantir la sécurité, la conformité RGPD et l’auditabilité de chaque opération de traduction
- Faciliter l’extension, la maintenance et la documentation des fonctionnalités i18n

---

## 📁 Structure recommandée

- `autoTranslate.js` : Traduction automatique (détection de langue, traduction, logs, audit)
- `dialectSupport.js` : Gestion avancée des dialectes et variantes linguistiques
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité** : Validation stricte des textes, anonymisation des logs, gestion sécurisée des tokens.
- **RGPD** : Consentement utilisateur requis, logs locaux anonymisés, droit à l’oubli (fonctions de purge).
- **Auditabilité** : Historique local des traductions et détections, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouvelles langues, dialectes ou services de traduction.
- **Documentation** : Docstring JSDoc pour chaque fonction, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
import { autoTranslate } from './autoTranslate';
import { translateToDialect } from './dialectSupport';

async function traduireTexte() {
  const res = await autoTranslate({ text: 'Bonjour', targetLang: 'en' });
  const dialectRes = await translateToDialect({ text: 'Bonjour', targetDialect: 'fr-CA' });
  // ...traitement, audit, logs, etc.
}
```

---

## 📚 Documentation associée

- [Blueprints](../blueprints/README.md)
- [Sécurité & RGPD](../docs/security.md)
- [Cahier des charges Dihya Coding](../../../../docs/user_guide/README.md)

---

> **Dihya Coding : internationalisation moderne, sécurisée, extensible et conforme RGPD pour chaque génération.**