# Composant recherche

**Composant métier Recherche pour Dihya Coding – Génération de solutions numériques pour la recherche scientifique, académique, R&D, gestion de projets, publications, laboratoires, données, collaborations et innovation ouverte.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés à la recherche (scientifique, académique, R&D, laboratoires, gestion de projets, publications, données, collaborations, innovation) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables, inspiration amazigh)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la création de projets, protocoles, rapports, publications
- **Templates métiers recherche** (laboratoire, projet, publication, base de données, veille, open science)
- **Gestion des projets & protocoles** (création, édition, suivi, historique, partage)
- **Gestion des utilisateurs & rôles** (chercheur, doctorant, technicien, admin, invité)
- **Gestion des publications & rapports** (rédaction, édition, dépôt, DOI, versioning)
- **Gestion des données & résultats** (import/export, anonymisation, visualisation, conformité RGPD)
- **Collaboration & partage** (groupes, commentaires, notifications, co-édition)
- **Veille scientifique & notifications** (alertes, nouveautés, bibliographie, citations)
- **Intégration d’outils IA** (analyse, résumé, traduction, détection plagiat)
- **SEO automatique** (balises, sitemap, microdata schema.org/ScholarlyArticle, Organization)
- **Export/Import** (CSV, JSON, YAML, PDF, partage en un clic)
- **Marketplace de plugins** (visualisation, bibliographie, IA, open data)
- **Accessibilité renforcée** (contrastes, navigation clavier, ARIA)
- **Sécurité** (validation des fichiers, CORS, rate limiting, logs auditables, chiffrement)
- **Conformité RGPD** (suppression/export/anonymisation des données sur demande)

---

## 📦 Structure recommandée
```markdown
# Composant recherche

**Composant métier Recherche pour Dihya Coding – Génération de solutions numériques pour la recherche scientifique, académique, R&D, gestion de projets, publications, laboratoires, données, collaborations et innovation ouverte.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés à la recherche (scientifique, académique, R&D, laboratoires, gestion de projets, publications, données, collaborations, innovation) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables, inspiration amazigh)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la création de projets, protocoles, rapports, publications
- **Templates métiers recherche** (laboratoire, projet, publication, base de données, veille, open science)
- **Gestion des projets & protocoles** (création, édition, suivi, historique, partage)
- **Gestion des utilisateurs & rôles** (chercheur, doctorant, technicien, admin, invité)
- **Gestion des publications & rapports** (rédaction, édition, dépôt, DOI, versioning)
- **Gestion des données & résultats** (import/export, anonymisation, visualisation, conformité RGPD)
- **Collaboration & partage** (groupes, commentaires, notifications, co-édition)
- **Veille scientifique & notifications** (alertes, nouveautés, bibliographie, citations)
- **Intégration d’outils IA** (analyse, résumé, traduction, détection plagiat)
- **SEO automatique** (balises, sitemap, microdata schema.org/ScholarlyArticle, Organization)
- **Export/Import** (CSV, JSON, YAML, PDF, partage en un clic)
- **Marketplace de plugins** (visualisation, bibliographie, IA, open data)
- **Accessibilité renforcée** (contrastes, navigation clavier, ARIA)
- **Sécurité** (validation des fichiers, CORS, rate limiting, logs auditables, chiffrement)
- **Conformité RGPD** (suppression/export/anonymisation des données sur demande)

---

## 📦 Structure recommandée

```
RechercheCard/
  RechercheCard.jsx|vue|svelte   # Composant principal (React/Vue/Svelte)
  RechercheCard.module.css       # Styles dédiés (ou Tailwind)
  RechercheCard.test.js          # Tests unitaires et d’intégration
  assets/                        # Icônes, images, illustrations recherche
  README.md                      # Ce fichier
```

---

## 🛠️ Exemple d’utilisation (React)

```jsx
import RechercheCard from './RechercheCard';

<RechercheCard
  labName="Dihya Lab"
  projects={[
    { title: "Projet IA Amazigh", status: "En cours", lastUpdate: "2025-06-01" },
    { title: "Étude biodiversité", status: "Terminé", lastUpdate: "2025-05-20" }
  ]}
  publications={[
    { title: "Article sur l’IA", date: "2025-05-15", doi: "10.1234/dihya.ia2025" }
  ]}
  onAddProject={() => {/* ... */}}
  onPublishArticle={() => {/* ... */}}
  onDownloadReport={() => {/* ... */}}
/>
```

---

## 🔒 Sécurité & Bonnes pratiques

- **Validation stricte** des fichiers uploadés (taille, type, virus)
- **Chiffrement fort** des données sensibles (projets, données, publications)
- **Aucune donnée personnelle** sans consentement explicite
- **Logs auditables** et suppression/export sur demande (RGPD)
- **Pas de dépendance critique à une API propriétaire**
- **Tests unitaires et d’intégration** obligatoires

---

## 🌐 Accessibilité & SEO

- Contraste et navigation clavier testés (WCAG)
- Texte alternatif pour chaque média
- Microdata schema.org/ScholarlyArticle, Organization pour le SEO

---

## 📚 Documentation

- [Templates métiers recherche](../../../docs/contribution/templates/README.md)
- [Charte graphique & branding](../../../branding/README.md)
- [Guide design général](../../../design/README.md)

---

## 🤝 Contribution

- Proposer des variantes (laboratoire, projet, publication, open science…)
- Respecter la charte graphique et la conformité RGPD
- Documenter chaque ajout (usage, sécurité, accessibilité)

---

© Dihya Coding – 2025
```