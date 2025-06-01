# Composant BeauteCard

**Composant métier Beauté pour Dihya Coding – Génération de solutions numériques pour salons, instituts, spas, coiffeurs, esthéticien·nes, bien-être et réservation en ligne.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés au secteur de la beauté et du bien-être (gestion de rendez-vous, catalogue de prestations, gestion clients, paiement, fidélité, avis) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la description des prestations, profils, avis
- **Templates métiers beauté** (salon, institut, spa, coiffeur, esthétique, bien-être)
- **Gestion des rendez-vous** (prise, modification, annulation, rappels)
- **Gestion des clients & profils** (historique, fidélité, préférences, avis)
- **Catalogue de prestations** (services, tarifs, durée, images)
- **Paiement en ligne** (Stripe, plugins, QR code)
- **Notifications & mailing** (confirmation, rappel, promo)
- **SEO automatique** (balises, sitemap, microdata schema.org/BeautySalon)
- **Export/Import** (JSON, YAML, PDF, partage en un clic)
- **Marketplace de plugins** (paiement, fidélité, analytics, avis)
- **Accessibilité renforcée** (contrastes, navigation clavier, ARIA)
- **Sécurité** (validation des fichiers, CORS, rate limiting, logs auditables)
- **Conformité RGPD** (suppression/export/anonymisation des données sur demande)

---

## 📦 Structure recommandée
```markdown
# Composant BeauteCard

**Composant métier Beauté pour Dihya Coding – Génération de solutions numériques pour salons, instituts, spas, coiffeurs, esthéticien·nes, bien-être et réservation en ligne.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés au secteur de la beauté et du bien-être (gestion de rendez-vous, catalogue de prestations, gestion clients, paiement, fidélité, avis) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la description des prestations, profils, avis
- **Templates métiers beauté** (salon, institut, spa, coiffeur, esthétique, bien-être)
- **Gestion des rendez-vous** (prise, modification, annulation, rappels)
- **Gestion des clients & profils** (historique, fidélité, préférences, avis)
- **Catalogue de prestations** (services, tarifs, durée, images)
- **Paiement en ligne** (Stripe, plugins, QR code)
- **Notifications & mailing** (confirmation, rappel, promo)
- **SEO automatique** (balises, sitemap, microdata schema.org/BeautySalon)
- **Export/Import** (JSON, YAML, PDF, partage en un clic)
- **Marketplace de plugins** (paiement, fidélité, analytics, avis)
- **Accessibilité renforcée** (contrastes, navigation clavier, ARIA)
- **Sécurité** (validation des fichiers, CORS, rate limiting, logs auditables)
- **Conformité RGPD** (suppression/export/anonymisation des données sur demande)

---

## 📦 Structure recommandée

```
BeauteCard/
  BeauteCard.jsx|vue|svelte   # Composant principal (React/Vue/Svelte)
  BeauteCard.module.css       # Styles dédiés (ou Tailwind)
  BeauteCard.test.js          # Tests unitaires et d’intégration
  assets/                     # Icônes, images, illustrations beauté
  README.md                   # Ce fichier
```

---

## 🛠️ Exemple d’utilisation (React)

```jsx
import BeauteCard from './BeauteCard';

<BeauteCard
  salonName="Institut Dihya"
  address="123 Avenue de la Beauté, Tizi Ouzou"
  services={[
    { name: "Soin visage", price: 40, duration: 60 },
    { name: "Coiffure", price: 25, duration: 45 }
  ]}
  nextAvailable="2025-06-10T14:00"
  rating={4.8}
  onBook={() => {/* ... */}}
  onLeaveReview={() => {/* ... */}}
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
- Microdata schema.org/BeautySalon pour le SEO

---

## 📚 Documentation

- [Templates métiers beauté](../../../docs/contribution/templates/README.md)
- [Charte graphique & branding](../../../branding/README.md)
- [Guide design général](../../../design/README.md)

---

## 🤝 Contribution

- Proposer des variantes (institut, spa, coiffeur, bien-être…)
- Respecter la charte graphique et la conformité RGPD
- Documenter chaque ajout (usage, sécurité, accessibilité)

---

© Dihya Coding – 2025
```