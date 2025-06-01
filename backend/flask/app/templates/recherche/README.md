# Template Métier "Recherche" – Dihya Coding

## Présentation

Ce template "Recherche" fait partie de la plateforme **Dihya Coding**, solution No-Code / Low-Code générant automatiquement des applications de gestion de projets de recherche, laboratoires, publications, équipes scientifiques et collaborations à partir d’un cahier des charges écrit ou vocal.

- **Frontend** : React + Tailwind (UI moderne, responsive, thème amazigh personnalisable)
- **Backend** : Flask (API RESTful sécurisée, gestion rôles, workflow recherche)
- **Déploiement** : GitHub Actions, Pages, Replit fallback
- **Multilingue** : i18n dynamique, dialectes supportés

---

## Fonctionnalités principales

- **Gestion des projets de recherche** (création, suivi, statuts, historique)
- **Gestion des équipes & membres** (profils, rôles, affectations, historique)
- **Gestion des publications & résultats** (articles, rapports, brevets, uploads)
- **Gestion des financements & budgets** (demandes, suivi, reporting)
- **Gestion des collaborations** (partenaires, conventions, échanges)
- **Gestion des tâches & planning** (assignation, validation, suivi)
- **Tableaux de bord & analytics** (KPI, visualisation, alertes)
- **Marketplace de plugins** (modules : bibliométrie, open science, analytics, custom)
- **Authentification** (JWT/OAuth, rôles admin/chercheur/partenaire/invité)
- **SEO & sécurité** (balises, sitemap, rate limiting, headers)
- **Démo instantanée** (preview live, lien partageable)
- **Extensible** (ajout facile de nouvelles fonctionnalités via plugins ou API)

---

## Routes Backend (Flask)

| Méthode | Endpoint                      | Description                                 | Authentification      |
|---------|-------------------------------|---------------------------------------------|-----------------------|
| GET     | `/api/projects`               | Liste des projets de recherche              | Chercheur/Admin       |
| POST    | `/api/projects`               | Créer/modifier un projet                    | Chercheur/Admin       |
| GET     | `/api/teams`                  | Liste des équipes/membres                   | Chercheur/Admin       |
| POST    | `/api/teams`                  | Ajouter/modifier une équipe/membre          | Chercheur/Admin       |
| GET     | `/api/publications`           | Liste des publications/rapports             | Chercheur/Admin       |
| POST    | `/api/publications`           | Ajouter/modifier une publication            | Chercheur/Admin       |
| GET     | `/api/funding`                | Liste des financements/budgets              | Chercheur/Admin       |
| POST    | `/api/funding`                | Ajouter/modifier un financement             | Chercheur/Admin       |
| GET     | `/api/collaborations`         | Liste des collaborations/partenaires        | Chercheur/Admin       |
| POST    | `/api/collaborations`         | Ajouter/modifier une collaboration          | Chercheur/Admin       |
| GET     | `/api/tasks`                  | Liste des tâches/planning                   | Chercheur/Admin       |
| POST    | `/api/tasks`                  | Créer/modifier une tâche                    | Chercheur/Admin       |
| GET     | `/api/analytics`              | Tableaux de bord & KPI                      | Admin/Chercheur       |
| GET     | `/api/notifications`          | Notifications                               | Tous rôles            |
| POST    | `/api/plugins`                | Ajouter un plugin                           | Admin                 |

---

## Logique Métier

- **Projets** : gestion statuts, jalons, historique, reporting, archivage
- **Équipes/Membres** : profils, rôles, affectations, historique contributions
- **Publications** : articles, rapports, brevets, uploads, versioning
- **Financements** : demandes, suivi, reporting, alertes
- **Collaborations** : partenaires, conventions, échanges, historique
- **Tâches/Planning** : assignation, validation, suivi, notifications
- **Analytics** : KPI, alertes, visualisation, export
- **Sécurité** : validation stricte, CORS, headers, anti-DDoS, logs horodatés

---

## Design UI/UX

- **Thème** : Modernité + héritage amazigh (couleurs, motifs, polices)
- **Responsive** : Mobile, tablette, desktop
- **Accessibilité** : Contrastes, navigation clavier, ARIA
- **Customisation** : Thèmes, logos, branding labo/institut

---

## Extensibilité

- **Plugins** : bibliométrie, open science, analytics, custom
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

1. Décrivez votre projet recherche/labo (texte ou vocal)
2. Sélectionnez le template "Recherche"
3. Personnalisez (modules, design, plugins)
4. Générez le code (frontend + backend)
5. Testez en live, partagez le lien, déployez en 1 clic

---

**Slogan** : _"De l’idée au code, en toute souveraineté."_

---