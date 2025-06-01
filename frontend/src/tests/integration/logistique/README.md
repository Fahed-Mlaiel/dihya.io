# Tests d'intégration pour le module Logistique

Ce dossier contient les tests d'intégration pour la gestion des projets dans le secteur de la logistique.

## Structure
- `test_logistique.js` : Tests d'intégration automatisés (Jest, supertest)

## Exécution

```bash
npm run test:integration -- --testPathPattern=logistique
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
