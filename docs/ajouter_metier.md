# Ajouter un Métier – Dihya

## Objectif
Permettre l’ajout d’un nouveau métier (domaine) dans la plateforme Dihya, avec sécurité, i18n, audit, plugins, RGPD.

## Étapes
1. **Créer un fichier** dans `docs/metiers/` (ex: `metiers/robotique.md`)
2. **Décrire le métier** :
   - Présentation, cas d’usage, API, sécurité, i18n, plugins, RGPD
3. **Ajouter les routes** dans `3d_routes.md` ou fichier métier dédié
4. **Définir les rôles** (admin, user, invité)
5. **Configurer l’i18n** (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
6. **Ajouter tests, exemples, docstring, auditabilité**
7. **Vérifier conformité RGPD, accessibilité, SEO**

## Exemple de template
```markdown
# Métier : Robotique

## Présentation
La robotique combine IA, 3D, VR, AR pour l’industrie, la santé, l’éducation…

## Cas d’usage
- Simulation robotique 3D
- Génération IA de scripts
- Collaboration temps réel

## API
- `GET /api/robotique/projects`
- `POST /api/robotique/generate`

## Sécurité
- JWT, CORS, WAF, audit, RGPD

## Internationalisation
- fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es

## Plugins
- Génération IA, export multi-format

## RGPD
- Logs, anonymisation, export
```

---
*Procédure multilingue, sécurisée, auditable, conforme RGPD.*
