# 🌍 Dihya – Django Social API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/social`](#rôle-du-dossier-routessocial)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API social](#exemples-dapi-social)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🌍 Rôle du dossier `routes/social`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, l’innovation et la valorisation des interactions sociales via l’API Django Dihya.

- **Multi-stack** : Django REST, plugins Python/Node, intégration réseaux sociaux, cloud souverain, IA social, gestion profils, posts, commentaires, notifications, modération
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, chiffrement, anonymisation, modération IA
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST social** : gestion des profils, posts, commentaires, likes, partages, abonnements, notifications, IA social, modération, rapports
- **Gestion des droits d’accès** : RBAC (admin, modérateur, utilisateur, guest, auditeur)
- **Traçabilité et logs** : audit des accès, posts, modifications, suppressions, exports
- **Interopérabilité** : intégration avec réseaux sociaux, open data, webhooks, partenaires
- **Automatisation** : notifications, alertes, génération de rapports, IA recommandation, modération dynamique
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
social/
├── views.py           # Vues Django REST pour profils, posts, commentaires, likes, partages, abonnements, notifications, IA social
├── serializers.py     # Serializers pour profils, posts, commentaires, likes, partages, abonnements, notifications, IA social
├── urls.py            # Routage des endpoints social
├── permissions.py     # Permissions RBAC pour l’accès aux services social
├── tasks.py           # Tâches asynchrones (notifications, IA, génération rapports, modération)
├── assets/            # Exemples de posts, modèles IA, rapports, templates
├── tests/             # Tests unitaires et d’intégration API social
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, modérateur, utilisateur, guest)
- **Logs d’accès** et d’opérations critiques (création, modification, suppression, modération)
- **Chiffrement** des données sensibles (profils, posts, commentaires, identités)
- **Anonymisation** des données dans les exports et logs
- **Modération IA** et fallback open source pour la détection de contenus inappropriés
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité, consentement
- **Scripts de vérification d’intégrité** pour chaque post ou asset social

---

## 🛠️ Exemples d’API social

### Création d’un post

```http
POST /api/social/posts/
Authorization: Bearer <token>
Content-Type: application/json

{
  "utilisateur_id": 4,
  "contenu": "Bienvenue sur Dihya Social !",
  "media": null
}
```

### Ajout d’un commentaire

```http
POST /api/social/commentaires/
Authorization: Bearer <token>
Content-Type: application/json

{
  "post_id": 12,
  "utilisateur_id": 4,
  "contenu": "Bravo pour cette initiative !"
}
```

### Abonnement à un profil

```http
POST /api/social/abonnements/
Authorization: Bearer <token>
Content-Type: application/json

{
  "utilisateur_id": 4,
  "cible_id": 7
}
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, modération) aux rôles autorisés
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
- [API Social (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Social souverain, extensible, multilingue, prêt pour la production, la démo et la contribution.

---
