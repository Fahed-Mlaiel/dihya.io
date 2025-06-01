# 🏅 Dihya – Django Sport API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/sport`](#rôle-du-dossier-routessport)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API sport](#exemples-dapi-sport)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🏅 Rôle du dossier `routes/sport`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, l’innovation et la valorisation du secteur sport via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration ERP/CRM, cloud souverain, IA sport, gestion clubs, compétitions, résultats, entraînements, billetterie
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement, anonymisation
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST sport** : gestion des clubs, équipes, athlètes, compétitions, résultats, entraînements, billetterie, IA sport, notifications, rapports
- **Gestion des droits d’accès** : RBAC (admin, coach, athlète, supporter, auditeur, guest)
- **Traçabilité et logs** : audit des accès, modifications, suppressions, exports
- **Interopérabilité** : intégration avec ERP, CRM, open data, webhooks, partenaires
- **Automatisation** : notifications, alertes, génération de rapports, IA recommandation, gestion planning, billetterie dynamique
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
sport/
├── views.py           # Vues Django REST pour clubs, équipes, athlètes, compétitions, résultats, entraînements, billetterie, IA sport
├── serializers.py     # Serializers pour clubs, équipes, athlètes, compétitions, résultats, entraînements, billetterie, IA sport
├── urls.py            # Routage des endpoints sport
├── permissions.py     # Permissions RBAC pour l’accès aux services sport
├── tasks.py           # Tâches asynchrones (notifications, IA, génération rapports, gestion planning)
├── assets/            # Exemples de compétitions, modèles IA, rapports, templates
├── tests/             # Tests unitaires et d’intégration API sport
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, coach, athlète, supporter, guest)
- **Logs d’accès** et d’opérations critiques (création, modification, suppression)
- **Chiffrement** des données sensibles (athlètes, résultats, billetterie, identités)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque compétition ou asset sport

---

## 🛠️ Exemples d’API sport

### Création d’un club

```http
POST /api/sport/clubs/
Authorization: Bearer <token>
Content-Type: application/json

{
  "nom": "US Kabylie",
  "ville": "Tizi Ouzou",
  "annee_fondation": 1946
}
```

### Ajout d’un résultat de compétition

```http
POST /api/sport/resultats/
Authorization: Bearer <token>
Content-Type: application/json

{
  "competition_id": 3,
  "equipe_id": 7,
  "score": 2,
  "adversaire": "MC Alger",
  "score_adversaire": 1
}
```

### Réservation de billet

```http
POST /api/sport/billetterie/
Authorization: Bearer <token>
Content-Type: application/json

{
  "competition_id": 3,
  "supporter_id": 12,
  "place": "Tribune Est"
}
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, billetterie) aux rôles autorisés
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
- [API Sport (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Sport souverain, extensible, multilingue, prêt pour la production, la démo et la contribution.

---
