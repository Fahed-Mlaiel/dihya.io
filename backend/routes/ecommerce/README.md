# Dihya Backend – API E-commerce

---

## 🇫🇷 Français

Ce module expose une API e-commerce complète, sécurisée, modulaire et multilingue pour la plateforme Dihya :
- **Endpoints** : gestion produits, panier, paiement, plugins, fallback IA, OpenAPI
- **Sécurité** : JWT, RBAC, CORS, CSP, audit logging, conformité RGPD
- **Extensibilité** : hooks plugins, templates métiers, import/export, marketplace
- **Accessibilité** : API REST, OpenAPI, multilingue (fr, en, ar, amazigh)
- **Souveraineté** : logs anonymisés, fallback open source, AGPL
- **Tests** : unitaires, intégration, e2e, accessibilité, sécurité, i18n
- **Exemples** : voir ci-dessous pour usage Python/JS/cURL/Postman

## 🇬🇧 English

This module provides a full-featured, secure, modular, multilingual e-commerce API for Dihya platform:
- **Endpoints**: products, cart, payment, plugins, fallback AI, OpenAPI
- **Security**: JWT, RBAC, CORS, CSP, audit logging, GDPR compliance
- **Extensibility**: plugin hooks, business templates, import/export, marketplace
- **Accessibility**: REST API, OpenAPI, multilingual (fr, en, ar, amazigh)
- **Sovereignty**: anonymized logs, open source fallback, AGPL
- **Tests**: unit, integration, e2e, accessibility, security, i18n
- **Examples**: see below for Python/JS/cURL/Postman usage

## 🇦🇪 العربية

هذه الوحدة توفر واجهة برمجة تطبيقات تجارة إلكترونية كاملة وآمنة وقابلة للتوسعة ومتعددة اللغات لمنصة ديهيا:
- **النقاط**: المنتجات، السلة، الدفع، الإضافات، الذكاء الاصطناعي الاحتياطي، OpenAPI
- **الأمان**: JWT، RBAC، CORS، CSP، تدقيق السجلات، توافق RGPD
- **الامتداد**: ربط الإضافات، قوالب الأعمال، الاستيراد/التصدير، السوق
- **إتاحة**: REST API، OpenAPI، متعدد اللغات (فر، إنج، عرب، أمازيغ)
- **السيادة**: سجلات مجهولة، بدائل مفتوحة المصدر، AGPL
- **الاختبارات**: وحدة، تكامل، e2e، وصول، أمان، i18n
- **أمثلة**: انظر أدناه لاستخدام Python/JS/cURL/Postman

## ⴰⵎⴰⵣⵉⵖ (Amazigh)

Aneɣru agi d API n tzemre n e-commerce, tazult, tazwart, multilingual i Dihya:
- **Endpoints**: tzemre, tkarḍa, tazwart, plugins, fallback IA, OpenAPI
- **Tazult**: JWT, RBAC, CORS, CSP, audit, GDPR
- **Extension**: hooks plugins, templates, import/export, marketplace
- **Tazult**: REST API, OpenAPI, multilingual (fr, en, ar, amz)
- **Tazult**: logs anonymisés, fallback open source, AGPL
- **Tests**: unit, integration, e2e, a11y, security, i18n
- **Amedya**: wali d amedya s Python/JS/cURL/Postman

---

## Endpoints principaux
- `POST /api/ecommerce/products` : créer un produit (admin)
- `GET /api/ecommerce/products` : lister les produits
- `POST /api/ecommerce/cart` : ajouter au panier
- `POST /api/ecommerce/checkout` : initier un paiement
- `GET /api/ecommerce/plugins` : plugins e-commerce actifs
- `POST /api/ecommerce/fallback` : fallback IA open source
- `GET /api/ecommerce/openapi` : spec OpenAPI dynamique

## Sécurité & conformité
- Authentification JWT, gestion des rôles (admin, user, guest)
- CORS, CSP, rate limiting, audit logging souverain, anonymisation
- RGPD, logs effaçables, consentement utilisateur simulé pour tests
- Fallback open source si API externe indisponible

## Extensibilité & plugins
- Ajout dynamique de plugins (paiement, analytics, CMS, IA…)
- Import/export de templates métiers
- Marketplace e-commerce Dihya

## Exemples d’usage

### Python (requests)
```python
import requests
r = requests.get('https://dihya.app/api/ecommerce/products', headers={'Authorization': 'Bearer <token>'})
print(r.json())
```

### JavaScript (fetch)
```js
fetch('/api/ecommerce/products', { headers: { Authorization: 'Bearer <token>' } })
  .then(r => r.json()).then(console.log)
```

### cURL
```bash
curl -H "Authorization: Bearer <token>" https://dihya.app/api/ecommerce/products
```

### Postman
- Importer l’endpoint `/api/ecommerce/products` et ajouter le header JWT

## Tests & auditabilité
- Tests unitaires, intégration, e2e, accessibilité, sécurité, i18n (voir dossier tests/)
- Audit logging souverain, logs anonymisés, conformité AGPL
- Exemples de tests dans `tests/ecommerce/`

## Contribution & extension
- Fork, PR, plugins, templates, traduction, guides multilingues
- Voir CONTRIBUTING.md, PLUGINS_GUIDE.md, API_REFERENCE_*.md

---

© 2025 Dihya Coding – AGPL, souveraineté numérique, multilingue, open source, extensible, prêt à l’emploi.
