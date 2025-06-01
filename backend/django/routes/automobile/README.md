# Dihya Backend Django – API Automobile

---

## 🇫🇷 Français
Ce module expose une API automobile Django complète, sécurisée, modulaire et multilingue pour la plateforme Dihya :
- **Endpoints** : véhicules, modèles, marques, maintenance, logs, audit, IA, plugins
- **Sécurité** : JWT, RBAC, CORS, CSP, audit logging, conformité RGPD/NIS2
- **Extensibilité** : hooks plugins, templates métiers, import/export, marketplace
- **Accessibilité** : API REST, OpenAPI, multilingue (fr, en, ar, amazigh)
- **Souveraineté** : logs anonymisés, fallback open source, AGPL
- **Tests** : unitaires, intégration, e2e, accessibilité, sécurité, i18n
- **Exemples** : voir ci-dessous pour usage Python/JS/cURL/Postman

## 🇬🇧 English
This module provides a full-featured, secure, modular, multilingual Django automobile API for Dihya platform:
- **Endpoints**: vehicles, models, brands, maintenance, logs, audit, AI, plugins
- **Security**: JWT, RBAC, CORS, CSP, audit logging, GDPR/NIS2 compliance
- **Extensibility**: plugin hooks, business templates, import/export, marketplace
- **Accessibility**: REST API, OpenAPI, multilingual (fr, en, ar, amazigh)
- **Sovereignty**: anonymized logs, open source fallback, AGPL
- **Tests**: unit, integration, e2e, accessibility, security, i18n
- **Examples**: see below for Python/JS/cURL/Postman usage

## 🇦🇪 العربية
هذه الوحدة توفر واجهة برمجة تطبيقات سيارات كاملة وآمنة وقابلة للتوسعة ومتعددة اللغات لمنصة ديهيا:
- **النقاط**: المركبات، النماذج، العلامات التجارية، الصيانة، السجلات، التدقيق، الذكاء الاصطناعي، الإضافات
- **الأمان**: JWT، RBAC، CORS، CSP، تدقيق السجلات، توافق RGPD/NIS2
- **الامتداد**: ربط الإضافات، قوالب الأعمال، الاستيراد/التصدير، السوق
- **إتاحة**: REST API، OpenAPI، متعدد اللغات (فر، إنج، عرب، أمازيغ)
- **السيادة**: سجلات مجهولة، بدائل مفتوحة المصدر، AGPL
- **الاختبارات**: وحدة، تكامل، e2e، وصول، أمان، i18n
- **أمثلة**: انظر أدناه لاستخدام Python/JS/cURL/Postman

## ⴰⵎⴰⵣⵉⵖ (Amazigh)
Aneɣru agi d API n automobile, tazult, tazwart, multilingual i Dihya:
- **Endpoints**: vehicles, models, brands, maintenance, logs, audit, IA, plugins
- **Tazult**: JWT, RBAC, CORS, CSP, audit, GDPR/NIS2
- **Extension**: hooks plugins, templates, import/export, marketplace
- **Tazult**: REST API, OpenAPI, multilingual (fr, en, ar, amz)
- **Tazult**: logs anonymisés, fallback open source, AGPL
- **Tests**: unit, integration, e2e, a11y, security, i18n
- **Amedya**: wali d amedya s Python/JS/cURL/Postman

---

## Endpoints principaux
- `/api/v1/automobile/vehicules/` : gestion des véhicules
- `/api/v1/automobile/modeles/` : gestion des modèles
- `/api/v1/automobile/marques/` : gestion des marques
- `/api/v1/automobile/maintenance/` : gestion de la maintenance
- `/api/v1/automobile/ia/` : IA automobile souveraine
- `/api/v1/automobile/audit/logs/` : audit logging

## Sécurité & conformité
- Authentification JWT, gestion des rôles (admin, user, guest)
- CORS, CSP, rate limiting, audit logging souverain, anonymisation
- RGPD/NIS2, logs effaçables, consentement utilisateur simulé pour tests
- Fallback open source si API externe indisponible

## Extensibilité & plugins
- Ajout dynamique de plugins (diagnostic, IA, CMS…)
- Import/export de templates métiers
- Marketplace automobile Dihya

## Exemples d’usage

### Python (requests)
```python
import requests
r = requests.get('https://dihya.app/api/v1/automobile/vehicules/', headers={'Authorization': 'Bearer <token>'})
print(r.json())
```

### JavaScript (fetch)
```js
fetch('/api/v1/automobile/vehicules/', { headers: { Authorization: 'Bearer <token>' } })
  .then(r => r.json()).then(console.log)
```

### cURL
```bash
curl -H "Authorization: Bearer <token>" https://dihya.app/api/v1/automobile/vehicules/
```

### Postman
- Importer l’endpoint `/api/v1/automobile/vehicules/` et ajouter le header JWT

## Tests & auditabilité
- Tests unitaires, intégration, e2e, accessibilité, sécurité, i18n (voir dossier tests/)
- Audit logging souverain, logs anonymisés, conformité AGPL
- Exemples de tests dans `tests/automobile/`

## Contribution & extension
- Fork, PR, plugins, templates, traduction, guides multilingues
- Voir CONTRIBUTING.md, PLUGINS_GUIDE.md, API_REFERENCE_*.md

---

© 2025 Dihya Coding – AGPL, souveraineté numérique, multilingue, open source, extensible, prêt à l’emploi.
