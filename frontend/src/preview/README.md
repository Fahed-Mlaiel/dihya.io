# 🖥️ Preview – Dihya Coding

Ce dossier regroupe tous les composants et modules d’aperçu (preview) pour Dihya Coding : affichage sécurisé, design moderne, SEO, conformité RGPD, auditabilité, extensibilité et documentation claire.

---

## 🚀 Objectifs

- Offrir un aperçu sécurisé, moderne et conforme RGPD des projets/modules générés
- Garantir la sécurité, la robustesse, l’auditabilité et la documentation de chaque composant d’aperçu
- Faciliter l’extension, la maintenance et la personnalisation des stratégies de preview

---

## 📁 Structure recommandée

- `PreviewFrame.jsx` : Composant d’aperçu embarqué (iframe sécurisé, logs RGPD)
- `README.md` : Présentation, bonnes pratiques, exemples

---

## 🛡️ Bonnes pratiques

- **Sécurité & RGPD** : Utilisation d’iframe avec sandbox, consentement utilisateur requis, logs anonymisés, droit à l’oubli (purge).
- **Auditabilité** : Historique local des aperçus, logs effaçables, documentation claire.
- **Extensibilité** : Ajout facile de nouveaux types d’aperçus ou de stratégies d’intégration.
- **Robustesse** : Gestion des erreurs d’affichage, fallback, accessibilité.
- **SEO** : Titres, descriptions et balises meta adaptés pour chaque aperçu.
- **Documentation** : Docstring JSDoc pour chaque composant, exemples d’utilisation.

---

## 📝 Exemple d’utilisation

```jsx
import PreviewFrame from './PreviewFrame';

function ProjectPreview() {
  return (
    <PreviewFrame
      src="https://dihya.app/previews/projet-123"
      title="Aperçu du projet"
      height={700}
    />
  );
}
```

---

## 📚 Documentation associée

- [PreviewFrame.jsx](./PreviewFrame.jsx)
- [Sécurité & RGPD](../docs/security.md)
- [Utils](../utils/README.md)
- [Cahier des charges Dihya Coding](../../../docs/user_guide/README.md)

---

> **Dihya Coding : aperçus modernes, sécurisés, robustes, extensibles et conformes RGPD pour chaque génération.**