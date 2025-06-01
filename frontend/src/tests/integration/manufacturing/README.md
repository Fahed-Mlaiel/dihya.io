# Tests d'intégration pour le module Manufacturing

Ce dossier contient les tests d'intégration pour la gestion des projets dans le secteur manufacturing (industrie avancée, usines intelligentes, etc.).

## Structure
- `test_manufacturing.js` : Tests d'intégration automatisés (Jest, supertest)

## Exécution

```bash
npm run test:integration -- --testPathPattern=manufacturing
```

## Internationalisation
- Les tests couvrent les réponses en : français, anglais, arabe, amazigh, allemand, chinois, japonais, coréen, néerlandais, hébreu, persan, hindi, espagnol.

## Sécurité
- Authentification JWT obligatoire
- Contrôle CORS avancé
- Validation stricte des entrées
- Audit logging

## Conformité
- RGPD, auditabilité, anonymisation, export des accès

## Plugins
- Système de plugins testable via API/CLI

## Contact
Pour toute contribution, voir [CONTRIBUTING.md](../../../../CONTRIBUTING.md)
