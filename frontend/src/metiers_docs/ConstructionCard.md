# Composant ConstructionCard

**Composant métier Construction pour Dihya Coding – Génération de solutions numériques pour la construction, la gestion de projets, le suivi de chantiers, la conformité, la sécurité et la mobilité.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés au secteur de la construction (gestion de chantiers, suivi d’avancement, ressources humaines et matérielles, sécurité, conformité, mobilité) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la description des projets, tâches, incidents
- **Templates métiers construction** (gestion de chantier, suivi d’avancement, planning, gestion des équipes, sécurité)
- **Gestion des projets et chantiers** (fiche projet, avancement, photos, documents, plans)
- **Gestion des ressources** (matériel, main d’œuvre, sous-traitants, fournisseurs)
- **Gestion des utilisateurs & rôles** (chef de projet, chef de chantier, ouvrier, conducteur de travaux, admin)
- **Notifications & mailing** (alertes sécurité, rappels, incidents, planning)
- **SEO automatique** (balises, sitemap, microdata schema.org/ConstructionCompany)
- **Export/Import** (JSON, YAML, PDF, partage en un clic)
- **Marketplace de plugins** (planning, météo, conformité, analytics)
- **Accessibilité renforcée** (contrastes, navigation clavier, ARIA)
- **Sécurité** (validation des fichiers, CORS, rate limiting, logs auditables)
- **Conformité RGPD** (suppression/export/anonymisation des données sur demande)

---

## 📦 Structure recommandée
```markdown
# Composant ConstructionCard

**Composant métier Construction pour Dihya Coding – Génération de solutions numériques pour la construction, la gestion de projets, le suivi de chantiers, la conformité, la sécurité et la mobilité.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés au secteur de la construction (gestion de chantiers, suivi d’avancement, ressources humaines et matérielles, sécurité, conformité, mobilité) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la description des projets, tâches, incidents
- **Templates métiers construction** (gestion de chantier, suivi d’avancement, planning, gestion des équipes, sécurité)
- **Gestion des projets et chantiers** (fiche projet, avancement, photos, documents, plans)
- **Gestion des ressources** (matériel, main d’œuvre, sous-traitants, fournisseurs)
- **Gestion des utilisateurs & rôles** (chef de projet, chef de chantier, ouvrier, conducteur de travaux, admin)
- **Notifications & mailing** (alertes sécurité, rappels, incidents, planning)
- **SEO automatique** (balises, sitemap, microdata schema.org/ConstructionCompany)
- **Export/Import** (JSON, YAML, PDF, partage en un clic)
- **Marketplace de plugins** (planning, météo, conformité, analytics)
- **Accessibilité renforcée** (contrastes, navigation clavier, ARIA)
- **Sécurité** (validation des fichiers, CORS, rate limiting, logs auditables)
- **Conformité RGPD** (suppression/export/anonymisation des données sur demande)

---

## 📦 Structure recommandée

```
ConstructionCard/
  ConstructionCard.jsx|vue|svelte   # Composant principal (React/Vue/Svelte)
  ConstructionCard.module.css       # Styles dédiés (ou Tailwind)
  ConstructionCard.test.js          # Tests unitaires et d’intégration
  assets/                           # Icônes, images, illustrations construction
  README.md                         # Ce fichier
```

---

## 🛠️ Exemple d’utilisation (React)

```jsx
import ConstructionCard from './ConstructionCard';

<ConstructionCard
  projectName="Immeuble Amazigh"
  location="Tizi Ouzou"
  startDate="2025-04-01"
  endDate="2026-01-15"
  status="En cours"
  progress={30}
  team={[{ name: "Yacine", role: "Chef de projet" }, { name: "Samira", role: "Ingénieure" }]}
  onDownloadReport={() => {/* ... */}}
  onAddIncident={() => {/* ... */}}
/>
```

---

## 🔒 Sécurité & Bonnes pratiques

- **Validation stricte** des fichiers uploadés (taille, type, virus)
- **Aucune donnée personnelle** sans consentement explicite
- **Logs auditables** et suppression/export sur demande (RGPD)
- **Pas de dépendance critique à une API propriétaire**
- **Tests unitaires et d’intégration** obligatoires

---

## 🌐 Accessibilité & SEO

- Contraste et navigation clavier testés (WCAG)
- Texte alternatif pour chaque média
- Microdata schema.org/ConstructionCompany pour le SEO

---

## 📚 Documentation

- [Templates métiers construction](../../../docs/contribution/templates/README.md)
- [Charte graphique & branding](../../../branding/README.md)
- [Guide design général](../../../design/README.md)

---

## 🤝 Contribution

- Proposer des variantes (chantier, planning, sécurité, conformité…)
- Respecter la charte graphique et la conformité RGPD
- Documenter chaque ajout (usage, sécurité, accessibilité)

---

© Dihya Coding – 2025
```