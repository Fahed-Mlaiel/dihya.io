# 📢 Dihya – Django Publicité API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/publicite`](#rôle-du-dossier-routespublicite)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API publicité](#exemples-dapi-publicité)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 📢 Rôle du dossier `routes/publicite`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, la diffusion et l’innovation publicitaire via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration DSP/SSP, cloud souverain, IA publicité, analytics, automation
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement, modération IA
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST publicité** : gestion des campagnes, annonces, emplacements, audiences, budgets, analytics, IA publicité, A/B testing, notifications, rapports
- **Gestion des droits d’accès** : RBAC (admin, annonceur, régie, analyste, auditeur, guest)
- **Traçabilité et logs** : audit des accès, campagnes, modifications, suppressions, exports
- **Interopérabilité** : intégration avec DSP, SSP, CRM, plateformes médias, open data, webhooks, partenaires
- **Automatisation** : notifications, alertes, génération de rapports, IA recommandation, scoring, modération dynamique
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
publicite/
├── views.py           # Vues Django REST pour campagnes, annonces, emplacements, audiences, budgets, analytics, rapports
├── serializers.py     # Serializers pour campagnes, annonces, emplacements, audiences, budgets, analytics, rapports
├── urls.py            # Routage des endpoints publicité
├── permissions.py     # Permissions RBAC pour l’accès aux services publicité
├── tasks.py           # Tâches asynchrones (notifications, IA, génération rapports, modération)
├── assets/            # Exemples de campagnes, annonces, modèles IA, rapports, templates
├── tests/             # Tests unitaires et d’intégration API publicité
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, annonceur, régie, analyste, guest)
- **Logs d’accès** et d’opérations critiques (création, campagne, suppression)
- **Chiffrement** des données sensibles (budgets, audiences, analytics)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque campagne ou asset publicité

---

## 🛠️ Exemples d’API publicité

### Création d’une campagne publicitaire

```http
POST /api/publicite/campagnes/
Authorization: Bearer <token>
Content-Type: application/json

{
  "nom": "Campagne Printemps 2025",
  "budget": 5000,
  "audience_id": 3,
  "debut": "2025-03-01",
  "fin": "2025-04-01"
}
```

### Ajout d’une annonce

```http
POST /api/publicite/annonces/
Authorization: Bearer <token>
Content-Type: application/json

{
  "campagne_id": 1,
  "titre": "Nouveau produit Amazigh",
  "media_id": 12,
  "emplacement": "homepage"
}
```

### Génération d’un rapport analytics

```http
GET /api/publicite/analytics/?campagne_id=1
Authorization: Bearer <token>
Accept: application/json
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, scoring) aux rôles autorisés
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
- [API Publicité (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Publicité souveraine, extensible, multilingue, prête pour la production, la démo et la contribution.

---
