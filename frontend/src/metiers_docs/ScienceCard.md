# Composant science

**Composant métier Science pour Dihya Coding – Génération de solutions numériques pour la recherche scientifique, laboratoires, gestion d’expériences, protocoles, données, publications, collaborations et innovation ouverte.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés à la science (laboratoires, expériences, protocoles, gestion de données, publications, collaborations, innovation) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables, inspiration amazigh)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la création d’expériences, protocoles, rapports, publications
- **Templates métiers science** (laboratoire, projet, expérience, base de données, open science)
- **Gestion des expériences & protocoles** (création, édition, suivi, historique, partage)
- **Gestion des utilisateurs & rôles** (chercheur, technicien, doctorant, admin, invité)
- **Gestion des publications & rapports** (rédaction, édition, dépôt, DOI, versioning)
- **Gestion des données scientifiques** (import/export, anonymisation, visualisation, conformité RGPD)
- **Collaboration & partage** (groupes, commentaires, notifications, co-édition)
- **Veille scientifique & notifications** (alertes, nouveautés, bibliographie, citations)
- **Intégration d’outils IA** (analyse, résumé, traduction, détection plagiat)
- **SEO automatique** (balises, sitemap, microdata schema.org/ResearchProject, Organization)
- **Export/Import** (CSV, JSON, YAML, PDF, partage en un clic)
- **Marketplace de plugins** (visualisation, bibliographie, IA, open data)
- **Accessibilité renforcée** (contrastes, navigation clavier, ARIA)
- **Sécurité** (validation des fichiers, CORS, rate limiting, logs auditables, chiffrement)
- **Conformité RGPD** (suppression/export/anonymisation des données sur demande)

---

## 📦 Structure recommandée
```markdown
# Composant science

**Composant métier Science pour Dihya Coding – Génération de solutions numériques pour la recherche scientifique, laboratoires, gestion d’expériences, protocoles, données, publications, collaborations et innovation ouverte.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés à la science (laboratoires, expériences, protocoles, gestion de données, publications, collaborations, innovation) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables, inspiration amazigh)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la création d’expériences, protocoles, rapports, publications
- **Templates métiers science** (laboratoire, projet, expérience, base de données, open science)
- **Gestion des expériences & protocoles** (création, édition, suivi, historique, partage)
- **Gestion des utilisateurs & rôles** (chercheur, technicien, doctorant, admin, invité)
- **Gestion des publications & rapports** (rédaction, édition, dépôt, DOI, versioning)
- **Gestion des données scientifiques** (import/export, anonymisation, visualisation, conformité RGPD)
- **Collaboration & partage** (groupes, commentaires, notifications, co-édition)
- **Veille scientifique & notifications** (alertes, nouveautés, bibliographie, citations)
- **Intégration d’outils IA** (analyse, résumé, traduction, détection plagiat)
- **SEO automatique** (balises, sitemap, microdata schema.org/ResearchProject, Organization)
- **Export/Import** (CSV, JSON, YAML, PDF, partage en un clic)
- **Marketplace de plugins** (visualisation, bibliographie, IA, open data)
- **Accessibilité renforcée** (contrastes, navigation clavier, ARIA)
- **Sécurité** (validation des fichiers, CORS, rate limiting, logs auditables, chiffrement)
- **Conformité RGPD** (suppression/export/anonymisation des données sur demande)

---

## 📦 Structure recommandée

```
ScienceCard/
  ScienceCard.jsx|vue|svelte   # Composant principal (React/Vue/Svelte)
  ScienceCard.module.css       # Styles dédiés (ou Tailwind)
  ScienceCard.test.js          # Tests unitaires et d’intégration
  assets/                      # Icônes, images, illustrations science
  README.md                    # Ce fichier
```

---

## 🛠️ Exemple d’utilisation (React)

```jsx
import ScienceCard from './ScienceCard';

<ScienceCard
  labName="Dihya Science Lab"
  experiments={[
    { title: "Expérience ADN", status: "En cours", lastUpdate: "2025-06-01" },
    { title: "Analyse spectroscopique", status: "Terminé", lastUpdate: "2025-05-20" }
  ]}
  publications={[
    { title: "Découverte génétique", date: "2025-05-15", doi: "10.1234/dihya.science2025" }
  ]}
  onAddExperiment={() => {/* ... */}}
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
- Microdata schema.org/ResearchProject, Organization pour le SEO

---

## 📚 Documentation

- [Templates métiers science](../../../docs/contribution/templates/README.md)
- [Charte graphique & branding](../../../branding/README.md)
- [Guide design général](../../../design/README.md)

---

## 🤝 Contribution

- Proposer des variantes (laboratoire, projet, open science, base de données…)
- Respecter la charte graphique et la conformité RGPD
- Documenter chaque ajout (usage, sécurité, accessibilité)

---

© Dihya Coding – 2025
```