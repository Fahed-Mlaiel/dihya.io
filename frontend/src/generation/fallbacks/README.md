# 🛡️ Fallbacks – Dihya Coding

Ce dossier regroupe toutes les fonctions de secours (fallbacks) pour la génération IA dans Dihya Coding : gestion des indisponibilités, alertes quotas, robustesse et continuité de service.  
Chaque fallback garantit : design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Assurer la continuité de service IA même en cas d’indisponibilité d’un moteur (Llama, Mistral, Mixtral…)
- Gérer les alertes et blocages liés aux quotas IA
- Centraliser la logique de fallback pour faciliter l’extension et la maintenance

---

## 📁 Structure recommandée

- `fallbackLlama.js` : Fallback spécifique pour le moteur Llama
- `fallbackMistral.js` : Fallback spécifique pour le moteur Mistral
- `fallbackMixtral.js` : Fallback spécifique pour le moteur Mixtral
- `quotaDetector.js` : Détection et gestion des quotas IA (alerte, blocage, logs)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité** : Validation stricte des prompts, anonymisation des logs, gestion sécurisée des notifications.
- **RGPD** : Consentement utilisateur requis, logs locaux anonymisés, droit à l’oubli (fonctions de purge).
- **Auditabilité** : Historique local des fallback, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouveaux moteurs ou stratégies de fallback.
- **Documentation** : Docstring JSDoc pour chaque fonction, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
import { fallbackLlamaGenerate } from './fallbackLlama';
import { checkQuota, handleQuotaAlert } from './quotaDetector';

async function safeIaCall(prompt, userId) {
  const quota = await checkQuota({ userId });
  handleQuotaAlert(quota);
  if (quota.quotaExceeded) {
    return { error: 'Quota IA dépassé.' };
  }
  try {
    // ...appel IA principal
  } catch {
    // Fallback Llama en cas d’indisponibilité
    return await fallbackLlamaGenerate({ prompt });
  }
}
```

---

## 📚 Documentation associée

- [AI](../ai/README.md)
- [Blueprints](../blueprints/README.md)
- [Sécurité & RGPD](../docs/security.md)
- [Cahier des charges Dihya Coding](../../../../docs/user_guide/README.md)

---

> **Dihya Coding : robustesse, sécurité, auditabilité et conformité RGPD même en cas d’indisponibilité IA.**