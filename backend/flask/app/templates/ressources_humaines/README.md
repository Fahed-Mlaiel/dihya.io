# Template Métier "Ressources Humaines" – Dihya Coding

## Présentation

Ce template "Ressources Humaines" fait partie de la plateforme **Dihya Coding**, solution No-Code / Low-Code générant automatiquement des applications de gestion RH, recrutement, talents, paie, formation et suivi du personnel à partir d’un cahier des charges écrit ou vocal.

- **Frontend** : React + Tailwind (UI moderne, responsive, thème amazigh personnalisable)
- **Backend** : Flask (API RESTful sécurisée, gestion rôles, workflow RH)
- **Déploiement** : GitHub Actions, Pages, Replit fallback
- **Multilingue** : i18n dynamique, dialectes supportés

---

## Fonctionnalités principales

- **Gestion des employés** (profils, contrats, historique, documents)
- **Gestion du recrutement** (offres, candidatures, entretiens, suivi)
- **Gestion des absences & congés** (demandes, validation, planning)
- **Gestion de la paie** (bulletins, variables, export, historique)
- **Gestion des compétences & formations** (catalogue, suivi, évaluations)
- **Gestion des entretiens annuels** (objectifs, feedback, reporting)
- **Gestion des équipes & organigramme** (affectations, rôles, hiérarchie)
- **Gestion des tâches RH** (assignation, rappels, notifications)
- **Tableaux de bord & analytics** (KPI, visualisation, alertes)
- **Marketplace de plugins** (modules : paie, formation, analytics, custom)
- **Authentification** (JWT/OAuth, rôles admin/RH/manager/employé)
- **SEO & sécurité** (balises, sitemap, rate limiting, headers)
- **Démo instantanée** (preview live, lien partageable)
- **Extensible** (ajout facile de nouvelles fonctionnalités via plugins ou API)

---

## Routes Backend (Flask)

| Méthode | Endpoint                      | Description                                 | Authentification      |
|---------|-------------------------------|---------------------------------------------|-----------------------|
| GET     | `/api/employees`              | Liste des employés                          | RH/Admin              |
| POST    | `/api/employees`              | Créer/modifier un employé                   | RH/Admin              |
| GET     | `/api/recruitment`            | Liste des offres/candidatures               | RH/Admin              |
| POST    | `/api/recruitment`            | Ajouter/modifier une offre/candidature      | RH/Admin              |
| GET     | `/api/absences`               | Liste des absences/congés                   | RH/Admin/Manager      |
| POST    | `/api/absences`               | Ajouter/modifier une absence/congé          | RH/Admin/Manager      |
| GET     | `/api/payroll`                | Liste des bulletins de paie                 | RH/Admin              |
| POST    | `/api/payroll`                | Ajouter/modifier un bulletin de paie        | RH/Admin              |
| GET     | `/api/skills`                 | Liste des compétences/formations            | RH/Admin              |
| POST    | `/api/skills`                 | Ajouter/modifier une compétence/formation   | RH/Admin              |
| GET     | `/api/interviews`             | Liste des entretiens annuels                | RH/Admin/Manager      |
| POST    | `/api/interviews`             | Ajouter/modifier un entretien               | RH/Admin/Manager      |
| GET     | `/api/teams`                  | Liste des équipes/organigramme              | RH/Admin              |
| POST    | `/api/teams`                  | Ajouter/modifier une équipe                 | RH/Admin              |
| GET     | `/api/tasks`                  | Liste des tâches RH                         | RH/Admin/Manager      |
| POST    | `/api/tasks`                  | Créer/modifier une tâche RH                 | RH/Admin/Manager      |
| GET     | `/api/analytics`              | Tableaux de bord & KPI                      | Admin/RH/Manager      |
| GET     | `/api/notifications`          | Notifications                               | Tous rôles            |
| POST    | `/api/plugins`                | Ajouter un plugin                           | Admin                 |

---

## Logique Métier

- **Employés** : profils, contrats, documents, historique, stat<!-- filepath: /workspaces/Dihya/Dihya/backend/flask/app/templates/ressources_humaines/README.md -->

# Template Métier "Ressources Humaines" – Dihya Coding

## Présentation

Ce template "Ressources Humaines" fait partie de la plateforme **Dihya Coding**, solution No-Code / Low-Code générant automatiquement des applications de gestion RH, recrutement, talents, paie, formation et suivi du personnel à partir d’un cahier des charges écrit ou vocal.

- **Frontend** : React + Tailwind (UI moderne, responsive, thème amazigh personnalisable)
- **Backend** : Flask (API RESTful sécurisée, gestion rôles, workflow RH)
- **Déploiement** : GitHub Actions, Pages, Replit fallback
- **Multilingue** : i18n dynamique, dialectes supportés

---

## Fonctionnalités principales

- **Gestion des employés** (profils, contrats, historique, documents)
- **Gestion du recrutement** (offres, candidatures, entretiens, suivi)
- **Gestion des absences & congés** (demandes, validation, planning)
- **Gestion de la paie** (bulletins, variables, export, historique)
- **Gestion des compétences & formations** (catalogue, suivi, évaluations)
- **Gestion des entretiens annuels** (objectifs, feedback, reporting)
- **Gestion des équipes & organigramme** (affectations, rôles, hiérarchie)
- **Gestion des tâches RH** (assignation, rappels, notifications)
- **Tableaux de bord & analytics** (KPI, visualisation, alertes)
- **Marketplace de plugins** (modules : paie, formation, analytics, custom)
- **Authentification** (JWT/OAuth, rôles admin/RH/manager/employé)
- **SEO & sécurité** (balises, sitemap, rate limiting, headers)
- **Démo instantanée** (preview live, lien partageable)
- **Extensible** (ajout facile de nouvelles fonctionnalités via plugins ou API)

---

## Routes Backend (Flask)

| Méthode | Endpoint                      | Description                                 | Authentification      |
|---------|-------------------------------|---------------------------------------------|-----------------------|
| GET     | `/api/employees`              | Liste des employés                          | RH/Admin              |
| POST    | `/api/employees`              | Créer/modifier un employé                   | RH/Admin              |
| GET     | `/api/recruitment`            | Liste des offres/candidatures               | RH/Admin              |
| POST    | `/api/recruitment`            | Ajouter/modifier une offre/candidature      | RH/Admin              |
| GET     | `/api/absences`               | Liste des absences/congés                   | RH/Admin/Manager      |
| POST    | `/api/absences`               | Ajouter/modifier une absence/congé          | RH/Admin/Manager      |
| GET     | `/api/payroll`                | Liste des bulletins de paie                 | RH/Admin              |
| POST    | `/api/payroll`                | Ajouter/modifier un bulletin de paie        | RH/Admin              |
| GET     | `/api/skills`                 | Liste des compétences/formations            | RH/Admin              |
| POST    | `/api/skills`                 | Ajouter/modifier une compétence/formation   | RH/Admin              |
| GET     | `/api/interviews`             | Liste des entretiens annuels                | RH/Admin/Manager      |
| POST    | `/api/interviews`             | Ajouter/modifier un entretien               | RH/Admin/Manager      |
| GET     | `/api/teams`                  | Liste des équipes/organigramme              | RH/Admin              |
| POST    | `/api/teams`                  | Ajouter/modifier une équipe                 | RH/Admin              |
| GET     | `/api/tasks`                  | Liste des tâches RH                         | RH/Admin/Manager      |
| POST    | `/api/tasks`                  | Créer/modifier une tâche RH                 | RH/Admin/Manager      |
| GET     | `/api/analytics`              | Tableaux de bord & KPI                      | Admin/RH/Manager      |
| GET     | `/api/notifications`          | Notifications                               | Tous rôles            |
| POST    | `/api/plugins`                | Ajouter un plugin                           | Admin                 |

---

## Logique Métier

- **Employés** : profils, contrats, documents, historique, stat