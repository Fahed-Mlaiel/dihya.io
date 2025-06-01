# Multilingue – Migrations Dihya DB

Ce fichier documente les migrations multilingues (français, anglais, arabe, amazigh) pour la base de données Dihya.

## Bonnes pratiques
- Toujours prévoir la compatibilité multilingue dans les migrations
- Documenter chaque champ multilingue
- Tester les migrations sur des données dans chaque langue supportée

## Exemples
- Ajout de la colonne `lang` dans `users`
- Migration des données existantes vers la langue par défaut

---

> Voir les scripts SQL dans ce dossier et la documentation principale dans `../README.md`.
