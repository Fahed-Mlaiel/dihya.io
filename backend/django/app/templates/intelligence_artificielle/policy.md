# 🤖 Dihya Intelligence Artificielle Module – Politique d’Utilisation / Usage Policy / سياسة الاستخدام / ⴰⵙⵏⴼⴰⵡ ⵏ ⵉⵏⵜⴻⵍⵉⴳⴻⵏⵙ ⴰⵙⵜⵉⴼⴰⵍⴰⵢ

---

## 🇫🇷 Politique d’Utilisation

Ce dossier contient les templates du module "intelligence_artificielle" de Dihya.
**Respect des règles :**
- **Sécurité** : Aucune donnée sensible, clé API, secret, ou donnée confidentielle ne doit être exposée dans les templates.
- **Accessibilité** : Tous les templates doivent respecter le RGAA/WCAG (lang, contrastes, navigation clavier, ARIA).
- **Internationalisation** : Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- **Souveraineté numérique & IA** : Aucun appel à des ressources externes non souveraines (CDN, analytics tiers, IA cloud non maîtrisée, etc.).
- **Confidentialité** : Pas de tracking, pas de cookies tiers, respect de la vie privée des utilisateurs et des données IA.
- **Rôles** : Les templates doivent intégrer la gestion des rôles utilisateur (data scientist, opérateur, client, admin, invité…).
- **SEO** : Balises meta, titres, descriptions, et balises structurées obligatoires.
- **Tests** : Chaque template doit être couvert par des tests d’accessibilité, de rendu et de conformité IA.

---

## 🇬🇧 Usage Policy

This folder contains the "intelligence_artificielle" (AI) module templates for Dihya.
**Rules:**
- **Security**: No sensitive data, API key, secret, or confidential information must be exposed in templates.
- **Accessibility**: All templates must comply with RGAA/WCAG (lang, contrast, keyboard nav, ARIA).
- **Internationalization**: Use `{% trans %}` or `{% blocktrans %}` for all displayed text.
- **Digital Sovereignty & AI**: No calls to non-sovereign external resources (CDN, third-party analytics, uncontrolled cloud AI, etc.).
- **Privacy**: No tracking, no third-party cookies, user and AI data privacy respected.
- **Roles**: Templates must integrate user role management (data scientist, operator, customer, admin, guest…).
- **SEO**: Meta tags, titles, descriptions, and structured tags are mandatory.
- **Tests**: Each template must be covered by accessibility, rendering, and AI compliance tests.

---

## 🇦🇪 سياسة الاستخدام

يحتوي هذا المجلد على قوالب وحدة "الذكاء الاصطناعي" في ديهيا.
**القواعد:**
- **الأمان**: لا يجوز كشف أي بيانات حساسة أو مفاتيح API أو أسرار أو بيانات سرية في القوالب.
- **إمكانية الوصول**: يجب أن تتوافق جميع القوالب مع معايير الوصول (RGAA/WCAG).
- **تعدد اللغات**: استخدم `{% trans %}` أو `{% blocktrans %}` لكل النصوص.
- **السيادة الرقمية والذكاء الاصطناعي**: لا تستخدم موارد خارجية غير سيادية أو ذكاء اصطناعي سحابي غير مراقب.
- **الخصوصية**: لا تتبع المستخدمين، لا كوكيز لطرف ثالث، احترام خصوصية المستخدمين وبيانات الذكاء الاصطناعي.
- **الأدوار**: يجب أن تدعم القوالب إدارة الأدوار (عالم بيانات، مشغل، عميل، مشرف، زائر...).
- **تحسين محركات البحث**: يجب تضمين وسوم meta والعناوين والوصف.
- **الاختبارات**: يجب تغطية كل قالب باختبارات وصول وعرض وتوافق ذكاء اصطناعي.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n uγmis "intelligence_artificielle" n Dihya.
**Imiḍan:**
- **Taɣult**: Ulac isefka ur nelli d asensi, api_key, secret, neɣ isefka uslig deg templates.
- **Tawuri**: Akk templates ilaq ad s-d-yerrun i RGAA/WCAG.
- **Tamyizt**: Seqdec `{% trans %}` neɣ `{% blocktrans %}` i yal awal.
- **Aseggas n tmedyazt & IA**: Ulac tazwara d isemlal ur nelli d n tmurt, ulac IA cloud ur nettwaselkem.
- **Tawuri n wudem**: Ulac tracking, ulac cookies n uzzay, uslig n uclay d isefka IA yettwaselkem.
- **Isemnisen**: Templates ilaq ad s-d-yerrun i uselkim n wudem (data scientist, amḍan, acilay, admin, azay...).
- **SEO**: Meta, title, description, tags.
- **Imtihanen**: Yal template ilaq ad yili deg imtihanen n tawuri, uskan, d tawaḍit IA.

---

## ✅ Exemples de conformité / Compliance Examples

- **Sécurité** :
  ```html
  <!-- Ne jamais afficher de clé API, secret ou donnée IA sensible : -->
  <!-- {{ ai_model.api_key }} ❌ -->
  ```
- **Accessibilité** :
  ```html
  <html lang="fr"> <!-- Obligatoire -->
  <button aria-label="{% trans 'Lancer l’analyse IA' %}"></button>
  ```
- **i18n** :
  ```django
  <h1>{% trans "Bienvenue sur la plateforme IA souveraine" %}</h1>
  ```
- **SEO** :
  ```html
  <meta name="description" content="{% trans 'Plateforme IA souveraine, éthique et sécurisée' %}">
  ```

---

## 🔒 Contrôle & Audit

- **CI/CD** : Les templates sont vérifiés automatiquement à chaque push (lint, accessibilité, i18n, sécurité, conformité IA).
- **Audit** : Toute modification doit être revue par un mainteneur référent.
- **Logs** : Les accès aux templates sont journalisés côté serveur (audit trail).

---

## 🤝 Contribution

- Respectez cette politique pour toute contribution.
- Toute PR non conforme sera refusée.

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, IA éthique, excellence.
