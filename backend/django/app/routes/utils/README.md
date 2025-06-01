# 🛠️ Dihya – Django Utils API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/utils`](#rôle-du-dossier-routesutils)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API utils](#exemples-dapi-utils)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🛠️ Rôle du dossier `routes/utils`

Ce dossier regroupe tous les endpoints, vues, serializers et assets utilitaires transverses à l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration outils externes, cloud souverain, IA utils, outils de conversion, génération, validation, monitoring
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement, anonymisation
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST utilitaires** : génération UUID, conversion formats, validation emails, monitoring, outils IA, notifications, logs, rapports, outils de migration, backup/restore
- **Gestion des droits d’accès** : RBAC (admin, utils, dev, guest)
- **Traçabilité et logs** : audit des accès, modifications, suppressions, exports
- **Interopérabilité** : intégration avec outils externes, open data, webhooks, partenaires
- **Automatisation** : notifications, alertes, génération de rapports, IA utils, monitoring continu
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
utils/
├── views.py           # Vues Django REST pour outils utilitaires (UUID, conversion, validation, monitoring, IA utils)
├── serializers.py     # Serializers pour outils utilitaires
├── urls.py            # Routage des endpoints utils
├── permissions.py     # Permissions RBAC pour l’accès aux services utils
├── tasks.py           # Tâches asynchrones (notifications, IA, génération rapports, monitoring)
├── assets/            # Exemples de scripts, modèles IA, rapports, templates
├── tests/             # Tests unitaires et d’intégration API utils
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, utils, dev, guest)
- **Logs d’accès** et d’opérations critiques (création, modification, suppression)
- **Chiffrement** des données sensibles (logs, rapports, identités)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque asset utilitaire

---

## 🛠️ Exemples d’API utils

### Génération d’un UUID

```http
GET /api/utils/uuid/
Authorization: Bearer <token>
Accept: application/json
```

### Validation d’un email

```http
POST /api/utils/validate_email/
Authorization: Bearer <token>
Content-Type: application/json

{
  "email": "contact@dihya.io"
}
```

### Monitoring système

```http
GET /api/utils/monitoring/
Authorization: Bearer <token>
Accept: application/json
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, monitoring) aux rôles autorisés
- **Exporter** tous les logs et rapports d’audit (CSV, JSON)
- **Automatiser** l’exécution en CI/CD (GitHub Actions, Codespaces)
- **Séparer** scripts Python et Node.js pour compatibilité maximale

---

## 🌍 Multilingue

- **Français** : Ce dossier est documenté en français.
- **English** : This folder is documented in English.
- **العربية** : هذا المجلد موثق باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Afaylu agi yettwarnan s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## 📚 Documentation associée

- [Architecture backend](../../../../docs/architecture.md)
- [API Utils (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Utils souverains, extensibles, multilingues, prêts pour la production, la démo et la contribution.

---
