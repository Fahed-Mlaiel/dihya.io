# 🤖 AI – Dihya Coding

Ce dossier regroupe tous les modules liés à l’intelligence artificielle pour la génération, l’assistance et la gestion des quotas dans Dihya Coding.  
Chaque module garantit : design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Centraliser les fonctions IA : génération, fallback, assistant, gestion des quotas
- Garantir la sécurité, la conformité RGPD et l’auditabilité de chaque interaction IA
- Faciliter l’extension, la maintenance et la documentation des services IA

---

## 📁 Structure recommandée

- `assistant.js` : Assistant IA conversationnel (génération, aide contextuelle)
- `fallbackGeneric.js` : Fallback générique en cas d’indisponibilité du service IA principal
- `fallbackLlama.js` : Fallback spécifique pour le moteur Llama
- `fallbackMistral.js` : Fallback spécifique pour le moteur Mistral
- `fallbackMixtral.js` : Fallback spécifique pour le moteur Mixtral
- `quotaDetector.js` : Détection et gestion des quotas IA (alerte, blocage)
- `quotaManager.js` : Gestion centralisée des quotas IA (consommation, réinitialisation, logs)

---

## 🛡️ Bonnes pratiques

- **Sécurité** : Validation stricte des entrées, anonymisation des prompts et logs, gestion sécurisée des tokens.
- **RGPD** : Consentement utilisateur requis, logs locaux anonymisés, droit à l’oubli (fonctions de purge).
- **Auditabilité** : Historique des actions IA, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouveaux moteurs IA ou fallback, API claire et typée.
- **Documentation** : Docstring JSDoc pour chaque fonction, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
import { getAssistantReply } from './assistant';
import { fallbackGeneric } from './fallbackGeneric';

async function askAssistant(messages) {
  try {
    const result = await getAssistantReply({ messages, lang: 'fr' });
    // ...traitement du résultat
  } catch (e) {
    // Utilisation du fallback en cas d’erreur IA
    const fallback = await fallbackGeneric({ prompt: messages[messages.length - 1].content });
    // ...traitement du fallback
  }
}
```

---

## 📚 Documentation associée

- [Features](../../features/README.md)
- [Contexts](../../contexts/README.md)
- [Cahier des charges Dihya Coding](../../../../docs/user_guide/README.md)

---

> **Dihya Coding : des modules IA modernes, sûrs, souverains et documentés.**