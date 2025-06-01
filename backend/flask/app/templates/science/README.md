# Template Métier "Science" – Dihya Coding

## Présentation

Ce template "Science" fait partie de la plateforme **Dihya Coding**, solution No-Code / Low-Code générant automatiquement des applications de gestion de projets scientifiques, laboratoires, publications, équipes, financements et collaborations à partir d’un cahier des charges écrit ou vocal.

- **Frontend** : React + Tailwind (UI moderne, responsive, thème amazigh personnalisable)
- **Backend** : Flask (API RESTful sécurisée, gestion rôles, workflow science)
- **Déploiement** : GitHub Actions, Pages, Replit fallback
- **Multilingue** : i18n dynamique, dialectes supportés

---

## Fonctionnalités principales

- **Gestion des projets scientifiques** (création, édition, suivi, statuts)
- **Gestion des équipes & membres** (profils, rôles, affectations)
- **Gestion des publications** (articles, rapports, export, DOI)
- **Gestion des financements** (budgets, sources, échéances)
- **Gestion des collaborations** (partenaires, conventions, échanges)
- **Gestion des tâches & plannings** (kanban, deadlines, notifications)
- **Tableaux de bord & analytics** (KPI, bibliométrie, visualisation)
- **Marketplace de plugins** (modules : open science, analytics, custom)
- **Authentification** (JWT/OAuth, rôles admin/chercheur/partenaire/invité)
- **SEO & sécurité** (balises, sitemap, rate limiting, headers)
- **Démo instantanée** (preview live, lien partageable)
- **Extensible** (ajout facile de nouvelles fonctionnalités via plugins ou API)

---

## Routes Backend (Flask)

| Méthode | Endpoint                | Description                                 | Authentification      |
|---------|-------------------------|---------------------------------------------|-----------------------|
| GET     | `/api/projects`         | Liste des projets scientifiques             | Chercheur/Admin       |
| POST    | `/api/projects`         | Créer/modifier un projet                    | Chercheur/Admin       |
| GET     | `/api/teams`            | Liste des équipes/membres                   | Chercheur/Admin       |
| POST    | `/api/teams`            | Ajouter/modifier une équipe/membre          | Chercheur/Admin       |
| GET     | `/api/publications`     | Liste des publications/rapports             | Chercheur/Admin       |
| POST    | `/api/publications`     | Ajouter/modifier une publication            | Chercheur/Admin       |
| GET     | `/api/funding`          | Liste des financements/budgets              | Chercheur/Admin       |
| POST    | `/api/funding`          | Ajouter/modifier un financement             | Chercheur/Admin       |
| GET     | `/api/collaborations`   | Liste des collaborations/partenaires        | Chercheur/Admin       |
| POST    | `/api/collaborations`   | Ajouter/modifier une collaboration          | Chercheur/Admin       |
| GET     | `/api/tasks`            | Liste des tâches/planning                   | Chercheur/Admin       |
| POST    | `/api/tasks`            | Créer/modifier une tâche                    | Chercheur/Admin       |
| GET     | `/api/analytics`        | Tableaux de bord & KPI                      | Admin/Chercheur       |
| GET     | `/api/notifications`    | Notifications                               | Tous rôles            |
| POST    | `/api/plugins`          | Ajouter un plugin                           | Admin                 |

---

## Logique Métier

- **Projets** : suivi, statuts, jalons, documentation, alertes
- **Équipes** : gestion membres, rôles, affectations, notifications
- **Publications** : articles, rapports, DOI, export, bibliométrie
- **Financements** : budgets, échéances, alertes, reporting
- **Collaborations** : partenaires, conventions, échanges, suivi
- **Tâches** : kanban, deadlines, notifications, historique
- **Analytics** : KPI, bibliométrie, visualisation, export
- **Sécurité** : validation stricte, CORS, headers, anti-DDoS, logs horodatés

---

## Design UI/UX

- **Thème** : Modernité + héritage amazigh (couleurs, motifs, polices)
- **Responsive** : Mobile, tablette, desktop
- **Accessibilité** : Contrastes, navigation clavier, ARIA
- **Customisation** : Thèmes, logos, branding labo/projet

---

## Extensibilité

- **Plugins** : open science, analytics, custom
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

1. Décrivez votre projet scientifique (texte ou vocal)
2. Sélectionnez le template "Science"
3. Personnalisez (modules, design, plugins)
4. Générez le code (frontend + backend)
5. Testez en live, partagez le lien, déployez en 1 clic

---

**Slogan** : _"De l’idée au code, en toute souveraineté."_

---