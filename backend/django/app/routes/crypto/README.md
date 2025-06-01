# 🪙 Dihya – Django Crypto API Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Rôle du dossier `routes/crypto`](#rôle-du-dossier-routescrypto)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemples d’API crypto](#exemples-dapi-crypto)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🪙 Rôle du dossier `routes/crypto`

Ce dossier regroupe tous les endpoints, vues, serializers et assets liés à la gestion, l’intégration et la valorisation des crypto-actifs via l’API Django Dihya.

- **Multi-stack** : Django REST, Web3.py, exchanges, plugins Python/Node, cloud souverain
- **Souveraineté** : aucun code propriétaire, tout est open source, versionné, auditable
- **Sécurité** : endpoints protégés, gestion des rôles, logs, conformité RGPD/NIS2, auditabilité
- **Accessibilité** : API REST multilingue, documentation claire, endpoints publics et privés

---

## 🧠 Fonctions principales

- **API REST crypto** : gestion de wallets, transactions, portefeuilles, exchanges, cotations, NFT, tokens, staking
- **Interopérabilité** : intégration multi-blockchain (Bitcoin, Ethereum, Polygon, etc.), exchanges, webhooks
- **Gestion des droits d’accès** : RBAC (admin, opérateur, utilisateur, auditeur, guest)
- **Traçabilité et logs** : audit des accès, transactions, échanges, suppressions, exports
- **Automatisation** : génération de wallets, signatures, notifications, vérification de preuve, alertes de prix
- **Extensibilité** : ajout facile de nouveaux modules, endpoints, plugins, IA

---

## 📁 Structure recommandée

```
crypto/
├── views.py           # Vues Django REST pour wallets, transactions, exchanges, NFT, tokens
├── serializers.py     # Serializers pour wallets, transactions, exchanges, NFT, tokens
├── urls.py            # Routage des endpoints crypto
├── permissions.py     # Permissions RBAC pour l’accès aux services crypto
├── tasks.py           # Tâches asynchrones (notifications, génération, vérification, alertes)
├── assets/            # Exemples de contrats, ABI, NFT, tokens, historiques de prix
├── tests/             # Tests unitaires et d’intégration API crypto
└── README.md          # Ce fichier (documentation multilingue)
```

---

## 🔒 Sécurité & conformité

- **Endpoints protégés** par authentification JWT et RBAC (admin, opérateur, utilisateur, guest)
- **Logs d’accès** et d’opérations critiques (création, transaction, suppression, échange)
- **Chiffrement** des clés privées et données sensibles (AES-256, vault, HSM)
- **Anonymisation** des données dans les exports et logs
- **Conformité RGPD/NIS2** : suppression sur demande, export, auditabilité
- **Scripts de vérification d’intégrité** pour chaque transaction ou asset crypto

---

## 🔒 Policies & RBAC/ABAC/PBAC (Ultra avancé)
- Siehe `policies.py`: alle Aktionen (Erstellung, Ansicht, Export, Audit, RGPD, Plugins, Multitenant, Accessibility, Fallback) sind fein granuliert, auditierbar, erweiterbar, multilingue.
- Helper `has_policy(role, action)` für Plugins, Audit, CI/CD, dynamische Erweiterung.

## 🧩 Plugins (Ultra avancé)
- Siehe `plugins.py`: dynamische Verwaltung, Audit, RGPD, Multilingue, Accessibility, Fallback, Multitenant, CI/CD-ready.
- Beispiel: Crypto-Wallet-Plugin, Beschreibung in 4 Sprachen, Audit, einfache Erweiterung.

## 🧪 Fixtures & Beispieldaten (Ultra avancé)
- Siehe `fixtures.py`: multilinguale, multitenant, RGPD-ready, anonymisierte, a11y-konforme, plugin-fähige Demo-Datensätze für alle Kernmodelle und Tenants/Sprachen.
- Automatische Generierung für alle Modelle (Wallet, Transaction, Audit) und alle Tenants/Sprachen.

---

## 🛠️ Exemples d’API crypto

### Création d’un wallet

```http
POST /api/crypto/wallets/
Authorization: Bearer <token>
Content-Type: application/json

{
  "type": "bitcoin"
}
```

### Envoi d’une transaction

```http
POST /api/crypto/transactions/send/
Authorization: Bearer <token>
Content-Type: application/json

{
  "wallet_id": 1,
  "to": "bc1qxyz...",
  "amount": 0.01,
  "token": "BTC"
}
```

### Récupération de la cotation d’un token

```http
GET /api/crypto/tokens/BTC/price/
Authorization: Bearer <token>
Accept: application/json
```

---

## 📝 Bonnes pratiques

- **Documenter chaque endpoint** (usage, arguments, formats supportés, sécurité)
- **Traduire** tous les messages d’erreur et de succès (fr, en, ar, tzm)
- **Automatiser** les tests (unit, integration, e2e) pour chaque route critique
- **Limiter l’accès** aux fonctions sensibles (création, suppression, export, transaction) aux rôles autorisés
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
- [API Crypto (OpenAPI)](../../../../docs/openapi.yaml)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)
- [Webhooks](../../../../WEBHOOKS_GUIDE.md)

---

**Dihya Coding** – Crypto souveraine, extensible, multilingue, prête pour la production, la démo et la contribution.

---
