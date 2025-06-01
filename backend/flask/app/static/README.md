# Dossier `static/` — Backend Dihya Coding

Ce dossier contient les fichiers statiques utilisés par le backend Dihya Coding.

## Bonnes pratiques Dihya Coding

- **Aucun secret ou donnée sensible** ne doit être stocké ici.
- Utiliser ce dossier uniquement pour des fichiers statiques nécessaires au backend (ex : images, fichiers CSS/JS pour l’admin, documentation statique, etc.).
- **Sécuriser l’accès** : les routes Flask qui servent ces fichiers doivent vérifier les droits d’accès si besoin.
- **Organisation** : séparer les sous-dossiers par usage (`images/`, `docs/`, etc.).
- **Extensibilité** : prévoir la possibilité d’ajouter des fichiers statiques pour des plugins backend.

## Exemples d’utilisation

- Fichiers d’icônes pour l’interface d’administration backend
- Documentation technique statique (Markdown, HTML)
- Fichiers de configuration publique (ex : manifest.json)

## Sécurité

- Ne jamais exposer ce dossier en écriture via une API.
- Contrôler les extensions de fichiers autorisées si upload.
- Logger tout accès anormal ou tentative d’accès à un fichier non autorisé.

---

*Ce fichier fait partie de la documentation interne Dihya Coding.*