# Dihya Frontend – Structure des routes

Ce fichier documente la structure, la logique, la sécurité, l’accessibilité et l’extension des routes du frontend Dihya.

## FR – Français
- Routes principales : /, /login, /register, /dashboard, /projects, /plugins, /settings, /docs, /marketplace
- Sécurité : validation, RBAC, audit, logs, anonymisation, fallback
- Accessibilité : navigation clavier, ARIA, multilingue, responsive
- Extension : ajout de routes métiers, plugins, templates
- Souveraineté : fallback open source, auditabilité, logs, licence AGPL

## EN – English
- Main routes: /, /login, /register, /dashboard, /projects, /plugins, /settings, /docs, /marketplace
- Security: validation, RBAC, audit, logs, anonymization, fallback
- Accessibility: keyboard navigation, ARIA, multilingual, responsive
- Extension: add business routes, plugins, templates
- Sovereignty: open source fallback, auditability, logs, AGPL license

## AR – العربية
- المسارات الرئيسية: /، /login، /register، /dashboard، /projects، /plugins، /settings، /docs، /marketplace
- الأمان: تحقق، RBAC، تدقيق، سجلات، إخفاء الهوية، بدائل
- الوصول: تنقل لوحة المفاتيح، ARIA، تعدد لغات، استجابة
- التوسيع: إضافة مسارات مهنية، إضافات، قوالب
- السيادة: بدائل مفتوحة المصدر، تدقيق، سجلات، رخصة AGPL

## Taqbaylit (Amazigh)
- Iɣewwaṛen: /, /login, /register, /dashboard, /projects, /plugins, /settings, /docs, /marketplace
- Tazult: validation, RBAC, audit, logs, anonymisation, fallback
- Tazult: navigation clavier, ARIA, multilingual, responsive
- Extension: rnu iɣewwaṛen n umasal, plugins, templates
- Tazult: fallback open source, auditabilité, logs, licence AGPL

---

- Chaque route doit être testée (unit, integration, e2e, accessibilité, sécurité)
- Voir README.md, securite.md, tests/ pour plus de détails
