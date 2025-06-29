# Dossier /app/i18n

Ce dossier centralise toute l’internationalisation de l’application : fichiers de langue, scripts d’auto-traduction, gestion des dialectes, etc.

## Structure recommandée
- i18n.js : gestion principale de l’i18n
- autoTranslate.js : auto-traduction via API
- dialectSupport.js : gestion dynamique des dialectes
- index.js, __init__.py : points d’entrée JS/Python
- *.json : fichiers de traduction structurés

Chaque fichier doit suivre les conventions du projet et être maintenu à jour.
