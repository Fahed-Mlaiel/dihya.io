# 🎡 Dihya – Django Loisirs API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/loisirs`](#rôle-du-dossier-routesloisirs)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API loisirs](#exemples-dapi-loisirs)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🎡 Rôle du dossier `routes/loisirs`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, l’innovation et la valorisation des activités de loisirs via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration plateformes loisirs, cloud souverain, IA recommandation
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST loisirs** : gestion des activités, événements, réservations, lieux, participants, avis, promotions, IA recommandation
- **Gestion des droits d’accès** : RBAC (admin, organisateur, participant, auditeur, guest)
- **Traçabilité et logs** : audit des accès, réservations, participations, suppressions, exports
- **Interopérabilité** : intégration avec plateformes loisirs, open data, webhooks, partenaires
- **Automatisation** : notifications, rappels, génération de recommandations IA, gestion des disponibilités, promotions dynamiques
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
loisirs/
├── views.py           # Vues Django REST pour activités, événements, réservations, lieux, participants, avis
├── serializers.py     # Serializers pour activités, événements, réservations, lieux, participants, avis
├── urls.py            # Routage des endpoints loisirs
├── permissions.py     # Permissions RBAC pour l’accès aux services loisirs
├── tasks.py           # Tâches asynchrones (notifications, IA, gestion disponibilités)
├── assets/            # Exemples d’activités, images, modèles IA, promotions
├── tests/             # Tests unitaires et d’intégration API loisirs
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, organisateur, participant, guest)
- **Logs d’accès** et d’opérations critiques (création, réservation, participation, suppression)
- **Chiffrement** des données sensibles (réservations, identités, avis)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque réservation ou asset loisirs

---

## 🛠️ Exemples d’API loisirs

### Création d’une activité

```http
POST /api/loisirs/activites/
Authorization: Bearer <token>
Content-Type: application/json

{
  "nom": "Randonnée Amazigh",
  "lieu": "Kabylie",
  "date": "2025-08-15",
  "places": 20
}
```

### Réservation d’une activité

```http
POST /api/loisirs/reservations/
Authorization: Bearer <token>
Content-Type: application/json

{
  "participant_id": 7,
  "activite_id": 3
}
```

### Ajout d’un avis

```http
POST /api/loisirs/avis/
Authorization: Bearer <token>
Content-Type: application/json

{
  "activite_id": 3,
  "participant_id": 7,
  "note": 5,
  "commentaire": "Expérience inoubliable !"
}
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, réservation) aux rôles autorisés
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
- [API Loisirs (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Loisirs souverains, extensibles, multilingues, prêts pour la production, la démo et la contribution.

---
