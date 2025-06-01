# AI Integration Tests (fusionné)

Ce dossier contient le contenu fusionné de l'ancien dossier `intelligence_artificielle`.
Toutes les références, tests et templates doivent désormais pointer ici.

---

# Tests d'intégration pour le module Intelligence Artificielle

Ce dossier contient les tests d'intégration pour la gestion des projets IA (intelligence artificielle, machine learning, deep learning, NLP, etc.).

## Structure
- `test_ai.js` : Tests d'intégration automatisés (Jest, supertest)

## Exécution

```bash
npm run test:integration -- --testPathPattern=ai
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
