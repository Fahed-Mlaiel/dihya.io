# 👗 Dihya – Django Mode & Fashion API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/mode`](#rôle-du-dossier-routesmode)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API mode](#exemples-dapi-mode)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 👗 Rôle du dossier `routes/mode`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, la création et l’innovation dans le secteur de la mode via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration e-commerce, cloud souverain, IA fashion, PIM, DAM
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement, modération IA
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST mode** : gestion des collections, produits, créateurs, tendances, shootings, médias, avis, IA fashion, recommandations, modération
- **Gestion des droits d’accès** : RBAC (admin, créateur, styliste, client, auditeur, guest)
- **Traçabilité et logs** : audit des accès, créations, modifications, suppressions, exports
- **Interopérabilité** : intégration avec e-commerce, PIM, DAM, open data, webhooks, partenaires
- **Automatisation** : notifications, alertes, génération de recommandations IA, modération, gestion des stocks, promotions dynamiques
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
mode/
├── views.py           # Vues Django REST pour collections, produits, créateurs, tendances, shootings, médias, avis
├── serializers.py     # Serializers pour collections, produits, créateurs, tendances, shootings, médias, avis
├── urls.py            # Routage des endpoints mode
├── permissions.py     # Permissions RBAC pour l’accès aux services mode
├── tasks.py           # Tâches asynchrones (notifications, IA, gestion stocks, modération)
├── assets/            # Exemples de collections, images, modèles IA, templates
├── tests/             # Tests unitaires et d’intégration API mode
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, créateur, styliste, client, guest)
- **Logs d’accès** et d’opérations critiques (création, modification, suppression)
- **Chiffrement** des données sensibles (clients, créations, médias)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque collection ou asset mode

---

## 🛠️ Exemples d’API mode

### Création d’une collection

```http
POST /api/mode/collections/
Authorization: Bearer <token>
Content-Type: application/json

{
  "nom": "Printemps Amazigh",
  "annee": 2025,
  "createur_id": 4
}
```

### Ajout d’un produit

```http
POST /api/mode/produits/
Authorization: Bearer <token>
Content-Type: application/json

{
  "collection_id": 1,
  "nom": "Robe Kabyle",
  "taille": "M",
  "couleur": "bleu",
  "prix": 120.00
}
```

### Génération de recommandations IA

```http
GET /api/mode/ia/?client_id=7
Authorization: Bearer <token>
Accept: application/json
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, modération) aux rôles autorisés
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
- [API Mode (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Mode souveraine, extensible, multilingue, prête pour la production, la démo et la contribution.

---
