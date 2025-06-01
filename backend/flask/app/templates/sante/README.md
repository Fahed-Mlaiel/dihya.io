# Template Métier "Santé" – Dihya Coding

## Présentation

Ce template "Santé" fait partie de la plateforme **Dihya Coding**, solution No-Code / Low-Code générant automatiquement des applications de gestion médicale, cabinets, cliniques, hôpitaux, laboratoires, dossiers patients, rendez-vous et suivi santé à partir d’un cahier des charges écrit ou vocal.

- **Frontend** : React + Tailwind (UI moderne, responsive, thème amazigh personnalisable)
- **Backend** : Flask (API RESTful sécurisée, gestion rôles, workflow santé)
- **Déploiement** : GitHub Actions, Pages, Replit fallback
- **Multilingue** : i18n dynamique, dialectes supportés

---

## Fonctionnalités principales

- **Gestion des patients** (profils, dossiers médicaux, historique, documents)
- **Gestion des rendez-vous** (création, calendrier, rappels, notifications)
- **Gestion des praticiens** (profils, spécialités, planning)
- **Gestion des consultations** (comptes-rendus, prescriptions, ordonnances)
- **Gestion des actes médicaux** (soins, examens, résultats, uploads)
- **Gestion de la facturation** (devis, paiements, mutuelles, export)
- **Gestion des stocks médicaux** (médicaments, consommables, alertes)
- **Tableaux de bord & analytics** (KPI santé, visualisation, alertes)
- **Marketplace de plugins** (modules : téléconsultation, e-prescription, analytics, custom)
- **Authentification** (JWT/OAuth, rôles admin/médecin/secrétaire/patient/invité)
- **SEO & sécurité** (balises, sitemap, rate limiting, headers)
- **Démo instantanée** (preview live, lien partageable)
- **Extensible** (ajout facile de nouvelles fonctionnalités via plugins ou API)

---

## Routes Backend (Flask)

| Méthode | Endpoint                | Description                                 | Authentification      |
|---------|-------------------------|---------------------------------------------|-----------------------|
| GET     | `/api/patients`         | Liste des patients                          | Médecin/Admin         |
| POST    | `/api/patients`         | Créer/modifier un patient                   | Médecin/Admin         |
| GET     | `/api/appointments`     | Liste des rendez-vous                       | Médecin/Secrétaire    |
| POST    | `/api/appointments`     | Créer/modifier un rendez-vous               | Médecin/Secrétaire    |
| GET     | `/api/practitioners`    | Liste des praticiens                        | Admin                 |
| POST    | `/api/practitioners`    | Ajouter/modifier un praticien               | Admin                 |
| GET     | `/api/consultations`    | Liste des consultations                     | Médecin/Admin         |
| POST    | `/api/consultations`    | Créer/modifier une consultation             | Médecin               |
| GET     | `/api/acts`             | Liste des actes médicaux/examens            | Médecin/Admin         |
| POST    | `/api/acts`             | Ajouter/modifier un acte médical            | Médecin               |
| GET     | `/api/billing`          | Liste des factures/devis                    | Admin/Secrétaire      |
| POST    | `/api/billing`          | Créer/modifier une facture                  | Admin/Secrétaire      |
| GET     | `/api/stocks`           | Liste des stocks médicaux                   | Admin                 |
| POST    | `/api/stocks`           | Ajouter/modifier un stock                   | Admin                 |
| GET     | `/api/analytics`        | Tableaux de bord & KPI santé                | Admin/Médecin         |
| GET     | `/api/notifications`    | Notifications                               | Tous rôles            |
| POST    | `/api/plugins`          | Ajouter un plugin                           | Admin                 |

---

## Logique Métier

- **Patients** : dossiers, historique, documents, alertes, RGPD
- **Rendez-vous** : calendrier, rappels, notifications, gestion conflits
- **Praticiens** : profils, spécialités, planning, disponibilité
- **Consultations** : comptes-rendus, prescriptions, ordonnances, uploads
- **Actes médicaux** : examens, résultats, gestion fichiers, alertes
- **Facturation** : devis, paiements, mutuelles, export, alertes
- **Stocks** : médicaments, consommables, alertes seuils, inventaire
- **Analytics** : KPI santé, alertes, visualisation, export
- **Sécurité** : validation stricte, CORS, headers, anti-DDoS, logs horodatés, RGPD

---

## Design UI/UX

- **Thème** : Modernité + héritage amazigh (couleurs, motifs, polices)
- **Responsive** : Mobile, tablette, desktop
- **Accessibilité** : Contrastes, navigation clavier, ARIA
- **Customisation** : Thèmes, logos, branding cabinet/clinique

---

## Extensibilité

- **Plugins** : téléconsultation, e-prescription, analytics, custom
- **Templates** : Import/export JSON, YAML, JS
- **Marketplace** : Contribution externe, notation, documentation

---

## Déploiement & Souveraineté

- **CI/CD** : GitHub Actions (tests, build, déploiement auto)
- **Fallback** : Replit/Render si GitHub indisponible
- **Hébergement décentralisé** : IPFS/DWeb (optionnel)
- **Backup** : Notion API, GitHub, local

---

## Contribution

- **Ajout de métiers** : Étendre la classe `BusinessTemplate`
- **Documentation claire** : Guide utilisateur, contribution, API
- **Licence** : AGPL (open-source, souveraineté)

---

## Exemple d’utilisation

1. Décrivez votre projet santé/médical (texte ou vocal)
2. Sélectionnez le template "Santé"
3. Personnalisez (modules, design, plugins)
4. Générez le code (frontend + backend)
5. Testez en live, partagez le lien, déployez en 1 clic

---

**Slogan** : _"De l’idée au code, en toute souveraineté."_

---