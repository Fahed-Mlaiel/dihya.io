# 🩺 Dihya – Django Health API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/health`](#rôle-du-dossier-routeshealth)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API santé](#exemples-dapi-santé)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🩺 Rôle du dossier `routes/health`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, l’innovation et la valorisation des services de santé via l’API Django Dihya.

- **Multi-stack** : Django REST, FHIR, plugins Python/Node, cloud souverain, IA santé
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST santé** : gestion des patients, dossiers médicaux, rendez-vous, praticiens, prescriptions, analyses, IA santé
- **Interopérabilité** : intégration FHIR, HL7, open data, webhooks, partenaires santé
- **Gestion des droits d’accès** : RBAC (admin, médecin, infirmier, patient, auditeur, guest)
- **Traçabilité et logs** : audit des accès, modifications, suppressions, exports
- **Automatisation** : notifications, rappels, génération de rapports, IA diagnostic, suivi patient
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
health/
├── views.py           # Vues Django REST pour patients, dossiers, rendez-vous, praticiens, prescriptions, analyses
├── serializers.py     # Serializers pour patients, dossiers, rendez-vous, praticiens, prescriptions, analyses
├── urls.py            # Routage des endpoints santé
├── permissions.py     # Permissions RBAC pour l’accès aux services santé
├── tasks.py           # Tâches asynchrones (notifications, IA, génération rapports)
├── assets/            # Exemples de dossiers, modèles IA, rapports, open data
├── tests/             # Tests unitaires et d’intégration API santé
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, médecin, infirmier, patient, guest)
- **Logs d’accès** et d’opérations critiques (création, modification, suppression)
- **Chiffrement** des données sensibles (dossiers, prescriptions, identités)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque donnée ou asset santé

---

## 🛠️ Exemples d’API santé

### Création d’un patient

```http
POST /api/health/patients/
Authorization: Bearer <token>
Content-Type: application/json

{
  "nom": "Amina",
  "prenom": "Yahia",
  "date_naissance": "1990-05-12",
  "sexe": "F"
}
```

### Prise de rendez-vous

```http
POST /api/health/rendezvous/
Authorization: Bearer <token>
Content-Type: application/json

{
  "patient_id": 7,
  "praticien_id": 3,
  "date": "2025-06-10T09:00:00"
}
```

### Ajout d’une prescription

```http
POST /api/health/prescriptions/
Authorization: Bearer <token>
Content-Type: application/json

{
  "patient_id": 7,
  "medicament": "Paracétamol",
  "posologie": "500mg x3/j"
}
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, prescriptions) aux rôles autorisés
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
- [API Santé (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Santé souveraine, extensible, multilingue, prête pour la production, la démo et la contribution.

---
