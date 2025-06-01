# 📱 Dihya – Mobile Templates

---

## 🇫🇷 Présentation

Ce dossier contient les templates HTML du module **mobile** de Dihya (PWA, web mobile, intégration Flutter/React Native, etc.).
Ils sont conçus pour garantir : sécurité, accessibilité, confidentialité, souveraineté numérique, conformité mobile (RGPD, notifications souveraines, accessibilité), internationalisation, SEO, modularité, compatibilité multi-stack.

- **Stack compatible** : Django, Jinja2, moteurs alternatifs, IA open source, PWA, Flutter, React Native, notifications souveraines.
- **Sécurité** : Pas de données personnelles, information sensible, ou secret mobile, pas de scripts inline, conformité RGPD/vie privée.
- **Accessibilité** : RGAA/WCAG, navigation tactile/voix, ARIA, responsive, contrastes.
- **i18n** : Prise en charge multilingue (français, anglais, arabe, amazigh).
- **SEO & PWA** : Balises meta, titres, descriptions, manifest, viewport responsive, données structurées.
- **Rôles** : Gestion dynamique des rôles utilisateur (utilisateur mobile, admin, invité…).
- **Tests** : Couverture automatique (lint, accessibilité, rendu, conformité mobile/PWA).
- **Souveraineté** : Aucun appel à des ressources externes non souveraines, notifications push souveraines uniquement, conformité RGPD, mentions légales.

---

## 🇬🇧 Overview

This folder contains the **mobile** module HTML templates for Dihya (PWA, mobile web, Flutter/React Native integration, etc.).
Designed for : security, accessibility, privacy, digital sovereignty, mobile compliance (GDPR, sovereign notifications, accessibility), i18n, SEO, modularity, multi-stack compatibility.

- **Stack compatible**: Django, Jinja2, alternative engines, open source AI, PWA, Flutter, React Native, sovereign notifications.
- **Security**: No personal data, sensitive info, or mobile secrets, no inline scripts, GDPR/privacy compliant.
- **Accessibility**: RGAA/WCAG, touch/voice nav, ARIA, responsive, contrast.
- **i18n**: Multilingual support (French, English, Arabic, Amazigh).
- **SEO & PWA**: Meta tags, titles, descriptions, manifest, responsive viewport, structured data.
- **Roles**: Dynamic user role management (mobile user, admin, guest…).
- **Tests**: Automatic coverage (lint, accessibility, rendering, mobile/PWA compliance).
- **Sovereignty**: No calls to non-sovereign external resources, only sovereign push notifications, GDPR compliance, legal notices.

---

## 🇦🇪 مقدمة

يحتوي هذا المجلد على قوالب HTML لوحدة "الموبايل" في ديهيا (PWA، ويب موبايل، تكامل Flutter/React Native...).
مصممة للأمان، الخصوصية، الوصول، السيادة الرقمية، التوافق المحمول (RGPD، إشعارات سيادية، الوصول)، التعدد اللغوي، تحسين محركات البحث، التمدد، التوافق مع عدة تقنيات.

- **التوافق**: Django، Jinja2، محركات أخرى، ذكاء اصطناعي مفتوح المصدر، PWA، Flutter، React Native، إشعارات سيادية.
- **الأمان**: لا بيانات شخصية أو معلومات حساسة أو أسرار موبايل، لا سكريبتات داخلية، متوافق مع GDPR/خصوصية المستخدمين.
- **الوصول**: معايير RGAA/WCAG، دعم اللمس/الصوت، ARIA، استجابة التصميم، تباين.
- **تعدد اللغات**: دعم الفرنسية، الإنجليزية، العربية، الأمازيغية.
- **SEO & PWA**: وسوم meta، عناوين، أوصاف، manifest، viewport، بيانات منظمة.
- **الأدوار**: إدارة ديناميكية للأدوار (مستخدم موبايل، مشرف، زائر...).
- **الاختبارات**: تغطية تلقائية (lint، وصول، عرض، توافق موبايل/PWA).
- **السيادة**: لا موارد خارجية غير سيادية، إشعارات دفع سيادية فقط، توافق RGPD، إشعارات قانونية.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n HTML n uγmis "mobile" n Dihya (PWA, web mobile, Flutter, React Native...).
Iɣewwaṛen i taɣult, tawuri, uslig, tmedyazt, tawaḍit n mobile, tamyizt, SEO, tmedyazt, amsawal n multi-stack.

- **Tawuri**: Ulac isefka ur nelli d asensi, isefka uslig, neɣ asensi n mobile, ulac script deg templates.
- **Tawuri n wudem**: RGAA/WCAG, tawuri n tneflit, ARIA, responsive, tawuri n tneflit n mobile.
- **Tamyizt**: Tamulti (fr, en, ar, tz).
- **SEO & PWA**: Meta, title, description, manifest, viewport, tags.
- **Isemnisen**: Uselkim n wudem (mobile user, admin, azay…).
- **Imtihanen**: Lint, tawuri, uskan, tawaḍit n mobile/PWA.
- **Aseggas n tmedyazt**: Ulac tazwara d isemlal ur nelli d n tmurt, push n tmurt kan, RGPD ilaq ad yili, tazwart n taseddast ilaq ad tili.

---

## 🚀 Structure & Bonnes pratiques / Best Practices

- Placez vos fichiers `.html` ici.
- Respectez la [policy.md](./policy.md) pour chaque template.
- Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- Ajoutez les balises `<html lang="">`, `<meta>`, `<title>`, ARIA, manifest, viewport responsive.
- Ne jamais afficher d’information mobile confidentielle ou de donnée personnelle.
- Pour chaque nouveau template, ajoutez un test d’accessibilité, de rendu et de conformité mobile/PWA.

---

## 🧩 Exemple de template conforme

```django
{# filepath: mobile/example.html #}
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}{% trans "Accueil Mobile" %}{% endblock %}</title>
  <meta name="description" content="{% trans 'Application mobile souveraine, conforme RGPD et sécurisée' %}">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="manifest" href="{% static 'mobile/manifest.json' %}">
  {% block extra_meta %}{% endblock %}
</head>
<body>
  <header>
    <h1>{% trans "Bienvenue sur l’application mobile souveraine" %}</h1>
    {% if user.is_authenticated %}
      <p>{% trans "Connecté en tant que" %} {{ user.username }}</p>
      {% if user.is_superuser %}
        <span class="role">{% trans "Administrateur" %}</span>
      {% elif user.groups|length > 0 %}
        <span class="role">{% trans "Utilisateur mobile" %}</span>
      {% else %}
        <span class="role">{% trans "Invité" %}</span>
      {% endif %}
    {% else %}
      <a href="{% url 'login' %}">{% trans "Connexion" %}</a>
    {% endif %}
  </header>
  <main>
    <button aria-label="{% trans 'Menu mobile' %}"></button>
    {% block content %}{% endblock %}
  </main>
  <footer>
    <small>&copy; 2025 Dihya</small>
    <a href="{% url 'legal_mentions' %}">{% trans "Mentions légales" %}</a>
  </footer>
</body>
</html>
```

---

## 🧪 Tests & CI

- Chaque template est vérifié automatiquement (lint, accessibilité, i18n, sécurité, conformité mobile/PWA) via CI/CD.
- Pour lancer les tests localement :
  ```bash
  python manage.py test app.tests.test_templates_mobile
  ```

---

## 🤝 Contribution

- Toute contribution doit respecter la [policy.md](./policy.md).
- Les PRs non conformes sont refusées.
- Multilingue : tout nouveau texte doit être balisé pour la traduction.

---

## 📚 Ressources

- [Django i18n](https://docs.djangoproject.com/fr/stable/topics/i18n/translation/)
- [WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [RGAA](https://accessibilite.numerique.gouv.fr/methode/criteres/)
- [CNIL RGPD](https://www.cnil.fr/fr/rgpd-de-quoi-parle-t-on)
- [Dihya Docs](../../../../docs/)

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, conformité mobile, excellence.
