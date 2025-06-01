# Composant BtpCard

**Composant métier BTP pour Dihya Coding – Génération de solutions numériques pour le Bâtiment et Travaux Publics : gestion de chantiers, suivi de projets, ressources, sécurité, conformité et mobilité.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés au secteur BTP (gestion de chantiers, suivi d’avancement, ressources humaines et matérielles, sécurité, conformité, mobilité) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la description des chantiers, tâches, incidents
- **Templates métiers BTP** (gestion de chantier, suivi d’avancement, planning, gestion des équipes, sécurité)
- **Gestion des projets et chantiers** (fiche chantier, avancement, photos, documents, plans)
- **Gestion des ressources** (matériel, main d’œuvre, sous-traitants, fournisseurs)
- **Gestion des utilisateurs & rôles** (chef de chantier, ouvrier, conducteur de travaux, admin)
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
# Composant BtpCard

**Composant métier BTP pour Dihya Coding – Génération de solutions numériques pour le Bâtiment et Travaux Publics : gestion de chantiers, suivi de projets, ressources, sécurité, conformité et mobilité.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés au secteur BTP (gestion de chantiers, suivi d’avancement, ressources humaines et matérielles, sécurité, conformité, mobilité) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la description des chantiers, tâches, incidents
- **Templates métiers BTP** (gestion de chantier, suivi d’avancement, planning, gestion des équipes, sécurité)
- **Gestion des projets et chantiers** (fiche chantier, avancement, photos, documents, plans)
- **Gestion des ressources** (matériel, main d’œuvre, sous-traitants, fournisseurs)
- **Gestion des utilisateurs & rôles** (chef de chantier, ouvrier, conducteur de travaux, admin)
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
BtpCard/
  BtpCard.jsx|vue|svelte      # Composant principal (React/Vue/Svelte)
  BtpCard.module.css          # Styles dédiés (ou Tailwind)
  BtpCard.test.js             # Tests unitaires et d’intégration
  assets/                     # Icônes, images, illustrations BTP
  README.md                   # Ce fichier
```

---

## 🛠️ Exemple d’utilisation (React)

```jsx
import BtpCard from './BtpCard';

<BtpCard
  chantierName="Extension Lycée Dihya"
  location="Alger"
  startDate="2025-03-01"
  endDate="2025-12-15"
  status="En cours"
  progress={45}
  team={[{ name: "Ali", role: "Chef de chantier" }, { name: "Nadia", role: "Ingénieure" }]}
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

- [Templates métiers BTP](../../../docs/contribution/templates/README.md)
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