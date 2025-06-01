# hotellerie

# Tests d'intégration secteur Hôtellerie

Ce dossier contient les tests d'intégration avancés pour les APIs du secteur Hôtellerie dans Dihya.

## Structure
- **Tests RESTful et GraphQL**
- **Sécurité (CORS, JWT, WAF, anti-DDOS)**
- **Internationalisation (fr, en, ar, ...)**
- **Multitenancy & rôles**
- **Auditabilité & RGPD**

## Exécution

```bash
pytest --tb=short --disable-warnings
```

## Exemples de tests
- Création de projet hôtelier (admin, user, invité)
- Vérification des logs structurés
- Tests d'accès multilingues
- Simulation d'attaque (WAF/DDOS)

## Multilingue
- Français, English, العربية, ⴰⵎⴰⵣⵉⵖ, Deutsch, 中文, 日本語, 한국어, Nederlands, עברית, فارسی, हिन्दी, Español

## Conformité
- RGPD, audit, anonymisation, export

## Contact
- [Dihya Open Source](https://github.com/dihya-coding)
