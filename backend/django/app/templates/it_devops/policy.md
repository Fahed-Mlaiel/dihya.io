# 🖥️ Dihya IT & DevOps Module – Politique d’Utilisation / Usage Policy / سياسة الاستخدام / ⴰⵙⵏⴼⴰⵡ ⵏ IT & DevOps

---

## 🇫🇷 Politique d’Utilisation

Ce dossier contient les templates du module "it_devops" de Dihya.
**Respect des règles :**
- **Sécurité** : Aucune donnée sensible, secret, token, mot de passe, clé ou information d’infrastructure ne doit être exposée dans les templates.
- **Accessibilité** : Tous les templates doivent respecter le RGAA/WCAG (lang, contrastes, navigation clavier, ARIA).
- **Internationalisation** : Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- **Souveraineté numérique & DevSecOps** : Aucun appel à des ressources externes non souveraines (CDN, analytics tiers, monitoring cloud non maîtrisé, etc.).
- **Confidentialité** : Pas de tracking, pas de cookies tiers, respect de la vie privée des utilisateurs et des données d’infrastructure.
- **Rôles** : Les templates doivent intégrer la gestion des rôles utilisateur (dev, ops, devops, admin, invité…).
- **SEO** : Balises meta, titres, descriptions, et balises structurées obligatoires.
- **Tests** : Chaque template doit être couvert par des tests d’accessibilité, de rendu et de conformité DevOps.

---

## 🇬🇧 Usage Policy

This folder contains the "it_devops" module templates for Dihya.
**Rules:**
- **Security**: No sensitive data, secret, token, password, key, or infrastructure info must be exposed in templates.
- **Accessibility**: All templates must comply with RGAA/WCAG (lang, contrast, keyboard nav, ARIA).
- **Internationalization**: Use `{% trans %}` or `{% blocktrans %}` for all displayed text.
- **Digital Sovereignty & DevSecOps**: No calls to non-sovereign external resources (CDN, third-party analytics, uncontrolled cloud monitoring, etc.).
- **Privacy**: No tracking, no third-party cookies, user and infrastructure data privacy respected.
- **Roles**: Templates must integrate user role management (dev, ops, devops, admin, guest…).
- **SEO**: Meta tags, titles, descriptions, and structured tags are mandatory.
- **Tests**: Each template must be covered by accessibility, rendering, and DevOps compliance tests.

---

## 🇦🇪 سياسة الاستخدام

يحتوي هذا المجلد على قوالب وحدة "تكنولوجيا المعلومات و DevOps" في ديهيا.
**القواعد:**
- **الأمان**: لا يجوز كشف أي بيانات حساسة أو أسرار أو رموز أو كلمات مرور أو مفاتيح أو معلومات بنية تحتية في القوالب.
- **إمكانية الوصول**: يجب أن تتوافق جميع القوالب مع معايير الوصول (RGAA/WCAG).
- **تعدد اللغات**: استخدم `{% trans %}` أو `{% blocktrans %}` لكل النصوص.
- **السيادة الرقمية و DevSecOps**: لا تستخدم موارد خارجية غير سيادية أو مراقبة سحابية غير خاضعة للسيطرة.
- **الخصوصية**: لا تتبع المستخدمين، لا كوكيز لطرف ثالث، احترام خصوصية المستخدمين وبيانات البنية التحتية.
- **الأدوار**: يجب أن تدعم القوالب إدارة الأدوار (مطور، عمليات، ديفوبس، مشرف، زائر...).
- **تحسين محركات البحث**: يجب تضمين وسوم meta والعناوين والوصف.
- **الاختبارات**: يجب تغطية كل قالب باختبارات وصول وعرض وتوافق DevOps.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n uγmis "it_devops" n Dihya.
**Imiḍan:**
- **Taɣult**: Ulac isefka ur nelli d asensi, secret, token, password, key, neɣ isefka n tneflit deg templates.
- **Tawuri**: Akk templates ilaq ad s-d-yerrun i RGAA/WCAG.
- **Tamyizt**: Seqdec `{% trans %}` neɣ `{% blocktrans %}` i yal awal.
- **Aseggas n tmedyazt & DevSecOps**: Ulac tazwara d isemlal ur nelli d n tmurt, ulac monitoring cloud ur nettwaselkem.
- **Tawuri n wudem**: Ulac tracking, ulac cookies n uzzay, uslig n uclay d isefka n tneflit yettwaselkem.
- **Isemnisen**: Templates ilaq ad s-d-yerrun i uselkim n wudem (dev, ops, devops, admin, azay...).
- **SEO**: Meta, title, description, tags.
- **Imtihanen**: Yal template ilaq ad yili deg imtihanen n tawuri, uskan, d tawaḍit DevOps.

---

## ✅ Exemples de conformité / Compliance Examples

- **Sécurité** :
  ```html
  <!-- Ne jamais afficher de secret, token, mot de passe ou clé : -->
  <!-- {{ devops.secret_token }} ❌ -->
  ```
- **Accessibilité** :
  ```html
  <html lang="fr"> <!-- Obligatoire -->
  <button aria-label="{% trans 'Déployer' %}"></button>
  ```
- **i18n** :
  ```django
  <h1>{% trans "Bienvenue sur la plateforme DevOps souveraine" %}</h1>
  ```
- **SEO** :
  ```html
  <meta name="description" content="{% trans 'Plateforme DevOps souveraine, sécurisée et conforme' %}">
  ```

---

## 🔒 Contrôle & Audit

- **CI/CD** : Les templates sont vérifiés automatiquement à chaque push (lint, accessibilité, i18n, sécurité, conformité DevOps).
- **Audit** : Toute modification doit être revue par un mainteneur référent.
- **Logs** : Les accès aux templates sont journalisés côté serveur (audit trail).

---

## 🤝 Contribution

- Respectez cette politique pour toute contribution.
- Toute PR non conforme sera refusée.

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, DevSecOps, excellence.
