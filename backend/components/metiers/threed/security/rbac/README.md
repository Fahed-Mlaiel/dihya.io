# rbac/

Ce dossier regroupe les modules de gestion RBAC (Role-Based Access Control) :
- `engine/` : moteur RBAC (Node.js, Python)
- `roles/` : gestion des rôles (Node.js, Python)
- `permissions/` : gestion des permissions (Node.js, Python)
- `samples/` : exemples avancés d’utilisation (engine, roles, permissions)

Chaque sous-dossier contient :
- Les scripts principaux
- Un README explicatif
- Les fichiers d’initialisation (`__init__.js`, `__init__.py`)
- Un fichier `.keep` pour le versionnement

Le point d’entrée principal du module est `index.js`.

## Bonnes pratiques
- Ajouter tout nouveau module ou exemple dans le sous-dossier approprié.
- Documenter chaque module et fournir des exemples d’utilisation.
- Ajouter des tests unitaires pour chaque module.

---

Structure validée par un ingénieur senior, clé en main, prête pour l’industrialisation.
