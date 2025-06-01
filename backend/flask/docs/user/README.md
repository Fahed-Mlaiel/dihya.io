# docs/user/ — Documentation utilisateur backend (Dihya Coding)

Ce dossier regroupe la documentation destinée aux utilisateurs finaux, administrateurs ou clients du backend Flask Dihya Coding.

## Objectif

- Expliquer le fonctionnement des principales fonctionnalités accessibles via l’API ou l’interface d’administration.
- Fournir des guides pratiques pour l’utilisation, la configuration et la personnalisation du backend.
- Documenter les bonnes pratiques de sécurité, de gestion des comptes et des données.

## Bonnes pratiques

- Organiser la documentation par thématique ou fonctionnalité (authentification, gestion des projets, notifications, etc.).
- Utiliser un langage clair, accessible et illustré d’exemples concrets.
- Mettre à jour la documentation à chaque évolution majeure du backend.
- Inclure des captures d’écran ou schémas si pertinent.
- Documenter les limitations, prérequis et points de vigilance (sécurité, RGPD, etc.).

## Exemple de structure

- `auth.md` : guide d’utilisation de l’authentification et gestion des comptes.
- `projects.md` : gestion des projets, création, modification, suppression.
- `notifications.md` : gestion des notifications et préférences utilisateur.
- `faq.md` : réponses aux questions fréquentes.

## Exemple de contenu

```markdown
## Authentification

Pour accéder à l’espace utilisateur, connectez-vous via `/api/login` avec votre email et mot de passe.
En cas de perte de mot de passe, utilisez la fonctionnalité de réinitialisation disponible sur `/api/reset-password`.

### Sécurité

- Utilisez un mot de passe fort et unique.
- Activez la double authentification si disponible.
- Ne partagez jamais vos identifiants.

## Gestion des projets

Pour créer un projet, rendez-vous sur `/api/projects` et cliquez sur "Nouveau projet".
Vous pouvez modifier ou supprimer vos projets à tout moment depuis votre tableau de bord.