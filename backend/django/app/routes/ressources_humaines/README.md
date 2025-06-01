# 👥 Dihya – Django Ressources Humaines API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/ressources_humaines`](#rôle-du-dossier-routesressources_humaines)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API RH](#exemples-dapi-rh)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 👥 Rôle du dossier `routes/ressources_humaines`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion avancée des ressources humaines via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration SIRH, cloud souverain, IA RH, paie, gestion des talents
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement, anonymisation
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST RH** : gestion des employés, contrats, absences, congés, paie, recrutement, évaluations, formations, IA RH, notifications, rapports
- **Gestion des droits d’accès** : RBAC (admin, RH, manager, employé, auditeur, guest)
- **Traçabilité et logs** : audit des accès, modifications, suppressions, exports
- **Interopérabilité** : intégration avec SIRH, paie, open data, webhooks, partenaires
- **Automatisation** : notifications, alertes, génération de rapports, IA RH, gestion des talents, onboarding, offboarding
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
ressources_humaines/
├── views.py           # Vues Django REST pour employés, contrats, absences, congés, paie, recrutement, évaluations, formations
├── serializers.py     # Serializers pour employés, contrats, absences, congés, paie, recrutement, évaluations, formations
├── urls.py            # Routage des endpoints RH
├── permissions.py     # Permissions RBAC pour l’accès aux services RH
├── tasks.py           # Tâches asynchrones (notifications, IA, génération rapports, onboarding)
├── assets/            # Exemples de contrats, modèles IA, rapports, templates
├── tests/             # Tests unitaires et d’intégration API RH
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, RH, manager, employé, guest)
- **Logs d’accès** et d’opérations critiques (création, modification, suppression)
- **Chiffrement** des données sensibles (contrats, paie, identités)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque contrat ou asset RH

---

## 🛠️ Exemples d’API RH

### Création d’un employé

```http
POST /api/ressources_humaines/employes/
Authorization: Bearer <token>
Content-Type: application/json

{
  "nom": "Amel",
  "prenom": "Yahia",
  "email": "amel.yahia@example.com",
  "poste": "Développeur IA"
}
```

### Demande de congé

```http
POST /api/ressources_humaines/conges/
Authorization: Bearer <token>
Content-Type: application/json

{
  "employe_id": 5,
  "date_debut": "2025-08-01",
  "date_fin": "2025-08-15",
  "motif": "Vacances"
}
```

### Génération d’un bulletin de paie

```http
GET /api/ressources_humaines/paie/?employe_id=5
Authorization: Bearer <token>
Accept: application/pdf
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, paie) aux rôles autorisés
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
- [API RH (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – RH souveraines, extensibles, multilingues, prêtes pour la production, la démo et la contribution.

---
