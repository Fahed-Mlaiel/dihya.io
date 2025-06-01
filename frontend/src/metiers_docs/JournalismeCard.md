# Composant journalisme

**Composant métier Journalisme pour Dihya Coding – Génération de solutions numériques pour médias, rédaction, publication, gestion de contenus, enquêtes, fact-checking, diffusion multicanal et souveraineté éditoriale.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés au journalisme (rédaction, publication, gestion de contenus, enquêtes, fact-checking, diffusion multicanal, médias indépendants) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables, inspiration amazigh)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la rédaction d’articles, enquêtes, interviews
- **Templates métiers journalisme** (média en ligne, blog, magazine, fact-checking, podcast)
- **Gestion des articles & contenus** (création, édition, publication, archivage, tags, médias)
- **Gestion des utilisateurs & rôles** (rédacteur, éditeur, admin, invité)
- **Workflow éditorial** (soumission, validation, publication, historique, commentaires internes)
- **Fact-checking & vérification** (outils IA, sources, versioning, logs)
- **Diffusion multicanal** (web, newsletter, réseaux sociaux, RSS, podcast)
- **SEO automatique** (balises, sitemap, microdata schema.org/NewsArticle, Organization)
- **Notifications & mailing** (alertes, newsletters, commentaires, modération)
- **Export/Import** (JSON, YAML, PDF, partage en un clic)
- **Marketplace de plugins** (analytics, CMS, traduction, accessibilité, anti-plagiat)
- **Accessibilité renforcée** (contrastes, navigation clavier, ARIA)
- **Sécurité** (validation des fichiers, CORS, rate limiting, logs auditables, chiffrement)
- **Conformité RGPD** (suppression/export/anonymisation des données sur demande)

---

## 📦 Structure recommandée
```markdown
# Composant journalisme

**Composant métier Journalisme pour Dihya Coding – Génération de solutions numériques pour médias, rédaction, publication, gestion de contenus, enquêtes, fact-checking, diffusion multicanal et souveraineté éditoriale.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés au journalisme (rédaction, publication, gestion de contenus, enquêtes, fact-checking, diffusion multicanal, médias indépendants) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables, inspiration amazigh)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la rédaction d’articles, enquêtes, interviews
- **Templates métiers journalisme** (média en ligne, blog, magazine, fact-checking, podcast)
- **Gestion des articles & contenus** (création, édition, publication, archivage, tags, médias)
- **Gestion des utilisateurs & rôles** (rédacteur, éditeur, admin, invité)
- **Workflow éditorial** (soumission, validation, publication, historique, commentaires internes)
- **Fact-checking & vérification** (outils IA, sources, versioning, logs)
- **Diffusion multicanal** (web, newsletter, réseaux sociaux, RSS, podcast)
- **SEO automatique** (balises, sitemap, microdata schema.org/NewsArticle, Organization)
- **Notifications & mailing** (alertes, newsletters, commentaires, modération)
- **Export/Import** (JSON, YAML, PDF, partage en un clic)
- **Marketplace de plugins** (analytics, CMS, traduction, accessibilité, anti-plagiat)
- **Accessibilité renforcée** (contrastes, navigation clavier, ARIA)
- **Sécurité** (validation des fichiers, CORS, rate limiting, logs auditables, chiffrement)
- **Conformité RGPD** (suppression/export/anonymisation des données sur demande)

---

## 📦 Structure recommandée

```
JournalismeCard/
  JournalismeCard.jsx|vue|svelte   # Composant principal (React/Vue/Svelte)
  JournalismeCard.module.css       # Styles dédiés (ou Tailwind)
  JournalismeCard.test.js          # Tests unitaires et d’intégration
  assets/                          # Icônes, images, illustrations journalisme
  README.md                        # Ce fichier
```

---

## 🛠️ Exemple d’utilisation (React)

```jsx
import JournalismeCard from './JournalismeCard';

<JournalismeCard
  newsroom="Dihya News"
  articles={[
    { title: "Lancement de Dihya Coding", author: "A. Amellal", date: "2025-05-15", status: "Publié" },
    { title: "Interview : Femmes et Tech", author: "N. Dihya", date: "2025-05-10", status: "Brouillon" }
  ]}
  onPublishArticle={article => {/* ... */}}
  onFactCheck={article => {/* ... */}}
  onDownloadReport={() => {/* ... */}}
/>
```

---

## 🔒 Sécurité & Bonnes pratiques

- **Validation stricte** des fichiers uploadés (taille, type, virus)
- **Chiffrement fort** des données sensibles (sources, brouillons)
- **Aucune donnée personnelle** sans consentement explicite
- **Logs auditables** et suppression/export sur demande (RGPD)
- **Pas de dépendance critique à une API propriétaire**
- **Tests unitaires et d’intégration** obligatoires

---

## 🌐 Accessibilité & SEO

- Contraste et navigation clavier testés (WCAG)
- Texte alternatif pour chaque média
- Microdata schema.org/NewsArticle, Organization pour le SEO

---

## 📚 Documentation

- [Templates métiers journalisme](../../../docs/contribution/templates/README.md)
- [Charte graphique & branding](../../../branding/README.md)
- [Guide design général](../../../design/README.md)

---

## 🤝 Contribution

- Proposer des variantes (média, blog, magazine, fact-checking…)
- Respecter la charte graphique et la conformité RGPD
- Documenter chaque ajout (usage, sécurité, accessibilité)

---

© Dihya Coding – 2025
```