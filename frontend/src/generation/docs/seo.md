# 🌐 SEO – Dihya Coding

Ce document présente les standards, bonnes pratiques et exigences SEO pour tous les templates et blueprints générés par Dihya Coding.  
Chaque module et template vise : SEO moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse et documentation claire.

---

## 🚀 Objectifs SEO

- **Référencement optimal** : Générer des pages et modules facilement indexables par les moteurs de recherche
- **Accessibilité** : Respecter les standards d’accessibilité (a11y) pour tous les utilisateurs
- **Conformité RGPD** : Respecter la vie privée, anonymiser les logs, obtenir le consentement utilisateur
- **Auditabilité** : Permettre l’audit SEO via logs locaux, audits Lighthouse, rapports exportables
- **Extensibilité** : Permettre l’ajout facile de nouvelles stratégies ou outils SEO

---

## 🛡️ Bonnes pratiques SEO

- **Balises meta** : Génération automatique des balises title, description, keywords, canonical, robots, Open Graph, Twitter Cards
- **Structure sémantique** : Utilisation correcte des balises HTML5 (header, nav, main, footer, article, section, etc.)
- **URLs propres** : Génération de slugs SEO-friendly, URLs courtes et explicites
- **Sitemap & robots.txt** : Génération automatique et mise à jour dynamique
- **Accessibilité (a11y)** : Contraste, navigation clavier, aria-labels, textes alternatifs pour les images
- **Performance** : Optimisation du temps de chargement, lazy loading, images optimisées
- **Logs & auditabilité** : Historique local des audits SEO, logs effaçables (RGPD)
- **Consentement** : Consentement explicite pour toute collecte ou analyse SEO avancée

---

## 📝 Exemples de SEO dans les templates

```js
// Génération d’un slug SEO-friendly
import { generateSlug } from '../../seo/seoUtils';
const slug = generateSlug('Titre de ma page Géniale !');

// Génération d’une meta description optimisée
import { generateMetaDescription } from '../../seo/seoUtils';
const desc = generateMetaDescription('Texte long à résumer pour la meta description...');

// Configuration SEO complète pour une page
import { getSeoConfig } from '../../seo/seoConfig';
const seo = getSeoConfig({
  title: 'Accueil – Dihya Coding',
  description: 'Plateforme moderne, sécurisée et conforme RGPD pour la génération de code.',
  canonical: 'https://dihya.app/',
  keywords: ['génération', 'code', 'sécurité', 'RGPD'],
  lang: 'fr',
  og: { title: 'Dihya Coding', description: 'Génération moderne', image: '/img/og.png' }
});
```

---

## 📚 Documentation associée

- [Compatibilité](./compatibility.md)
- [Sécurité](./security.md)
- [AI Templates](../ai/README.md)
- [DevOps Templates](../devops/README.md)
- [Blockchain Templates](../blockchain/README.md)
- [Branding Templates](../branding/README.md)
- [Cahier des charges Dihya Coding](../../../../../docs/user_guide/README.md)

---

> **Dihya Coding : SEO moderne, sécurisé, accessible et conforme RGPD pour chaque génération.**