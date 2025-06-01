# docs/scripts/ — Génération automatisée de documentation (Dihya Coding)

Ce dossier contient les scripts permettant de générer automatiquement la documentation de l’API backend Dihya Coding à partir des fichiers OpenAPI, des docstrings ou de l’introspection du code.

## Objectif

- Automatiser la production de documentation technique à jour pour les développeurs et utilisateurs.
- Permettre l’export dans plusieurs formats ouverts (Markdown, HTML, JSON…).
- Faciliter l’audit, la maintenance et l’onboarding.

## Bonnes pratiques

- Générer la documentation à chaque modification majeure de l’API.
- Logger chaque génération avec horodatage dans un fichier dédié.
- Ne jamais inclure de secrets ou d’exemples contenant des données sensibles dans la documentation.
- Documenter la procédure d’utilisation de chaque script ici.
- Tester la validité et la lisibilité des fichiers générés.

## Exemple d’utilisation

```bash
python generate_api_doc.py