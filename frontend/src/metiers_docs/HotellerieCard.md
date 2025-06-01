# Composant HotellerieCard

**Composant métier Hôtellerie pour Dihya Coding – Génération de solutions numériques pour hôtels, auberges, résidences, gestion de réservations, chambres, clients, services et facturation.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés à l’hôtellerie (gestion de réservations, chambres, clients, services, facturation, avis, fidélisation) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables, inspiration amazigh)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la description des chambres, services, réservations
- **Templates métiers hôtellerie** (hôtel, auberge, résidence, location saisonnière)
- **Gestion des chambres** (ajout, édition, suppression, disponibilité, photos, équipements)
- **Gestion des réservations** (création, modification, annulation, calendrier, historique)
- **Gestion des clients & rôles** (client, réception, ménage, admin)
- **Paiement en ligne** (Stripe, PayPal, plugins, QR code)
- **Facturation & devis** (génération, envoi, suivi)
- **Gestion des services** (restauration, spa, navette, room service)
- **Notifications & mailing** (confirmation, rappel, promo, avis)
- **Fidélisation & avis clients** (points, coupons, avis, recommandations IA)
- **SEO automatique** (balises, sitemap, microdata schema.org/Hotel)
- **Export/Import** (CSV, JSON, YAML, PDF, partage en un clic)
- **Marketplace de plugins** (analytics, CMS, newsletter, marketing, CRM)
- **Accessibilité renforcée** (contrastes, navigation clavier, ARIA)
- **Sécurité** (validation des fichiers, CORS, anti-fraude, logs auditables)
- **Conformité RGPD** (suppression/export/anonymisation des données sur demande)

---

## 📦 Structure recommandée
```markdown
# Composant HotellerieCard

**Composant métier Hôtellerie pour Dihya Coding – Génération de solutions numériques pour hôtels, auberges, résidences, gestion de réservations, chambres, clients, services et facturation.**  
_Slogan : De l’idée au code, en toute souveraineté._

---

## 🎯 Objectif

Permettre la création, la personnalisation et la gestion de projets numériques dédiés à l’hôtellerie (gestion de réservations, chambres, clients, services, facturation, avis, fidélisation) via une interface No-Code / Low-Code moderne, accessible et souveraine.

---

## 🏗️ Fonctionnalités du composant

- **UI/UX moderne et responsive** (Material UI/Tailwind, thèmes personnalisables, inspiration amazigh)
- **Support multilingue** (fr, en, ar, ber, dialectes)
- **Entrée texte libre et vocale** pour la description des chambres, services, réservations
- **Templates métiers hôtellerie** (hôtel, auberge, résidence, location saisonnière)
- **Gestion des chambres** (ajout, édition, suppression, disponibilité, photos, équipements)
- **Gestion des réservations** (création, modification, annulation, calendrier, historique)
- **Gestion des clients & rôles** (client, réception, ménage, admin)
- **Paiement en ligne** (Stripe, PayPal, plugins, QR code)
- **Facturation & devis** (génération, envoi, suivi)
- **Gestion des services** (restauration, spa, navette, room service)
- **Notifications & mailing** (confirmation, rappel, promo, avis)
- **Fidélisation & avis clients** (points, coupons, avis, recommandations IA)
- **SEO automatique** (balises, sitemap, microdata schema.org/Hotel)
- **Export/Import** (CSV, JSON, YAML, PDF, partage en un clic)
- **Marketplace de plugins** (analytics, CMS, newsletter, marketing, CRM)
- **Accessibilité renforcée** (contrastes, navigation clavier, ARIA)
- **Sécurité** (validation des fichiers, CORS, anti-fraude, logs auditables)
- **Conformité RGPD** (suppression/export/anonymisation des données sur demande)

---

## 📦 Structure recommandée

```
HotellerieCard/
  HotellerieCard.jsx|vue|svelte   # Composant principal (React/Vue/Svelte)
  HotellerieCard.module.css       # Styles dédiés (ou Tailwind)
  HotellerieCard.test.js          # Tests unitaires et d’intégration
  assets/                         # Icônes, images, illustrations hôtellerie
  README.md                       # Ce fichier
```

---

## 🛠️ Exemple d’utilisation (React)

```jsx
import HotellerieCard from './HotellerieCard';

<HotellerieCard
  hotelName="Hôtel Amazigh"
  rooms={[
    { number: 101, type: "Suite", price: 120, available: true, image: "/assets/suite.jpg" },
    { number: 102, type: "Double", price: 80, available: false, image: "/assets/double.jpg" }
  ]}
  reservations={[
    { client: "Nadia", room: 101, from: "2025-07-01", to: "2025-07-05" }
  ]}
  onBookRoom={room => {/* ... */}}
  onCheckout={reservation => {/* ... */}}
  onLeaveReview={client => {/* ... */}}
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
- Microdata schema.org/Hotel pour le SEO

---

## 📚 Documentation

- [Templates métiers hôtellerie](../../../docs/contribution/templates/README.md)
- [Charte graphique & branding](../../../branding/README.md)
- [Guide design général](../../../design/README.md)

---

## 🤝 Contribution

- Proposer des variantes (auberge, résidence, location saisonnière…)
- Respecter la charte graphique et la conformité RGPD
- Documenter chaque ajout (usage, sécurité, accessibilité)

---

© Dihya Coding – 2025
```