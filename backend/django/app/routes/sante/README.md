# 🏥 Dihya – Django Santé API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/sante`](#rôle-du-dossier-routessante)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API santé](#exemples-dapi-santé)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🏥 Rôle du dossier `routes/sante`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, l’innovation et la valorisation du secteur santé via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration DMP, cloud souverain, IA santé, gestion dossiers, rendez-vous, prescriptions, télémédecine
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement, anonymisation, traçabilité médicale
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST santé** : gestion des patients, dossiers médicaux, rendez-vous, prescriptions, professionnels, établissements, IA santé, notifications, rapports
- **Gestion des droits d’accès** : RBAC (admin, médecin, infirmier, patient, auditeur, guest)
- **Traçabilité et logs** : audit des accès, modifications, suppressions, exports, accès DMP
- **Interopérabilité** : intégration avec DMP, SIH, open data, webhooks, partenaires
- **Automatisation** : notifications, alertes, génération de rapports, IA santé, gestion des rendez-vous, prescriptions électroniques
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
sante/
├── views.py           # Vues Django REST pour patients, dossiers, rendez-vous, prescriptions, professionnels, établissements, IA santé
├── serializers.py     # Serializers pour patients, dossiers, rendez-vous, prescriptions, professionnels, établissements, IA santé
├── urls.py            # Routage des endpoints santé
├── permissions.py     # Permissions RBAC pour l’accès aux services santé
├── tasks.py           # Tâches asynchrones (notifications, IA, génération rapports, gestion rendez-vous)
├── assets/            # Exemples de dossiers, modèles IA, rapports, templates
├── tests/             # Tests unitaires et d’intégration API santé
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, médecin, infirmier, patient, guest)
- **Logs d’accès** et d’opérations critiques (création, modification, suppression, accès DMP)
- **Chiffrement** des données sensibles (dossiers, prescriptions, identités)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité, consentement patient
- **Scripts de vérification d’intégrité** pour chaque dossier ou asset santé

---

## 🛠️ Exemples d’API santé

### Création d’un patient

```http
POST /api/sante/patients/
Authorization: Bearer <token>
Content-Type: application/json

{
  "nom": "Brahim",
  "prenom": "Nadia",
  "date_naissance": "1985-06-12",
  "email": "nadia.brahim@example.com"
}
```

### Prise de rendez-vous

```http
POST /api/sante/rendezvous/
Authorization: Bearer <token>
Content-Type: application/json

{
  "patient_id": 3,
  "professionnel_id": 2,
  "date": "2025-10-15T09:30:00"
}
```

### Génération d’une prescription

```http
POST /api/sante/prescriptions/
Authorization: Bearer <token>
Content-Type: application/json

{
  "patient_id": 3,
  "medecin_id": 2,
  "medicaments": [
    {"nom": "Paracétamol", "dose": "500mg", "frequence": "3x/jour"}
  ]
}
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, accès DMP) aux rôles autorisés
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
