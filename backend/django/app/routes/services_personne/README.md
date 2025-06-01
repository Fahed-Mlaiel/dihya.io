# 🧑‍💼 Dihya – Django Services à la Personne API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/services_personne`](#rôle-du-dossier-routesservices_personne)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API services à la personne](#exemples-dapi-services-à-la-personne)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🧑‍💼 Rôle du dossier `routes/services_personne`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, la valorisation et l’innovation dans les services à la personne via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration CRM, cloud souverain, IA services, gestion planning, réservations, facturation
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement, anonymisation
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST services à la personne** : gestion des clients, intervenants, prestations, plannings, réservations, factures, avis, IA services, notifications, rapports
- **Gestion des droits d’accès** : RBAC (admin, gestionnaire, intervenant, client, auditeur, guest)
- **Traçabilité et logs** : audit des accès, modifications, suppressions, exports
- **Interopérabilité** : intégration avec CRM, ERP, open data, webhooks, partenaires
- **Automatisation** : notifications, alertes, génération de rapports, IA recommandation, gestion planning, facturation dynamique
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
services_personne/
├── views.py           # Vues Django REST pour clients, intervenants, prestations, plannings, réservations, factures, avis, IA services
├── serializers.py     # Serializers pour clients, intervenants, prestations, plannings, réservations, factures, avis, IA services
├── urls.py            # Routage des endpoints services à la personne
├── permissions.py     # Permissions RBAC pour l’accès aux services à la personne
├── tasks.py           # Tâches asynchrones (notifications, IA, génération rapports, gestion planning)
├── assets/            # Exemples de prestations, modèles IA, rapports, templates
├── tests/             # Tests unitaires et d’intégration API services à la personne
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, gestionnaire, intervenant, client, guest)
- **Logs d’accès** et d’opérations critiques (création, modification, suppression)
- **Chiffrement** des données sensibles (clients, plannings, factures, identités)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque prestation ou asset services à la personne

---

## 🛠️ Exemples d’API services à la personne

### Création d’une prestation

```http
POST /api/services_personne/prestations/
Authorization: Bearer <token>
Content-Type: application/json

{
  "client_id": 12,
  "intervenant_id": 5,
  "type": "Ménage",
  "date": "2025-09-10T14:00:00",
  "duree": 2
}
```

### Réservation d’un service

```http
POST /api/services_personne/reservations/
Authorization: Bearer <token>
Content-Type: application/json

{
  "client_id": 12,
  "prestation_id": 7,
  "date": "2025-09-10T14:00:00"
}
```

### Génération d’une facture

```http
GET /api/services_personne/factures/?client_id=12
Authorization: Bearer <token>
Accept: application/pdf
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, facturation) aux rôles autorisés
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
- [API Services à la Personne (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Services à la personne souverains, extensibles, multilingues, prêts pour la production, la démo et la contribution.

---
