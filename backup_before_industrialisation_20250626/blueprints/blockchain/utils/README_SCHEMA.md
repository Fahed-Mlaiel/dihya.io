# README_SCHEMA.md – Utils

## Schéma d’architecture (ASCII)
```
[utils/seo.js] [utils/validators.js] [utils/arrayHelpers.js] [utils/dateHelpers.js] [utils/fileHelpers.js]
   |                |                    |                    |                    |
[SEO]         [Validation]         [Tableaux]           [Dates]            [Fichiers]
```

## Conventions
- Un helper = une logique métier réutilisable
- Exemples d’utilisation dans README_EXEMPLES.md
- Export via index.js

## Cas métier réels
- Génération de balises SEO dynamiques
- Validation de formulaires (email, mot de passe, required)
- Manipulation de tableaux métiers
- Formatage de dates multilingues
- Upload et gestion de fichiers
