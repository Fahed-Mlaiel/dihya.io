# energie

Ce module gère les routes, modèles, vues, permissions, audit et tests pour les projets énergétiques dans Dihya.

## Fonctionnalités principales
- API REST & GraphQL pour projets énergétiques
- Sécurité maximale (CORS, JWT, RBAC, audit, WAF, anti-DDOS)
- Multitenancy, gestion des rôles (admin, user, invité)
- Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Intégration plugins IA souverains (LLaMA, Mixtral, Mistral)
- RGPD, auditabilité, export, anonymisation
- Extensible via plugins/API/CLI

## Utilisation
Inclure `routes.py` dans le routeur principal Django. Voir exemples dans `tests.py`.

## Sécurité & RGPD
Toutes les actions sont logguées (voir `audit.py`). Export RGPD via permission dédiée.

## Extensibilité
Ajoutez vos plugins IA dans `plugins/` ou via l’API.

## Multilingue
Toutes les chaînes sont traduites via Django i18n.

## Tests
Lancez `pytest` pour une couverture complète (unit, intégration, e2e).
