# Composant ressources_humaines

**Composant métier Ressources Humaines pour Dihya Coding – Génération de solutions numériques pour la gestion RH, recrutement, onboarding, gestion des talents, paie, formation, évaluations, conformité et expérience collaborateur.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés aux ressources humaines (recrutement, gestion des talents, paie, formation, évaluations, conformité, expérience collaborateur) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables, inspiration amazigh)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la création de fiches de poste, annonces, évaluations, feedbacks
- **Templates métiers RH** (recrutement, gestion du personnel, paie, formation, onboarding, évaluation)
- **Gestion des collaborateurs** (ajout, édition, historique, organigramme, mobilité)
- **Gestion des utilisateurs & rôles** (RH, manager, collaborateur, admin)
- **Gestion du recrutement** (annonces, candidatures, entretiens, scoring IA, onboarding)
- **Gestion de la paie & contrats** (bulletins, contrats, absences, congés, alertes)
- **Gestion de la formation** (catalogue, inscriptions, suivi, évaluations)
- **Gestion des évaluations & feedbacks** (objectifs, entretiens, 360°, reporting)
- **Notifications & mailing** (alertes, rappels, onboarding, anniversaires)
- **Export/Import** (CSV, JSON, YAML, PDF, partage en un clic)
- **SEO automatique** (balises, sitemap, microdata schema.org/Organization, EmployeeRole)
- **Marketplace de plugins** (paie, formation, analytics, bien-être, IA)
- **Accessibilité renforcée** (contrastes, navigation clavier, ARIA)
- **Sécurité** (validation des fichiers, chiffrement, CORS, rate limiting, logs auditables)
- **Conformité RGPD** (suppression/export/anonymisation des données sur demande)

---

## 📦 Structure recommandée
```markdown
# Composant ressources_humaines

**Composant métier Ressources Humaines pour Dihya Coding – Génération de solutions numériques pour la gestion RH, recrutement, onboarding, gestion des talents, paie, formation, évaluations, conformité et expérience collaborateur.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés aux ressources humaines (recrutement, gestion des talents, paie, formation, évaluations, conformité, expérience collaborateur) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables, inspiration amazigh)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la création de fiches de poste, annonces, évaluations, feedbacks
- **Templates métiers RH** (recrutement, gestion du personnel, paie, formation, onboarding, évaluation)
- **Gestion des collaborateurs** (ajout, édition, historique, organigramme, mobilité)
- **Gestion des utilisateurs & rôles** (RH, manager, collaborateur, admin)
- **Gestion du recrutement** (annonces, candidatures, entretiens, scoring IA, onboarding)
- **Gestion de la paie & contrats** (bulletins, contrats, absences, congés, alertes)
- **Gestion de la formation** (catalogue, inscriptions, suivi, évaluations)
- **Gestion des évaluations & feedbacks** (objectifs, entretiens, 360°, reporting)
- **Notifications & mailing** (alertes, rappels, onboarding, anniversaires)
- **Export/Import** (CSV, JSON, YAML, PDF, partage en un clic)
- **SEO automatique** (balises, sitemap, microdata schema.org/Organization, EmployeeRole)
- **Marketplace de plugins** (paie, formation, analytics, bien-être, IA)
- **Accessibilité renforcée** (contrastes, navigation clavier, ARIA)
- **Sécurité** (validation des fichiers, chiffrement, CORS, rate limiting, logs auditables)
- **Conformité RGPD** (suppression/export/anonymisation des données sur demande)

---

## 📦 Structure recommandée

```
Ressources_humainesCard/
  Ressources_humainesCard.jsx|vue|svelte   # Composant principal (React/Vue/Svelte)
  Ressources_humainesCard.module.css       # Styles dédiés (ou Tailwind)
  Ressources_humainesCard.test.js          # Tests unitaires et d’intégration
  assets/                                  # Icônes, images, illustrations RH
  README.md                                # Ce fichier
```

---

## 🛠️ Exemple d’utilisation (React)

```jsx
import RessourcesHumainesCard from './Ressources_humainesCard';

<RessourcesHumainesCard
  companyName="Dihya RH"
  employees={[
    { name: "A. Amellal", role: "Développeur", status: "Actif", lastEvaluation: "2025-05-15" },
    { name: "N. Dihya", role: "RH", status: "En congé", lastEvaluation: "2025-04-10" }
  ]}
  recruitments={[
    { position: "Data Scientist", status: "Ouvert", applications: 12 }
  ]}
  onAddEmployee={() => {/* ... */}}
  onStartRecruitment={() => {/* ... */}}
  onDownloadReport={() => {/* ... */}}
/>
```

---

## 🔒 Sécurité & Bonnes pratiques

- **Chiffrement fort** des données sensibles (paie, dossiers RH)
- **Validation stricte** des fichiers uploadés (taille, type, virus)
- **Aucune donnée personnelle** sans consentement explicite
- **Logs auditables** et suppression/export sur demande (RGPD)
- **Pas de dépendance critique à une API propriétaire**
- **Tests unitaires et d’intégration** obligatoires

---

## 🌐 Accessibilité & SEO

- Contraste et navigation clavier testés (WCAG)
- Texte alternatif pour chaque média
- Microdata schema.org/Organization, EmployeeRole pour le SEO

---

## 📚 Documentation

- [Templates métiers RH](../../../docs/contribution/templates/README.md)
- [Charte graphique & branding](../../../branding/README.md)
- [Guide design général](../../../design/README.md)

---

## 🤝 Contribution

- Proposer des variantes (recrutement, paie, formation, bien-être…)
- Respecter la charte graphique et la conformité RGPD
- Documenter chaque ajout (usage, sécurité, accessibilité)

---

© Dihya Coding – 2025
```