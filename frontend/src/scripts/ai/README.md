# 🤖 IA – Dihya Coding

Ce dossier regroupe tous les modules d’IA utilisés dans Dihya Coding : fallback GPT, Llama, Mixtral, détection de quota, sécurité, conformité RGPD, auditabilité, extensibilité et documentation claire.

---

## 🚀 Objectifs

- Fournir des intégrations IA robustes, sécurisées, modernes et conformes RGPD pour la génération, l’assistance et l’automatisation
- Gérer les indisponibilités, les quotas, la sécurité et la traçabilité des appels IA
- Faciliter l’extension, la maintenance et la personnalisation des stratégies IA

---

## 📁 Structure recommandée

- `gpt_fallback.js` : Fallback IA GPT (gestion des indisponibilités, logs, RGPD)
- `llama_fallback.js` : Fallback IA Llama (gestion des indisponibilités, logs, RGPD)
- `mixtral_fallback.js` : Fallback IA Mixtral (gestion des indisponibilités, logs, RGPD)
- `quotaDetector.js` : Détection et gestion des quotas IA (limites d’usage, logs)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité & RGPD** : Consentement utilisateur requis, logs anonymisés, droit à l’oubli (purge), pas de données personnelles dans les prompts/réponses.
- **Auditabilité** : Historique local des appels et quotas, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouveaux modèles IA ou stratégies de fallback.
- **Robustesse** : Gestion des erreurs, fallback local, monitoring des quotas.
- **Documentation** : Docstring JSDoc pour chaque module, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
import { gptFallback } from './gpt_fallback';
import { llamaFallback } from './llama_fallback';
import { mixtralFallback } from './mixtral_fallback';
import { checkQuota, incrementQuota } from './quotaDetector';

// Vérification du quota avant appel IA
const { allowed } = checkQuota();
if (allowed) {
  const result = await gptFallback({ prompt: 'Explique RGPD.' });
  // Utiliser result.response
  incrementQuota();
}
```

---

## 📚 Documentation associée

- [gpt_fallback.js](./gpt_fallback.js)
- [llama_fallback.js](./llama_fallback.js)
- [mixtral_fallback.js](./mixtral_fallback.js)
- [quotaDetector.js](./quotaDetector.js)
- [Sécurité & RGPD](../../docs/security.md)
- [Utils](../../utils/README.md)
- [Cahier des charges Dihya Coding](../../../../docs/user_guide/README.md)

---

> **Dihya Coding : IA moderne, sécurisée, robuste, extensible et conforme RGPD pour chaque génération.**