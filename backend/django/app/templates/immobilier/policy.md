# 🏢 Dihya Immobilier Module – Politique d’Utilisation / Usage Policy / سياسة الاستخدام / ⴰⵙⵏⴼⴰⵡ ⵏ ⴰⵎⵓⴱⴱⵉⵍⵉⵔ

---

## 🇫🇷 Politique d’Utilisation

Ce dossier contient les templates du module "immobilier" de Dihya.
**Respect des règles :**
- **Sécurité** : Aucune donnée sensible, client ou propriétaire ne doit être exposée dans les templates.
- **Accessibilité** : Tous les templates doivent respecter le RGAA/WCAG (lang, contrastes, navigation clavier, ARIA).
- **Internationalisation** : Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- **Souveraineté numérique** : Aucun appel à des ressources externes non souveraines (CDN, analytics tiers, etc.).
- **Confidentialité** : Pas de tracking, pas de cookies tiers, respect de la vie privée des utilisateurs.
- **Rôles** : Les templates doivent intégrer la gestion des rôles utilisateur (agent, propriétaire, client, admin, invité…).
- **SEO** : Balises meta, titres, descriptions, et balises structurées obligatoires.
- **Tests** : Chaque template doit être couvert par des tests d’accessibilité et de rendu.

---

## 🇬🇧 Usage Policy

This folder contains the "immobilier" (real estate) module templates for Dihya.
**Rules:**
- **Security**: No sensitive, customer or owner data must be exposed in templates.
- **Accessibility**: All templates must comply with RGAA/WCAG (lang, contrast, keyboard nav, ARIA).
- **Internationalization**: Use `{% trans %}` or `{% blocktrans %}` for all displayed text.
- **Digital Sovereignty**: No calls to non-sovereign external resources (CDN, third-party analytics, etc.).
- **Privacy**: No tracking, no third-party cookies, user privacy respected.
- **Roles**: Templates must integrate user role management (agent, owner, customer, admin, guest…).
- **SEO**: Meta tags, titles, descriptions, and structured tags are mandatory.
- **Tests**: Each template must be covered by accessibility and rendering tests.

---

## 🇦🇪 سياسة الاستخدام

يحتوي هذا المجلد على قوالب وحدة "العقار" في ديهيا.
**القواعد:**
- **الأمان**: لا يجوز كشف أي بيانات حساسة أو بيانات العملاء أو المالكين في القوالب.
- **إمكانية الوصول**: يجب أن تتوافق جميع القوالب مع معايير الوصول (RGAA/WCAG).
- **تعدد اللغات**: استخدم `{% trans %}` أو `{% blocktrans %}` لكل النصوص.
- **السيادة الرقمية**: لا تستخدم موارد خارجية غير سيادية.
- **الخصوصية**: لا تتبع المستخدمين، لا كوكيز لطرف ثالث، احترام خصوصية المستخدمين.
- **الأدوار**: يجب أن تدعم القوالب إدارة الأدوار (وكيل، مالك، عميل، مشرف، زائر...).
- **تحسين محركات البحث**: يجب تضمين وسوم meta والعناوين والوصف.
- **الاختبارات**: يجب تغطية كل قالب باختبارات وصول وعرض.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n uγmis "immobilier" n Dihya.
**Imiḍan:**
- **Taɣult**: Ulac isefka ur nelli d asensi neɣ n uclay neɣ n umalik deg templates.
- **Tawuri**: Akk templates ilaq ad s-d-yerrun i RGAA/WCAG.
- **Tamyizt**: Seqdec `{% trans %}` neɣ `{% blocktrans %}` i yal awal.
- **Aseggas n tmedyazt**: Ulac tazwara d isemlal ur nelli d n tmurt.
- **Tawuri n wudem**: Ulac tracking, ulac cookies n uzzay, uslig n uclay yettwaselkem.
- **Isemnisen**: Templates ilaq ad s-d-yerrun i uselkim n wudem (agent, amalik, acilay, admin, azay...).
- **SEO**: Meta, title, description, tags.
- **Imtihanen**: Yal template ilaq ad yili deg imtihanen n tawuri d uskan.

---

## ✅ Exemples de conformité / Compliance Examples

- **Sécurité** :
  ```html
  <!-- Ne jamais afficher de variable sensible ou client/propriétaire : -->
  <!-- {{ owner.bank_account }} ❌ -->
  ```
- **Accessibilité** :
  ```html
  <html lang="fr"> <!-- Obligatoire -->
  <button aria-label="{% trans 'Demander une visite' %}"></button>
  ```
- **i18n** :
  ```django
  <h1>{% trans "Bienvenue sur la plateforme immobilière" %}</h1>
  ```
- **SEO** :
  ```html
  <meta name="description" content="{% trans 'Plateforme immobilière souveraine' %}">
  ```

---

## 🔒 Contrôle & Audit

- **CI/CD** : Les templates sont vérifiés automatiquement à chaque push (lint, accessibilité, i18n, sécurité).
- **Audit** : Toute modification doit être revue par un mainteneur référent.
- **Logs** : Les accès aux templates sont journalisés côté serveur (audit trail).

---

## 🤝 Contribution

- Respectez cette politique pour toute contribution.
- Toute PR non conforme sera refusée.

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, excellence.
