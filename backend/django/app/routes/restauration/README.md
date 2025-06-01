# 🍽️ Dihya – Django Restauration API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/restauration`](#rôle-du-dossier-routesrestauration)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API restauration](#exemples-dapi-restauration)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🍽️ Rôle du dossier `routes/restauration`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, l’innovation et la valorisation du secteur restauration via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration POS, cloud souverain, IA restauration, gestion commandes, menus, stocks, réservations
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement, anonymisation
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST restauration** : gestion des restaurants, menus, plats, commandes, réservations, stocks, fournisseurs, avis, IA restauration, notifications, rapports
- **Gestion des droits d’accès** : RBAC (admin, chef, serveur, client, auditeur, guest)
- **Traçabilité et logs** : audit des accès, commandes, modifications, suppressions, exports
- **Interopérabilité** : intégration avec POS, ERP, open data, webhooks, partenaires
- **Automatisation** : notifications, alertes, génération de rapports, IA recommandation, gestion des stocks, promotions dynamiques
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
restauration/
├── views.py           # Vues Django REST pour restaurants, menus, plats, commandes, réservations, stocks, fournisseurs, avis
├── serializers.py     # Serializers pour restaurants, menus, plats, commandes, réservations, stocks, fournisseurs, avis
├── urls.py            # Routage des endpoints restauration
├── permissions.py     # Permissions RBAC pour l’accès aux services restauration
├── tasks.py           # Tâches asynchrones (notifications, IA, gestion stocks, génération rapports)
├── assets/            # Exemples de menus, plats, modèles IA, templates
├── tests/             # Tests unitaires et d’intégration API restauration
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, chef, serveur, client, guest)
- **Logs d’accès** et d’opérations critiques (commande, modification, suppression)
- **Chiffrement** des données sensibles (commandes, réservations, identités)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque commande ou asset restauration

---

## 🛠️ Exemples d’API restauration

### Création d’une commande

```http
POST /api/restauration/commandes/
Authorization: Bearer <token>
Content-Type: application/json

{
  "client_id": 8,
  "restaurant_id": 2,
  "plats": [
    {"plat_id": 5, "quantite": 2},
    {"plat_id": 7, "quantite": 1}
  ],
  "date": "2025-09-01T19:30:00"
}
```

### Réservation de table

```http
POST /api/restauration/reservations/
Authorization: Bearer <token>
Content-Type: application/json

{
  "client_id": 8,
  "restaurant_id": 2,
  "date": "2025-09-01T20:00:00",
  "nombre_personnes": 4
}
```

### Ajout d’un avis

```http
POST /api/restauration/avis/
Authorization: Bearer <token>
Content-Type: application/json

{
  "client_id": 8,
  "restaurant_id": 2,
  "note": 5,
  "commentaire": "Cuisine excellente, service rapide !"
}
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, gestion stocks) aux rôles autorisés
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
- [API Restauration (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Restauration souveraine, extensible, multilingue, prête pour la production, la démo et la contribution.

---
