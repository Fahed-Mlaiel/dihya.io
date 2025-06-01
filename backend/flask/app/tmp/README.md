# Dossier `tmp/` — Backend Dihya Coding

Ce dossier est réservé aux fichiers temporaires générés ou utilisés par le backend Dihya Coding.

## Bonnes pratiques Dihya Coding

- **Aucun secret ou donnée sensible** ne doit être stocké durablement ici.
- Utiliser ce dossier uniquement pour des fichiers temporaires (ex : fichiers d’upload en attente, traitements batch, logs éphémères).
- **Nettoyage automatique** : prévoir des tâches planifiées pour supprimer régulièrement les fichiers anciens ou inutiles.
- **Accès restreint** : toute opération sur ce dossier doit être protégée par authentification (JWT ou autre).
- **Validation stricte** des fichiers déposés (type, taille, contenu).
- **Ne jamais exposer ce dossier en écriture via une API publique** sans contrôle strict.

## Exemples d’utilisation

- Fichiers d’upload en attente de validation
- Fichiers temporaires pour génération de rapports ou conversion de formats
- Logs éphémères pour débogage

## Sécurité

- Logger toute opération d’écriture ou de suppression pour audit.
- Ne jamais conserver de fichiers temporaires plus longtemps que nécessaire.
- Interdire l’exécution de fichiers stockés dans ce dossier.

---

*Ce fichier fait partie de la documentation interne Dihya Coding.*