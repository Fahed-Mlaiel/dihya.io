# RBAC — Organisation des tests centralisés

Ce dossier regroupe tous les tests d’exemples (samples) pour le contrôle d’accès basé sur les rôles (RBAC), organisés par sous-dossier métier :

- `engine/` : moteur de règles RBAC
- `permissions/` : gestion des permissions
- `roles/` : gestion des rôles
- `index.js` : point d’entrée centralisé ultra avancé pour tous les tests RBAC (import dynamique, exports clé en main, métadonnées, CI/CD ready)

Chaque sous-dossier contient les fichiers de tests correspondants, prêts à être exécutés ou intégrés dans les pipelines CI/CD.

## Logique avancée
- Tous les modules sont importés dynamiquement via `index.js`.
- Métadonnées métier, couverture, auteur, date de mise à jour incluses dans chaque module.
- Structure clé en main, extensible, conforme au cahier des charges Dihya.

---

*Ajoutez ici tout nouveau test RBAC en respectant la structure et la logique métier. Dernière mise à jour : 2025-06-08.*
