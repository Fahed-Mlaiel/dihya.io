# Dihya Backend – Structure des routes

Ce fichier documente la structure, la logique, la sécurité, l’accessibilité et l’extension des routes du backend Dihya.

## FR – Français
- Endpoints principaux : /api, /auth, /users, /projects, /plugins, /marketplace, /docs, /admin
- Sécurité : validation, RBAC, audit, logs, anonymisation, fallback
- Accessibilité : navigation API, multilingue, responsive
- Extension : ajout d’endpoints métiers, plugins, templates
- Souveraineté : fallback open source, auditabilité, logs, licence AGPL

## EN – English
- Main endpoints: /api, /auth, /users, /projects, /plugins, /marketplace, /docs, /admin
- Security: validation, RBAC, audit, logs, anonymization, fallback
- Accessibility: API navigation, multilingual, responsive
- Extension: add business endpoints, plugins, templates
- Sovereignty: open source fallback, auditability, logs, AGPL license

## AR – العربية
- نقاط النهاية الرئيسية: /api، /auth، /users، /projects، /plugins، /marketplace، /docs، /admin
- الأمان: تحقق، RBAC، تدقيق، سجلات، إخفاء الهوية، بدائل
- الوصول: تنقل API، تعدد لغات، استجابة
- التوسيع: إضافة نقاط نهاية مهنية، إضافات، قوالب
- السيادة: بدائل مفتوحة المصدر، تدقيق، سجلات، رخصة AGPL

## Taqbaylit (Amazigh)
- Endpoints: /api, /auth, /users, /projects, /plugins, /marketplace, /docs, /admin
- Tazult: validation, RBAC, audit, logs, anonymisation, fallback
- Tazult: navigation API, multilingual, responsive
- Extension: rnu endpoints n umasal, plugins, templates
- Tazult: fallback open source, auditabilité, logs, licence AGPL

---

- Chaque endpoint doit être testé (unit, integration, e2e, accessibilité, sécurité)
- Voir README.md, securite.md, tests/ pour plus de détails
