# 🏗️ Dihya – Django BTP (Bâtiment & Travaux Publics) API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/btp`](#rôle-du-dossier-routesbtp)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API BTP](#exemples-dapi-btp)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🏗️ Rôle du dossier `routes/btp`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, la planification, la traçabilité et l’innovation dans le secteur du BTP via l’API Django Dihya.

- **Multi-stack** : Django REST, intégration BIM, plugins Python/Node, cloud souverain, IoT chantier
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST BTP** : gestion de projets, chantiers, ressources, matériaux, équipements, sous-traitants, incidents, BIM
- **Gestion des droits d’accès** : RBAC (admin, chef de projet, ouvrier, sous-traitant, auditeur, guest)
- **Traçabilité et logs** : audit des accès, modifications, suppressions, exports
- **Interopérabilité** : intégration avec SI BTP, open data, webhooks, BIM, IoT chantier
- **Automatisation** : alertes sécurité, notifications, génération de rapports, suivi temps réel
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
btp/
├── views.py           # Vues Django REST pour le BTP
├── serializers.py     # Serializers pour projets, chantiers, ressources, incidents
├── urls.py            # Routage des endpoints BTP
├── permissions.py     # Permissions RBAC pour l’accès aux services BTP
├── tasks.py           # Tâches asynchrones (alertes, génération IA, suivi IoT)
├── assets/            # Exemples de plans, modèles BIM, open data
├── tests/             # Tests unitaires et d’intégration API BTP
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, chef de projet, ouvrier, sous-traitant, guest)
- **Logs d’accès** et d’opérations critiques (création, modification, suppression)
- **Anonymisation** des données sensibles dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque donnée ou asset BTP

---

## 🔒 Policies & RBAC/ABAC/PBAC (Ultra avancé)
- Siehe `policies.py`: alle Aktionen (Erstellung, Ansicht, Export, Audit, RGPD, Plugins, Multitenant, Accessibility, Fallback) sind fein granuliert, auditierbar, erweiterbar, multilingue.
- Helper `has_policy(role, action)` für Plugins, Audit, CI/CD, dynamische Erweiterung.

## 🧩 Plugins (Ultra avancé)
- Siehe `plugins.py`: dynamische Verwaltung, Audit, RGPD, Multilingue, Accessibility, Fallback, Multitenant, CI/CD-ready.
- Beispiel: Plugin für intelligente Baustellenverwaltung, Beschreibung in 4 Sprachen, Audit, einfache Erweiterung.

## 🧪 Fixtures & Beispieldaten (Ultra avancé)
- Siehe `fixtures.py`: multilinguale, multitenant, RGPD-ready, anonymisierte, a11y-konforme, plugin-fähige Demo-Datensätze für alle Kernmodelle und Tenants/Sprachen.
- Automatische Generierung für alle Modelle (Chantier, Ouvrier, Rapport) und alle Tenants/Sprachen.

---

## 🛠️ Exemples d’API BTP

### Création d’un projet BTP

```http
POST /api/btp/projets/
Authorization: Bearer <token>
Content-Type: application/json

{
  "nom": "Chantier Amazigh",
  "localisation": "Alger",
  "date_debut": "2025-06-01",
  "chef_projet_id": 7
}
```

### Ajout d’un incident de chantier

```http
POST /api/btp/incidents/
Authorization: Bearer <token>
Content-Type: application/json

{
  "projet_id": 1,
  "description": "Incident sécurité mineur",
  "date": "2025-06-02"
}
```

### Génération d’un rapport de chantier

```http
GET /api/btp/rapports/?projet_id=1
Authorization: Bearer <token>
Accept: application/json
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export) aux rôles autorisés
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
- [API BTP (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – BTP souverain, extensible, multilingue, prêt pour la production, la démo et la contribution.

---
