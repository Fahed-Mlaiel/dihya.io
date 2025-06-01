# 💄 Dihya – Django Beauté API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/beaute`](#rôle-du-dossier-routesbeaute)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API beauté](#exemples-dapi-beaute)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 💄 Rôle du dossier `routes/beaute`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, la création, la réservation et la valorisation des services et produits de beauté via l’API Django Dihya.

- **Multi-stack** : Django REST, IA recommandation, plugins Python/Node, cloud souverain, intégration e-commerce
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST beauté** : gestion des salons, prestations, produits, réservations, avis, IA recommandation
- **Gestion des droits d’accès** : RBAC (admin, professionnel, client, auditeur, guest)
- **Traçabilité et logs** : audit des accès, créations, modifications, suppressions, exports
- **Interopérabilité** : intégration avec plateformes beauté, e-commerce, open data, webhooks
- **Automatisation** : notifications, rappels, génération de recommandations IA, badges fidélité
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
beaute/
├── views.py           # Vues Django REST pour les salons, prestations, produits, réservations
├── serializers.py     # Serializers pour salons, prestations, produits, avis, réservations
├── urls.py            # Routage des endpoints beauté
├── permissions.py     # Permissions RBAC pour l’accès aux services beauté
├── tasks.py           # Tâches asynchrones (notifications, IA, rappels)
├── assets/            # Exemples de produits, images, modèles IA
├── tests/             # Tests unitaires et d’intégration API beauté
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, professionnel, client, guest)
- **Logs d’accès** et d’opérations critiques (création, modification, suppression)
- **Anonymisation** des données sensibles dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque donnée ou asset beauté

---

## 🔒 Policies & RBAC/ABAC/PBAC (Ultra avancé)
- Siehe `policies.py`: alle Aktionen (Erstellung, Ansicht, Export, Audit, RGPD, Plugins, Multitenant, Accessibility, Fallback) sind fein granuliert, auditierbar, erweiterbar, multilingue.
- Helper `has_policy(role, action)` für Plugins, Audit, CI/CD, dynamische Erweiterung.

## 🧩 Plugins (Ultra avancé)
- Siehe `plugins.py`: dynamische Verwaltung, Audit, RGPD, Multilingue, Accessibility, Fallback, Multitenant, CI/CD-ready.
- Beispiel: Plugin für Beauty-AI-Empfehlungen, Beschreibung in 4 Sprachen, Audit, einfache Erweiterung.

## 🧪 Fixtures & Beispieldaten (Ultra avancé)
- Siehe `fixtures.py`: multilinguale, multitenant, RGPD-ready, anonymisierte, a11y-konforme, plugin-fähige Demo-Datensätze für alle Kernmodelle und Tenants/Sprachen.
- Automatische Generierung für alle Modelle (Salon, Prestation, Produit) und alle Tenants/Sprachen.

---

## 🛠️ Exemples d’API beauté

### Création d’un salon de beauté

```http
POST /api/beaute/salons/
Authorization: Bearer <token>
Content-Type: application/json

{
  "nom": "Salon Demo",
  "adresse": "123 avenue de la Beauté",
  "telephone": "+213123456789"
}
```

### Réservation d’une prestation

```http
POST /api/beaute/reservations/
Authorization: Bearer <token>
Content-Type: application/json

{
  "salon_id": 1,
  "prestation_id": 2,
  "client_id": 7,
  "date": "2025-06-01T14:00:00"
}
```

### Ajout d’un avis client

```http
POST /api/beaute/avis/
Authorization: Bearer <token>
Content-Type: application/json

{
  "salon_id": 1,
  "client_id": 7,
  "note": 5,
  "commentaire": "Service exceptionnel !"
}
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
- [API Beauté (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Beauté souveraine, extensible, multilingue, prête pour la production, la démo et la contribution.

---
