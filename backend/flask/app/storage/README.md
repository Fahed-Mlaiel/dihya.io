# Dossier `storage/` — Backend Dihya Coding

Ce dossier est destiné au stockage des fichiers persistants du backend Dihya Coding.

## Bonnes pratiques Dihya Coding

- **Aucun secret ou donnée sensible** ne doit être stocké en clair ici.
- Utiliser ce dossier pour les fichiers générés, exports, sauvegardes temporaires, ou autres données persistantes nécessaires au fonctionnement du backend.
- **Sécuriser l’accès** : toute opération de lecture/écriture doit être protégée par authentification (JWT ou autre).
- **Validation stricte** des fichiers : contrôler le type, la taille et le contenu avant d’accepter un fichier dans ce dossier.
- **Organisation** : créer des sous-dossiers par usage (`exports/`, `backups/`, etc.) pour faciliter la maintenance et l’audit.
- **Nettoyage régulier** : prévoir des tâches planifiées pour supprimer les fichiers obsolètes ou temporaires.

## Exemples d’utilisation

- Sauvegardes de la base de données (dumps)
- Exports de données utilisateur (CSV, JSON)
- Fichiers temporaires pour génération de rapports ou traitement batch

## Sécurité

- Ne jamais exposer ce dossier en écriture via une API publique sans contrôle strict.
- Logger toutes les opérations de lecture/écriture pour audit.
- Prévoir une politique de rétention et de suppression automatique des fichiers sensibles ou volumineux.

---

*Ce fichier fait partie de la documentation interne Dihya Coding.*