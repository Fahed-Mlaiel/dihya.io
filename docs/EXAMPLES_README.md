# Dihya Coding – Exemples & Démos

Ce fichier complète `EXAMPLES.md` avec des explications détaillées, des cas d’usage réels, et des conseils pour adapter chaque exemple à vos besoins (débutant à expert).

## Exemples API
- **Création de projet IA** : voir `EXAMPLES.md`, section 1. Personnalisez le champ `type` selon vos besoins (AI, VR, AR, Web, Mobile).
- **Sécurité JWT/CORS** : chaque appel API nécessite un JWT valide et respecte les politiques CORS strictes.
- **GraphQL** : utilisez l’endpoint `/graphql` pour des requêtes avancées, multilingues, et filtrées par rôle.

## Exemples Plugins
- **Ajout plugin IA** : voir `EXAMPLES.md`, section 4. Les plugins sont sandboxés, audités, et peuvent être ajoutés/retirés dynamiquement.
- **Développement plugin** : suivez le guide `PLUGINS_README.md` pour créer un plugin compatible (exemple fourni).

## Internationalisation
- **Changement de langue** : PATCH `/users/me` avec le champ `lang` (fr, en, ar, de, etc.).
- **Ajout d’une langue** : ajoutez un fichier de traduction dans `/i18n/` et référencez-le dans la config.

## RGPD & Audit
- **Export données** : GET `/users/me/export` (format JSON/CSV, anonymisation automatique).
- **Logs d’audit** : accessibles par rôle admin, exportables, horodatés, chiffrés.

## Génération de projet
- **API de génération** : POST `/generate` avec type (web, mobile, script IA, etc.), template, langue.
- **Personnalisation** : chaque template est modulaire, extensible, documenté.

## Conseils
- Testez chaque exemple avec différents rôles (admin, user, invité).
- Utilisez les mocks/fixtures pour simuler des cas extrêmes (fail sécurité, fail accessibilité, fail RGPD).
- Consultez les guides d’intégration et de tests pour automatiser vos workflows.

---

Pour toute question, ouvrez une issue ou contactez les mainteneurs (`docs/MAINTAINERS.md`).
