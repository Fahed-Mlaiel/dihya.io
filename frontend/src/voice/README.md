# 🗣️ Voice – Dihya Coding

Ce dossier regroupe tous les modules et utilitaires liés à la voix pour Dihya Coding : reconnaissance vocale, synthèse vocale, accessibilité, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Offrir des fonctionnalités de reconnaissance et synthèse vocale modernes et accessibles
- Garantir la sécurité, la conformité RGPD, l’auditabilité et la robustesse des traitements vocaux
- Permettre l’extension facile à de nouveaux cas d’usage ou modules vocaux

---

## 📁 Structure recommandée

- `recognition.js` : Reconnaissance vocale (speech-to-text), logs, RGPD
- `synthesis.js` : Synthèse vocale (text-to-speech), logs, RGPD
- `voiceUtils.js` : Utilitaires voix (validation, sécurité, anonymisation)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité & RGPD** : Consentement utilisateur requis, anonymisation des logs, droit à l’oubli (purge), pas de stockage de voix brute sans consentement explicite
- **Auditabilité** : Chaque fonction est commentée, logs vérifiés et effaçables, historique des actions vocales
- **Extensibilité** : Ajout facile de nouveaux modules ou fonctionnalités vocales
- **Robustesse** : Gestion des erreurs, fallback, validation stricte des entrées et sorties
- **Accessibilité** : Respect des standards WAI-ARIA, prise en charge multi-langue, feedback utilisateur
- **Documentation** : Docstring JSDoc pour chaque fonction, exemples d’utilisation

---

## 📝 Exemple d’utilisation

```js
import { startRecognition } from './recognition';
import { speak } from './synthesis';

startRecognition({
  lang: 'fr-FR',
  onResult: (text) => speak(`Vous avez dit : ${text}`)
});
```

---

## 📚 Documentation associée

- [recognition.js](./recognition.js)
- [synthesis.js](./synthesis.js)
- [voiceUtils.js](./voiceUtils.js)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : modules voix modernes, robustes, extensibles et conformes RGPD pour chaque génération.**