# 👗 Dihya Mode Module – Politique d’Utilisation / Usage Policy / سياسة الاستخدام / ⴰⵙⵏⴼⴰⵡ ⵏ ⵎⵓⴷ

---

## 🇫🇷 Politique d’Utilisation

Ce dossier contient les templates du module "mode" (gestion de collections, lookbooks, tendances, e-commerce mode, etc.) de Dihya.
**Respect des règles :**
- **Sécurité** : Aucune donnée personnelle, information sensible, ou secret mode ne doit être exposé dans les templates.
- **Accessibilité** : Tous les templates doivent respecter le RGAA/WCAG (lang, contrastes, navigation clavier/tactile, ARIA, responsive).
- **Internationalisation** : Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- **Souveraineté numérique & RGPD** : Aucun appel à des ressources externes non souveraines (CDN, analytics tiers, etc.), conformité RGPD, mentions légales obligatoires, e-commerce souverain uniquement.
- **Confidentialité** : Pas de tracking tiers, pas de cookies tiers, respect de la vie privée des utilisateurs et des droits images.
- **Rôles** : Les templates doivent intégrer la gestion des rôles utilisateur (client, styliste, admin, invité…).
- **SEO** : Balises meta, titres, descriptions, données structurées obligatoires.
- **Tests** : Chaque template doit être couvert par des tests d’accessibilité, de rendu et de conformité mode.
- **Droits d’auteur** : Respect absolu des droits d’auteur et licences images/mode.

---

## 🇬🇧 Usage Policy

This folder contains the "mode" module templates for Dihya (collections management, lookbooks, trends, fashion e-commerce, etc.).
**Rules:**
- **Security**: No personal data, sensitive info, or fashion secrets must be exposed in templates.
- **Accessibility**: All templates must comply with RGAA/WCAG (lang, contrast, keyboard/touch nav, ARIA, responsive).
- **Internationalization**: Use `{% trans %}` or `{% blocktrans %}` for all displayed text.
- **Digital Sovereignty & GDPR**: No calls to non-sovereign external resources (CDN, third-party analytics, etc.), GDPR compliance, legal notices required, only sovereign e-commerce.
- **Privacy**: No third-party tracking, no third-party cookies, user and image rights privacy respected.
- **Roles**: Templates must integrate user role management (customer, stylist, admin, guest…).
- **SEO**: Meta tags, titles, descriptions, structured data are mandatory.
- **Tests**: Each template must be covered by accessibility, rendering, and fashion compliance tests.
- **Copyright**: Absolute respect for copyright and image/fashion licenses.

---

## 🇦🇪 سياسة الاستخدام

يحتوي هذا المجلد على قوالب وحدة "الموضة" في ديهيا (إدارة المجموعات، لوك بوك، اتجاهات، تجارة إلكترونية للموضة...).
**القواعد:**
- **الأمان**: لا يجوز كشف أي بيانات شخصية أو معلومات حساسة أو أسرار موضة في القوالب.
- **إمكانية الوصول**: يجب أن تتوافق جميع القوالب مع معايير الوصول (RGAA/WCAG)، دعم لوحة المفاتيح/اللمس، ARIA، استجابة التصميم.
- **تعدد اللغات**: استخدم `{% trans %}` أو `{% blocktrans %}` لكل النصوص.
- **السيادة الرقمية والتوافق مع RGPD**: لا تستخدم موارد خارجية غير سيادية، توافق RGPD، وجوب وجود إشعارات قانونية، تجارة إلكترونية سيادية فقط.
- **الخصوصية**: لا تتبع المستخدمين، لا كوكيز لطرف ثالث، احترام خصوصية المستخدمين وحقوق الصور.
- **الأدوار**: يجب أن تدعم القوالب إدارة الأدوار (عميل، مصمم، مشرف، زائر...).
- **تحسين محركات البحث**: يجب تضمين وسوم meta والعناوين والوصف وبيانات منظمة.
- **الاختبارات**: يجب تغطية كل قالب باختبارات وصول وعرض وتوافق موضة.
- **حقوق النشر**: احترام مطلق لحقوق النشر ورخص الصور/الموضة.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n uγmis "mode" n Dihya (tawuri n tikkelt, lookbook, trends, e-commerce n mode...).
**Imiḍan:**
- **Taɣult**: Ulac isefka ur nelli d asensi, isefka uslig, neɣ asensi n mode deg templates.
- **Tawuri**: Akk templates ilaq ad s-d-yerrun i RGAA/WCAG, tawuri n tneflit, ARIA, responsive.
- **Tamyizt**: Seqdec `{% trans %}` neɣ `{% blocktrans %}` i yal awal.
- **Aseggas n tmedyazt & RGPD**: Ulac tazwara d isemlal ur nelli d n tmurt, RGPD ilaq ad yili, tazwart n taseddast ilaq ad tili, e-commerce n tmurt kan.
- **Tawuri n wudem**: Ulac tracking n uzzay, ulac cookies n uzzay, uslig n uclay d images yettwaselkem.
- **Isemnisen**: Templates ilaq ad s-d-yerrun i uselkim n wudem (client, stylist, admin, azay...).
- **SEO**: Meta, title, description, tags.
- **Imtihanen**: Yal template ilaq ad yili deg imtihanen n tawuri, uskan, d tawaḍit n mode.
- **Azref n tazwart**: Asirem n tazwart d izerfan n images/mode ilaq ad yili.

---

## ✅ Exemples de conformité / Compliance Examples

- **Sécurité** :
  ```html
  <!-- Ne jamais afficher d’information mode confidentielle ou de donnée personnelle : -->
  <!-- {{ mode.secret_collection }} ❌ -->
  ```
- **Accessibilité** :
  ```html
  <html lang="fr"> <!-- Obligatoire -->
  <img src="{% static 'mode/robe.jpg' %}" alt="{% trans 'Robe tendance' %}" />
  ```
- **i18n** :
  ```django
  <h1>{% trans "Nouvelles tendances mode" %}</h1>
  ```
- **SEO** :
  ```html
  <meta name="description" content="{% trans 'Boutique mode souveraine, conforme RGPD et sécurisée' %}">
  ```

---

## 🔒 Contrôle & Audit

- **CI/CD** : Les templates sont vérifiés automatiquement à chaque push (lint, accessibilité, i18n, sécurité, conformité mode).
- **Audit** : Toute modification doit être revue par un mainteneur référent.
- **Logs** : Les accès aux templates sont journalisés côté serveur (audit trail).

---

## 🤝 Contribution

- Respectez cette politique pour toute contribution.
- Toute PR non conforme sera refusée.

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, conformité mode, excellence.
