# 🚚 Dihya Logistique Module – Politique d’Utilisation / Usage Policy / سياسة الاستخدام / ⴰⵙⵏⴼⴰⵡ ⵏ ⵍⵓⴳⵙⵜⵉⴽ

---

## 🇫🇷 Politique d’Utilisation

Ce dossier contient les templates du module "logistique" de Dihya.
**Respect des règles :**
- **Sécurité** : Aucune donnée sensible, information confidentielle, ou secret logistique ne doit être exposé dans les templates.
- **Accessibilité** : Tous les templates doivent respecter le RGAA/WCAG (lang, contrastes, navigation clavier, ARIA).
- **Internationalisation** : Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- **Souveraineté numérique & RGPD** : Aucun appel à des ressources externes non souveraines (CDN, analytics tiers, etc.), conformité RGPD, mentions légales obligatoires.
- **Confidentialité** : Pas de tracking, pas de cookies tiers, respect de la vie privée des utilisateurs et des données logistiques.
- **Rôles** : Les templates doivent intégrer la gestion des rôles utilisateur (gestionnaire, opérateur, admin, invité…).
- **SEO** : Balises meta, titres, descriptions, et balises structurées obligatoires.
- **Tests** : Chaque template doit être couvert par des tests d’accessibilité, de rendu et de conformité logistique.

---

## 🇬🇧 Usage Policy

This folder contains the "logistique" (logistics) module templates for Dihya.
**Rules:**
- **Security**: No sensitive data, confidential info, or logistics secrets must be exposed in templates.
- **Accessibility**: All templates must comply with RGAA/WCAG (lang, contrast, keyboard nav, ARIA).
- **Internationalization**: Use `{% trans %}` or `{% blocktrans %}` for all displayed text.
- **Digital Sovereignty & GDPR**: No calls to non-sovereign external resources (CDN, third-party analytics, etc.), GDPR compliance, legal notices required.
- **Privacy**: No tracking, no third-party cookies, user and logistics data privacy respected.
- **Roles**: Templates must integrate user role management (manager, operator, admin, guest…).
- **SEO**: Meta tags, titles, descriptions, and structured tags are mandatory.
- **Tests**: Each template must be covered by accessibility, rendering, and logistics compliance tests.

---

## 🇦🇪 سياسة الاستخدام

يحتوي هذا المجلد على قوالب وحدة "اللوجستيك" في ديهيا.
**القواعد:**
- **الأمان**: لا يجوز كشف أي بيانات حساسة أو معلومات سرية أو أسرار لوجستية في القوالب.
- **إمكانية الوصول**: يجب أن تتوافق جميع القوالب مع معايير الوصول (RGAA/WCAG).
- **تعدد اللغات**: استخدم `{% trans %}` أو `{% blocktrans %}` لكل النصوص.
- **السيادة الرقمية والتوافق مع RGPD**: لا تستخدم موارد خارجية غير سيادية، توافق RGPD، وجوب وجود إشعارات قانونية.
- **الخصوصية**: لا تتبع المستخدمين، لا كوكيز لطرف ثالث، احترام خصوصية المستخدمين وبياناتهم اللوجستية.
- **الأدوار**: يجب أن تدعم القوالب إدارة الأدوار (مدير، مشغل، مشرف، زائر...).
- **تحسين محركات البحث**: يجب تضمين وسوم meta والعناوين والوصف.
- **الاختبارات**: يجب تغطية كل قالب باختبارات وصول وعرض وتوافق لوجستي.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n uγmis "logistique" n Dihya.
**Imiḍan:**
- **Taɣult**: Ulac isefka ur nelli d asensi, isefka uslig, neɣ asensi n logistique deg templates.
- **Tawuri**: Akk templates ilaq ad s-d-yerrun i RGAA/WCAG.
- **Tamyizt**: Seqdec `{% trans %}` neɣ `{% blocktrans %}` i yal awal.
- **Aseggas n tmedyazt & RGPD**: Ulac tazwara d isemlal ur nelli d n tmurt, RGPD ilaq ad yili, tazwart n taseddast ilaq ad tili.
- **Tawuri n wudem**: Ulac tracking, ulac cookies n uzzay, uslig n uclay d isefka n logistique yettwaselkem.
- **Isemnisen**: Templates ilaq ad s-d-yerrun i uselkim n wudem (amnas, amsawal, admin, azay...).
- **SEO**: Meta, title, description, tags.
- **Imtihanen**: Yal template ilaq ad yili deg imtihanen n tawuri, uskan, d tawaḍit n logistique.

---

## ✅ Exemples de conformité / Compliance Examples

- **Sécurité** :
  ```html
  <!-- Ne jamais afficher d’information logistique confidentielle ou de donnée sensible : -->
  <!-- {{ livraison.secret_logistique }} ❌ -->
  ```
- **Accessibilité** :
  ```html
  <html lang="fr"> <!-- Obligatoire -->
  <button aria-label="{% trans 'Voir le suivi' %}"></button>
  ```
- **i18n** :
  ```django
  <h1>{% trans "Bienvenue sur la plateforme logistique souveraine" %}</h1>
  ```
- **SEO** :
  ```html
  <meta name="description" content="{% trans 'Plateforme logistique souveraine, conforme RGPD et sécurisée' %}">
  ```

---

## 🔒 Contrôle & Audit

- **CI/CD** : Les templates sont vérifiés automatiquement à chaque push (lint, accessibilité, i18n, sécurité, conformité logistique).
- **Audit** : Toute modification doit être revue par un mainteneur référent.
- **Logs** : Les accès aux templates sont journalisés côté serveur (audit trail).

---

## 🤝 Contribution

- Respectez cette politique pour toute contribution.
- Toute PR non conforme sera refusée.

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, conformité logistique, excellence.
