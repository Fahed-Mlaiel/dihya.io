# ✈️ Dihya – Django Voyage API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/voyage`](#rôle-du-dossier-routesvoyage)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API voyage](#exemples-dapi-voyage)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## ✈️ Rôle du dossier `routes/voyage`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, la valorisation et l’innovation du secteur voyage via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration CRM/ERP, cloud souverain, IA voyage, gestion offres, réservations, itinéraires, avis, guides, événements
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement, anonymisation
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST voyage** : gestion des offres, destinations, réservations, itinéraires, avis, guides, événements, partenaires, IA voyage, notifications, rapports
- **Gestion des droits d’accès** : RBAC (admin, agent, guide, voyageur, auditeur, guest)
- **Traçabilité et logs** : audit des accès, modifications, suppressions, exports
- **Interopérabilité** : intégration avec CRM, ERP, open data, webhooks, partenaires
- **Automatisation** : notifications, alertes, génération de rapports, IA recommandation, gestion planning, réservation dynamique
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
voyage/
├── views.py           # Vues Django REST pour offres, destinations, réservations, itinéraires, avis, guides, événements, partenaires, IA voyage
├── serializers.py     # Serializers pour offres, destinations, réservations, itinéraires, avis, guides, événements, partenaires, IA voyage
├── urls.py            # Routage des endpoints voyage
├── permissions.py     # Permissions RBAC pour l’accès aux services voyage
├── tasks.py           # Tâches asynchrones (notifications, IA, génération rapports, gestion planning)
├── assets/            # Exemples d’offres, modèles IA, rapports, templates
├── tests/             # Tests unitaires et d’intégration API voyage
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, agent, guide, voyageur, guest)
- **Logs d’accès** et d’opérations critiques (création, modification, suppression)
- **Chiffrement** des données sensibles (réservations, itinéraires, avis, identités)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque offre ou asset voyage

---

## 🛠️ Exemples d’API voyage

### Création d’une offre de voyage

```http
POST /api/voyage/offres/
Authorization: Bearer <token>
Content-Type: application/json

{
  "titre": "Circuit Sahara Découverte",
  "destination_id": 5,
  "prix": 1800,
  "date_debut": "2025-10-01",
  "date_fin": "2025-10-15"
}
```

### Réservation d’un voyage

```http
POST /api/voyage/reservations/
Authorization: Bearer <token>
Content-Type: application/json

{
  "voyageur_id": 12,
  "offre_id": 3,
  "date": "2025-10-01"
}
```

### Ajout d’un avis

```http
POST /api/voyage/avis/
Authorization: Bearer <token>
Content-Type: application/json

{
  "voyageur_id": 12,
  "offre_id": 3,
  "note": 5,
  "commentaire": "Voyage exceptionnel, organisation parfaite !"
}
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, gestion offres) aux rôles autorisés
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
- [API Voyage (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Voyage souverain, extensible, multilingue, prêt pour la production, la démo et la contribution.

---
