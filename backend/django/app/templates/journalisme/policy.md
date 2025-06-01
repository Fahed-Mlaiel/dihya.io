# 📰 Dihya Journalisme Module – Politique d’Utilisation / Usage Policy / سياسة الاستخدام / ⴰⵙⵏⴼⴰⵡ ⵏ ⵉⵙⵉⵏⴰⵡⵉⵙ

---

## 🇫🇷 Politique d’Utilisation

Ce dossier contient les templates du module "journalisme" de Dihya.
**Respect des règles :**
- **Sécurité** : Aucune donnée sensible, source confidentielle, ou information non vérifiée ne doit être exposée dans les templates.
- **Accessibilité** : Tous les templates doivent respecter le RGAA/WCAG (lang, contrastes, navigation clavier, ARIA).
- **Internationalisation** : Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- **Souveraineté numérique & Éthique** : Aucun appel à des ressources externes non souveraines (CDN, analytics tiers, etc.), respect de l’éthique journalistique (pas de fake news, pas de publicité intrusive, pas de tracking).
- **Confidentialité** : Pas de tracking, pas de cookies tiers, respect de la vie privée des utilisateurs et des sources.
- **Rôles** : Les templates doivent intégrer la gestion des rôles utilisateur (journaliste, éditeur, lecteur, admin, invité…).
- **SEO** : Balises meta, titres, descriptions, et balises structurées obligatoires.
- **Tests** : Chaque template doit être couvert par des tests d’accessibilité, de rendu et de conformité éthique.

---

## 🇬🇧 Usage Policy

This folder contains the "journalisme" (journalism) module templates for Dihya.
**Rules:**
- **Security**: No sensitive data, confidential source, or unverified information must be exposed in templates.
- **Accessibility**: All templates must comply with RGAA/WCAG (lang, contrast, keyboard nav, ARIA).
- **Internationalization**: Use `{% trans %}` or `{% blocktrans %}` for all displayed text.
- **Digital Sovereignty & Ethics**: No calls to non-sovereign external resources (CDN, third-party analytics, etc.), respect journalistic ethics (no fake news, no intrusive ads, no tracking).
- **Privacy**: No tracking, no third-party cookies, user and source privacy respected.
- **Roles**: Templates must integrate user role management (journalist, editor, reader, admin, guest…).
- **SEO**: Meta tags, titles, descriptions, and structured tags are mandatory.
- **Tests**: Each template must be covered by accessibility, rendering, and ethics compliance tests.

---

## 🇦🇪 سياسة الاستخدام

يحتوي هذا المجلد على قوالب وحدة "الصحافة" في ديهيا.
**القواعد:**
- **الأمان**: لا يجوز كشف أي بيانات حساسة أو مصادر سرية أو معلومات غير موثقة في القوالب.
- **إمكانية الوصول**: يجب أن تتوافق جميع القوالب مع معايير الوصول (RGAA/WCAG).
- **تعدد اللغات**: استخدم `{% trans %}` أو `{% blocktrans %}` لكل النصوص.
- **السيادة الرقمية والأخلاقيات**: لا تستخدم موارد خارجية غير سيادية، احترام أخلاقيات الصحافة (لا أخبار زائفة، لا إعلانات مزعجة، لا تتبع).
- **الخصوصية**: لا تتبع المستخدمين، لا كوكيز لطرف ثالث، احترام خصوصية المستخدمين والمصادر.
- **الأدوار**: يجب أن تدعم القوالب إدارة الأدوار (صحفي، محرر، قارئ، مشرف، زائر...).
- **تحسين محركات البحث**: يجب تضمين وسوم meta والعناوين والوصف.
- **الاختبارات**: يجب تغطية كل قالب باختبارات وصول وعرض وتوافق أخلاقي.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n uγmis "journalisme" n Dihya.
**Imiḍan:**
- **Taɣult**: Ulac isefka ur nelli d asensi, source uslig, neɣ isefka ur nettwaselkem deg templates.
- **Tawuri**: Akk templates ilaq ad s-d-yerrun i RGAA/WCAG.
- **Tamyizt**: Seqdec `{% trans %}` neɣ `{% blocktrans %}` i yal awal.
- **Aseggas n tmedyazt & Tawaḍit**: Ulac tazwara d isemlal ur nelli d n tmurt, uslig n tawaḍit n ajurnalist (ulac fake news, ulac ads, ulac tracking).
- **Tawuri n wudem**: Ulac tracking, ulac cookies n uzzay, uslig n uclay d isefka n tneflit yettwaselkem.
- **Isemnisen**: Templates ilaq ad s-d-yerrun i uselkim n wudem (ajurnalist, amsefrak, agrawli, admin, azay...).
- **SEO**: Meta, title, description, tags.
- **Imtihanen**: Yal template ilaq ad yili deg imtihanen n tawuri, uskan, d tawaḍit n tawaḍit.

---

## ✅ Exemples de conformité / Compliance Examples

- **Sécurité** :
  ```html
  <!-- Ne jamais afficher de source confidentielle ou d’information non vérifiée : -->
  <!-- {{ article.source_confidentielle }} ❌ -->
  ```
- **Accessibilité** :
  ```html
  <html lang="fr"> <!-- Obligatoire -->
  <button aria-label="{% trans 'Lire l’article' %}"></button>
  ```
- **i18n** :
  ```django
  <h1>{% trans "Bienvenue sur la plateforme journalistique souveraine" %}</h1>
  ```
- **SEO** :
  ```html
  <meta name="description" content="{% trans 'Plateforme journalistique souveraine, éthique et sécurisée' %}">
  ```

---

## 🔒 Contrôle & Audit

- **CI/CD** : Les templates sont vérifiés automatiquement à chaque push (lint, accessibilité, i18n, sécurité, conformité éthique).
- **Audit** : Toute modification doit être revue par un mainteneur référent.
- **Logs** : Les accès aux templates sont journalisés côté serveur (audit trail).

---

## 🤝 Contribution

- Respectez cette politique pour toute contribution.
- Toute PR non conforme sera refusée.

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, éthique, excellence.
