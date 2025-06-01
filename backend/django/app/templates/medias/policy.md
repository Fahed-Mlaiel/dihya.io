# 🎥 Dihya Medias Module – Politique d’Utilisation / Usage Policy / سياسة الاستخدام / ⴰⵙⵏⴼⴰⵡ ⵏ ⵎⴻⴷⵉⴰⵙ

---

## 🇫🇷 Politique d’Utilisation

Ce dossier contient les templates du module "medias" (gestion de médias, DAM, streaming, galerie, upload, etc.) de Dihya.
**Respect des règles :**
- **Sécurité** : Aucune donnée personnelle, information sensible, ou secret média ne doit être exposé dans les templates.
- **Accessibilité** : Tous les templates doivent respecter le RGAA/WCAG (lang, contrastes, navigation clavier, ARIA).
- **Internationalisation** : Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- **Souveraineté numérique & RGPD** : Aucun appel à des ressources externes non souveraines (CDN, analytics tiers, etc.), conformité RGPD, mentions légales obligatoires, CDN/streaming souverain uniquement.
- **Confidentialité** : Pas de tracking tiers, pas de cookies tiers, respect de la vie privée des utilisateurs et des droits médias.
- **Rôles** : Les templates doivent intégrer la gestion des rôles utilisateur (gestionnaire médias, contributeur, admin, invité…).
- **SEO** : Balises meta, titres, descriptions, et balises structurées obligatoires.
- **Tests** : Chaque template doit être couvert par des tests d’accessibilité, de rendu et de conformité médias.
- **Droits d’auteur** : Respect absolu des droits d’auteur et licences médias.

---

## 🇬🇧 Usage Policy

This folder contains the "medias" module templates for Dihya (media management, DAM, streaming, gallery, upload, etc.).
**Rules:**
- **Security**: No personal data, sensitive info, or media secrets must be exposed in templates.
- **Accessibility**: All templates must comply with RGAA/WCAG (lang, contrast, keyboard nav, ARIA).
- **Internationalization**: Use `{% trans %}` or `{% blocktrans %}` for all displayed text.
- **Digital Sovereignty & GDPR**: No calls to non-sovereign external resources (CDN, third-party analytics, etc.), GDPR compliance, legal notices required, only sovereign CDN/streaming.
- **Privacy**: No third-party tracking, no third-party cookies, user and media rights privacy respected.
- **Roles**: Templates must integrate user role management (media manager, contributor, admin, guest…).
- **SEO**: Meta tags, titles, descriptions, and structured tags are mandatory.
- **Tests**: Each template must be covered by accessibility, rendering, and media compliance tests.
- **Copyright**: Absolute respect for copyright and media licenses.

---

## 🇦🇪 سياسة الاستخدام

يحتوي هذا المجلد على قوالب وحدة "الوسائط" في ديهيا (إدارة الوسائط، البث، المعرض، التحميل...).
**القواعد:**
- **الأمان**: لا يجوز كشف أي بيانات شخصية أو معلومات حساسة أو أسرار وسائط في القوالب.
- **إمكانية الوصول**: يجب أن تتوافق جميع القوالب مع معايير الوصول (RGAA/WCAG).
- **تعدد اللغات**: استخدم `{% trans %}` أو `{% blocktrans %}` لكل النصوص.
- **السيادة الرقمية والتوافق مع RGPD**: لا تستخدم موارد خارجية غير سيادية، توافق RGPD، وجوب وجود إشعارات قانونية، CDN وبث سيادي فقط.
- **الخصوصية**: لا تتبع المستخدمين، لا كوكيز لطرف ثالث، احترام خصوصية المستخدمين وحقوق الوسائط.
- **الأدوار**: يجب أن تدعم القوالب إدارة الأدوار (مدير وسائط، مساهم، مشرف، زائر...).
- **تحسين محركات البحث**: يجب تضمين وسوم meta والعناوين والوصف.
- **الاختبارات**: يجب تغطية كل قالب باختبارات وصول وعرض وتوافق وسائط.
- **حقوق النشر**: احترام مطلق لحقوق النشر ورخص الوسائط.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n uγmis "medias" n Dihya (amedya, upload, gallery, streaming...).
**Imiḍan:**
- **Taɣult**: Ulac isefka ur nelli d asensi, isefka uslig, neɣ asensi n medias deg templates.
- **Tawuri**: Akk templates ilaq ad s-d-yerrun i RGAA/WCAG.
- **Tamyizt**: Seqdec `{% trans %}` neɣ `{% blocktrans %}` i yal awal.
- **Aseggas n tmedyazt & RGPD**: Ulac tazwara d isemlal ur nelli d n tmurt, RGPD ilaq ad yili, tazwart n taseddast ilaq ad tili, CDN/streaming n tmurt kan.
- **Tawuri n wudem**: Ulac tracking n uzzay, ulac cookies n uzzay, uslig n uclay d medias yettwaselkem.
- **Isemnisen**: Templates ilaq ad s-d-yerrun i uselkim n wudem (media manager, contributor, admin, azay...).
- **SEO**: Meta, title, description, tags.
- **Imtihanen**: Yal template ilaq ad yili deg imtihanen n tawuri, uskan, d tawaḍit n medias.
- **Azref n tazwart**: Asirem n tazwart d izerfan n medias ilaq ad yili.

---

## ✅ Exemples de conformité / Compliance Examples

- **Sécurité** :
  ```html
  <!-- Ne jamais afficher d’information média confidentielle ou de donnée personnelle : -->
  <!-- {{ media.secret_droits }} ❌ -->
  ```
- **Accessibilité** :
  ```html
  <html lang="fr"> <!-- Obligatoire -->
  <img src="{% static 'medias/exemple.jpg' %}" alt="{% trans 'Exemple média' %}" />
  ```
- **i18n** :
  ```django
  <h1>{% trans "Bienvenue sur la médiathèque souveraine" %}</h1>
  ```
- **SEO** :
  ```html
  <meta name="description" content="{% trans 'Plateforme médias souveraine, conforme RGPD et sécurisée' %}">
  ```

---

## 🔒 Contrôle & Audit

- **CI/CD** : Les templates sont vérifiés automatiquement à chaque push (lint, accessibilité, i18n, sécurité, conformité médias).
- **Audit** : Toute modification doit être revue par un mainteneur référent.
- **Logs** : Les accès aux templates sont journalisés côté serveur (audit trail).

---

## 🤝 Contribution

- Respectez cette politique pour toute contribution.
- Toute PR non conforme sera refusée.

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, conformité médias, excellence.
