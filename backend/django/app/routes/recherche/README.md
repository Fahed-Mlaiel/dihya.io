# 🔎 Dihya – Django Recherche API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/recherche`](#rôle-du-dossier-routesrecherche)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API recherche](#exemples-dapi-recherche)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🔎 Rôle du dossier `routes/recherche`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la recherche avancée, la découverte, le filtrage et l’indexation de contenus via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration ElasticSearch, cloud souverain, IA recherche, open data
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement, anonymisation
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST recherche** : recherche plein texte, filtrage, suggestions, autocomplétion, facettes, IA recherche, logs, audit
- **Gestion des droits d’accès** : RBAC (admin, analyste, utilisateur, guest, auditeur)
- **Traçabilité et logs** : audit des accès, recherches, suppressions, exports
- **Interopérabilité** : intégration avec ElasticSearch, Solr, open data, webhooks, partenaires, fallback open source
- **Automatisation** : suggestions, notifications, IA recherche, indexation, fallback open source
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
recherche/
├── views.py           # Vues Django REST pour recherche, suggestions, autocomplétion, logs, IA
├── serializers.py     # Serializers pour recherche, suggestions, autocomplétion, logs, IA
├── urls.py            # Routage des endpoints recherche
├── permissions.py     # Permissions RBAC pour l’accès aux services recherche
├── tasks.py           # Tâches asynchrones (indexation, IA, notifications)
├── assets/            # Exemples d’index, modèles IA, rapports, templates
├── tests/             # Tests unitaires et d’intégration API recherche
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, analyste, utilisateur, guest)
- **Logs d’accès** et d’opérations critiques (recherche, suppression, export)
- **Chiffrement** des données sensibles (requêtes, logs, identités)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque index ou asset recherche

---

## 🛠️ Exemples d’API recherche

### Recherche plein texte

```http
GET /api/recherche/?q=amazigh
Authorization: Bearer <token>
Accept: application/json
```

### Suggestions IA

```http
GET /api/recherche/suggestions/?q=robe
Authorization: Bearer <token>
Accept: application/json
```

### Autocomplétion

```http
GET /api/recherche/autocomplete/?q=kab
Authorization: Bearer <token>
Accept: application/json
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (suppression, export, logs) aux rôles autorisés
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
- [API Recherche (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Recherche souveraine, extensible, multilingue, prête pour la production, la démo et la contribution.

---
