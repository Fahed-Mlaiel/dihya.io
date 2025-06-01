# 📰 Dihya – Django Journalisme API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/journalisme`](#rôle-du-dossier-routesjournalisme)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API journalisme](#exemples-dapi-journalisme)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 📰 Rôle du dossier `routes/journalisme`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, la publication et l’innovation dans le secteur du journalisme via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration CMS, cloud souverain, IA rédactionnelle
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST journalisme** : gestion des articles, journalistes, rubriques, médias, commentaires, publications, IA rédactionnelle
- **Gestion des droits d’accès** : RBAC (admin, journaliste, éditeur, lecteur, auditeur, guest)
- **Traçabilité et logs** : audit des accès, publications, modifications, suppressions, exports
- **Interopérabilité** : intégration avec CMS, plateformes médias, open data, webhooks, partenaires
- **Automatisation** : notifications, rappels, génération de contenus IA, modération, SEO, fact-checking
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
journalisme/
├── views.py           # Vues Django REST pour articles, journalistes, rubriques, médias, commentaires, publications
├── serializers.py     # Serializers pour articles, journalistes, rubriques, médias, commentaires, publications
├── urls.py            # Routage des endpoints journalisme
├── permissions.py     # Permissions RBAC pour l’accès aux services journalisme
├── tasks.py           # Tâches asynchrones (notifications, IA, modération, SEO)
├── assets/            # Exemples d’articles, images, modèles IA, rapports
├── tests/             # Tests unitaires et d’intégration API journalisme
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, journaliste, éditeur, lecteur, guest)
- **Logs d’accès** et d’opérations critiques (création, publication, suppression)
- **Chiffrement** des données sensibles (identités, brouillons, commentaires)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque article ou asset journalisme

---

## 🛠️ Exemples d’API journalisme

### Création d’un article

```http
POST /api/journalisme/articles/
Authorization: Bearer <token>
Content-Type: application/json

{
  "titre": "Dihya révolutionne le journalisme souverain",
  "contenu": "L’API Dihya permet une gestion avancée, multilingue et sécurisée des contenus journalistiques.",
  "auteur_id": 3,
  "rubrique": "Innovation"
}
```

### Publication d’un article

```http
POST /api/journalisme/publications/
Authorization: Bearer <token>
Content-Type: application/json

{
  "article_id": 12,
  "date_publication": "2025-06-01T09:00:00"
}
```

### Ajout d’un commentaire

```http
POST /api/journalisme/commentaires/
Authorization: Bearer <token>
Content-Type: application/json

{
  "article_id": 12,
  "auteur_id": 7,
  "contenu": "Bravo pour cette innovation souveraine !"
}
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, publication) aux rôles autorisés
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
- [API Journalisme (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Journalisme souverain, extensible, multilingue, prêt pour la production, la démo et la contribution.

---
