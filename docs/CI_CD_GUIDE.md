# CI/CD Guide Dihya

## Objectif
Fournir un guide complet pour l’intégration continue, le déploiement continu, et la sécurité CI/CD du projet Dihya.

## Stack
- GitHub Actions (tests, lint, audit, build, deploy)
- Docker, K8s, fallback local
- Sécurité : secrets, audit, anti-abus, logs
- Tests automatisés (unit, integration, e2e, accessibilité)
- Déploiement multi-environnements (prod, staging, demo)

## Bonnes pratiques
- CI obligatoire pour toute PR
- Audit, accessibilité, sécurité, SEO vérifiés à chaque build
- Logs structurés, exportables, anonymisables

## Exemples
- Voir `.github/workflows/`
- Voir `last_*_output.txt`

## Contact CI/CD
- cicd@dihya.org
