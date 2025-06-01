# 👁️ Dihya – Django Preview API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/preview`](#rôle-du-dossier-routespreview)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API preview](#exemples-dapi-preview)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 👁️ Rôle du dossier `routes/preview`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la prévisualisation de contenus (documents, médias, pages, données) via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration CMS, cloud souverain, IA preview, conversion, streaming
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement, filigrane
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST preview** : prévisualisation de documents, images, vidéos, audio, pages web, données structurées, IA preview, conversion, streaming
- **Gestion des droits d’accès** : RBAC (admin, éditeur, contributeur, lecteur, guest)
- **Traçabilité et logs** : audit des accès, prévisualisations, suppressions, exports
- **Interopérabilité** : intégration avec CMS, DAM, open data, webhooks, partenaires, fallback open source
- **Automatisation** : notifications, conversions, génération de miniatures, IA preview, OCR, transcription, fallback open source
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
preview/
├── views.py           # Vues Django REST pour preview de documents, images, vidéos, audio, pages, données, IA
├── serializers.py     # Serializers pour preview de documents, images, vidéos, audio, pages, données, IA
├── urls.py            # Routage des endpoints preview
├── permissions.py     # Permissions RBAC pour l’accès aux services preview
├── tasks.py           # Tâches asynchrones (conversions, IA, notifications, OCR)
├── assets/            # Exemples de contenus, modèles IA, rapports, templates
├── tests/             # Tests unitaires et d’intégration API preview
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, éditeur, contributeur, lecteur, guest)
- **Logs d’accès** et d’opérations critiques (prévisualisation, suppression)
- **Chiffrement** des données sensibles (documents, médias, identités)
- **Filigrane** pour les contenus critiques
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque preview ou asset

---

## 🛠️ Exemples d’API preview

### Prévisualisation d’un document

```http
GET /api/preview/documents/12/
Authorization: Bearer <token>
Accept: application/pdf
```

### Génération de miniature d’une image

```http
POST /api/preview/images/thumbnail/
Authorization: Bearer <token>
Content-Type: application/json

{
  "image_id": 42,
  "taille": "200x200"
}
```

### Prévisualisation d’une page web

```http
GET /api/preview/pages/?url=https://dihya.io
Authorization: Bearer <token>
Accept: text/html
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (prévisualisation, suppression, export) aux rôles autorisés
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
- [API Preview (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Preview souverain, extensible, multilingue, prêt pour la production, la démo et la contribution.

---
