# Politique de sécurité et conformité pour le module Energie

- Authentification JWT obligatoire
- Rôles supportés : admin, user, invité
- RGPD : logs, anonymisation, export
- CORS strict, WAF, anti-DDOS, audit
- Plugins autorisés : IA, monitoring, export
- Multilingue : fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es
- Accès API REST/GraphQL sécurisé
- Déploiement : Docker, K8s, fallback local
- SEO : robots.txt, sitemap.xml dynamiques
- Tests : unitaires, intégration, e2e, mocks
- Conformité Codespaces, Linux, CI/CD

## Exemples de règles
- Un admin peut créer, modifier, supprimer tout projet Energie
- Un user peut lister et consulter les projets Energie
- Un invité peut uniquement lister les projets publics
- Toute action est auditée et exportable
- Les plugins doivent être validés et auditables
