# 🧠 Contexts – Dihya Coding

Ce dossier regroupe tous les contextes React utilisés pour la gestion globale de l’état dans l’interface Dihya Coding.  
Chaque contexte garantit : design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs

- Centraliser la gestion des états globaux (authentification, langue, thème, etc.)
- Garantir la cohérence, la sécurité et la conformité RGPD des données partagées
- Faciliter l’extensibilité, la maintenance et l’auditabilité de l’application

---

## 📁 Structure recommandée

- `AuthContext.js` : Contexte d’authentification (sécurité, anonymisation, logs RGPD)
- `LanguageContext.js` : Contexte de gestion de la langue (SEO, accessibilité, logs)
- `ThemeProvider.jsx` : Fournisseur de thème graphique (design, logs, conformité)
- `...` : Ajouter d’autres contextes selon les besoins métier

---

## 🛡️ Bonnes pratiques

- **Sécurité** : Ne jamais stocker de secrets, tokens ou données sensibles non anonymisées dans le contexte.
- **RGPD** : Respect du consentement utilisateur, anonymisation des logs, droit à l’oubli (fonctions de purge).
- **Auditabilité** : Historique des modifications via Git, logs locaux effaçables.
- **Extensibilité** : Ajouter facilement de nouveaux contextes ou propriétés.
- **Documentation** : Docstring JSDoc pour chaque contexte, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```js
import { AuthProvider, useAuth } from './AuthContext';
import { LanguageProvider, useLanguage } from './LanguageContext';

function App() {
  return (
    <AuthProvider>
      <LanguageProvider>
        {/* ... */}
      </LanguageProvider>
    </AuthProvider>
  );
}
```

---

## 📚 Documentation associée

- [Composants](../components/README.md)
- [Thèmes graphiques](../branding/themes/README.md)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : des contextes modernes, sûrs, souverains et documentés.**