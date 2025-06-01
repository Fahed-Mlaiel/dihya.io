# Hôtellerie – API Dihya

Ce module gère les routes RESTful et GraphQL pour la gestion de projets hôtellerie (réservations, IA, etc.) avec sécurité maximale, multilingue, multitenant, audit, et intégration IA.

## Fonctionnalités principales
- CRUD hôtels, chambres, réservations, clients
- Sécurité avancée (CORS, JWT, WAF, anti-DDOS, audit)
- Internationalisation dynamique (fr, en, ar, etc.)
- Support GraphQL et REST
- Multitenancy, gestion des rôles (admin, user, invité)
- Intégration IA (LLaMA, Mixtral, fallback)
- SEO backend (sitemap, robots, logs structurés)
- Plugins extensibles
- RGPD, audit, anonymisation, export
- Tests complets (unit, integration, e2e)

## Exemples d'utilisation
- Création de réservation
- Génération automatique de chambres
- Export audit RGPD

## Multilingue
Toutes les routes et messages sont disponibles en : français, anglais, arabe, amazigh, allemand, chinois, japonais, coréen, néerlandais, hébreu, persan, hindi, espagnol.

## Sécurité
- JWT obligatoire
- CORS strict
- Validation stricte
- Audit log
- WAF intégré
- Anti-DDOS

## Extensibilité
Ajout de plugins via API ou CLI.

## Déploiement
Compatible Docker, K8s, GitHub Actions, fallback local.

---
