# 🏨 Dihya – Django Hôtellerie API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/hotellerie`](#rôle-du-dossier-routeshotellerie)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API hôtellerie](#exemples-dapi-hôtellerie)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🏨 Rôle du dossier `routes/hotellerie`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, la réservation et l’innovation dans le secteur hôtelier via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration PMS, cloud souverain, IA recommandation
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST hôtellerie** : gestion des hôtels, chambres, réservations, clients, paiements, services, avis, promotions, IA recommandation
- **Gestion des droits d’accès** : RBAC (admin, réceptionniste, client, auditeur, guest)
- **Traçabilité et logs** : audit des accès, réservations, paiements, suppressions, exports
- **Interopérabilité** : intégration avec PMS, plateformes de paiement, open data, webhooks, partenaires
- **Automatisation** : notifications, rappels, génération de recommandations IA, gestion des disponibilités, promotions dynamiques
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
hotellerie/
├── views.py           # Vues Django REST pour hôtels, chambres, réservations, clients, paiements, avis
├── serializers.py     # Serializers pour hôtels, chambres, réservations, clients, paiements, avis
├── urls.py            # Routage des endpoints hôtellerie
├── permissions.py     # Permissions RBAC pour l’accès aux services hôtellerie
├── tasks.py           # Tâches asynchrones (notifications, IA, gestion disponibilités)
├── assets/            # Exemples d’hôtels, images, modèles IA, promotions
├── tests/             # Tests unitaires et d’intégration API hôtellerie
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, réceptionniste, client, guest)
- **Logs d’accès** et d’opérations critiques (création, réservation, paiement, suppression)
- **Chiffrement** des données sensibles (paiements, identités, réservations)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque réservation ou asset hôtellerie

---

## 🛠️ Exemples d’API hôtellerie

### Création d’un hôtel

```http
POST /api/hotellerie/hotels/
Authorization: Bearer <token>
Content-Type: application/json

{
  "nom": "Hôtel Amazigh",
  "adresse": "123 avenue de la Liberté",
  "etoiles": 4
}
```

### Réservation d’une chambre

```http
POST /api/hotellerie/reservations/
Authorization: Bearer <token>
Content-Type: application/json

{
  "client_id": 7,
  "chambre_id": 12,
  "date_debut": "2025-07-01",
  "date_fin": "2025-07-07"
}
```

### Paiement d’une réservation

```http
POST /api/hotellerie/paiements/
Authorization: Bearer <token>
Content-Type: application/json

{
  "reservation_id": 42,
  "methode": "carte",
  "montant": 599.99
}
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, paiement) aux rôles autorisés
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
- [API Hôtellerie (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Hôtellerie souveraine, extensible, multilingue, prête pour la production, la démo et la contribution.

---
