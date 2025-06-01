# 🧬 Dihya – Django Science API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/science`](#rôle-du-dossier-routesscience)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API science](#exemples-dapi-science)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🧬 Rôle du dossier `routes/science`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, la valorisation et l’innovation scientifique via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration open science, cloud souverain, IA science, gestion publications, données, expériences, lab notebooks
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement, anonymisation, traçabilité scientifique
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST science** : gestion des publications, projets, expériences, jeux de données, lab notebooks, chercheurs, institutions, IA science, notifications, rapports
- **Gestion des droits d’accès** : RBAC (admin, chercheur, reviewer, institution, guest)
- **Traçabilité et logs** : audit des accès, modifications, suppressions, exports, accès données sensibles
- **Interopérabilité** : intégration avec open science, HAL, arXiv, open data, webhooks, partenaires
- **Automatisation** : notifications, alertes, génération de rapports, IA science, gestion des publications, peer review, extraction de données
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
science/
├── views.py           # Vues Django REST pour publications, projets, expériences, jeux de données, lab notebooks, chercheurs, institutions, IA science
├── serializers.py     # Serializers pour publications, projets, expériences, jeux de données, lab notebooks, chercheurs, institutions, IA science
├── urls.py            # Routage des endpoints science
├── permissions.py     # Permissions RBAC pour l’accès aux services science
├── tasks.py           # Tâches asynchrones (notifications, IA, génération rapports, peer review)
├── assets/            # Exemples de publications, modèles IA, rapports, templates
├── tests/             # Tests unitaires et d’intégration API science
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, chercheur, reviewer, institution, guest)
- **Logs d’accès** et d’opérations critiques (création, modification, suppression, accès données sensibles)
- **Chiffrement** des données sensibles (publications, jeux de données, identités)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité, consentement
- **Scripts de vérification d’intégrité** pour chaque publication ou asset science

---

## 🛠️ Exemples d’API science

### Création d’une publication scientifique

```http
POST /api/science/publications/
Authorization: Bearer <token>
Content-Type: application/json

{
  "titre": "Découverte d’un nouvel algorithme IA souverain",
  "auteurs": [2, 5],
  "projet_id": 7,
  "date_publication": "2025-11-01"
}
```

### Ajout d’un jeu de données

```http
POST /api/science/jeux_donnees/
Authorization: Bearer <token>
Content-Type: application/json

{
  "nom": "Données Amazigh 2025",
  "description": "Corpus linguistique amazigh open source.",
  "projet_id": 7
}
```

### Génération d’un rapport IA

```http
GET /api/science/ia/?projet_id=7
Authorization: Bearer <token>
Accept: application/json
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, accès données sensibles) aux rôles autorisés
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
- [API Science (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Science souveraine, extensible, multilingue, prête pour la production, la démo et la contribution.

---
