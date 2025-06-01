# 🤖 Dihya – Intelligence Artificielle Templates

---

## 🇫🇷 Présentation

Ce dossier contient les templates HTML du module **intelligence_artificielle** de Dihya.
Ils sont conçus pour garantir : sécurité, accessibilité, confidentialité, souveraineté numérique, éthique IA, internationalisation, SEO, modularité.

- **Stack compatible** : Django, Jinja2, moteurs alternatifs, fallback IA open source.
- **Sécurité** : Pas de données sensibles, clé API, secret, ou donnée confidentielle, pas de scripts inline, conformité RGPD/vie privée.
- **Accessibilité** : RGAA/WCAG, navigation clavier, ARIA, contrastes.
- **i18n** : Prise en charge multilingue (français, anglais, arabe, amazigh).
- **SEO** : Balises meta, titres, descriptions, données structurées.
- **Rôles** : Gestion dynamique des rôles utilisateur (data scientist, opérateur, client, admin, invité…).
- **Tests** : Couverture automatique (lint, accessibilité, rendu, conformité IA).
- **Souveraineté** : Aucun appel à des ressources externes non souveraines, IA locale priorisée.

---

## 🇬🇧 Overview

This folder contains the **intelligence_artificielle** (AI) module HTML templates for Dihya.
Designed for : security, accessibility, privacy, digital sovereignty, AI ethics, i18n, SEO, modularity.

- **Stack compatible**: Django, Jinja2, alternative engines, open source AI fallback.
- **Security**: No sensitive data, API key, secret, or confidential info, no inline scripts, GDPR/privacy compliant.
- **Accessibility**: RGAA/WCAG, keyboard nav, ARIA, contrast.
- **i18n**: Multilingual support (French, English, Arabic, Amazigh).
- **SEO**: Meta tags, titles, descriptions, structured data.
- **Roles**: Dynamic user role management (data scientist, operator, customer, admin, guest…).
- **Tests**: Automatic coverage (lint, accessibility, rendering, AI compliance).
- **Sovereignty**: No calls to non-sovereign external resources, local AI prioritized.

---

## 🇦🇪 مقدمة

يحتوي هذا المجلد على قوالب HTML لوحدة "الذكاء الاصطناعي" في ديهيا.
مصممة للأمان، الخصوصية، الوصول، السيادة الرقمية، أخلاقيات الذكاء الاصطناعي، التعدد اللغوي، تحسين محركات البحث، التمدد.

- **التوافق**: Django، Jinja2، محركات أخرى، ذكاء اصطناعي مفتوح المصدر.
- **الأمان**: لا بيانات حساسة أو مفاتيح API أو أسرار أو بيانات سرية، لا سكريبتات داخلية، متوافق مع GDPR/خصوصية المستخدمين.
- **الوصول**: معايير RGAA/WCAG، تنقل لوحة المفاتيح، ARIA.
- **تعدد اللغات**: دعم الفرنسية، الإنجليزية، العربية، الأمازيغية.
- **SEO**: وسوم meta، عناوين، أوصاف، بيانات منظمة.
- **الأدوار**: إدارة ديناميكية للأدوار (عالم بيانات، مشغل، عميل، مشرف، زائر...).
- **الاختبارات**: تغطية تلقائية (lint، وصول، عرض، توافق ذكاء اصطناعي).
- **السيادة**: لا موارد خارجية غير سيادية، أولوية للذكاء الاصطناعي المحلي.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n HTML n uγmis "intelligence_artificielle" n Dihya.
Iɣewwaṛen i taɣult, tawuri, uslig, tmedyazt, tawaḍit IA, tamyizt, SEO, tmedyazt.

- **Tawuri**: Ulac isefka ur nelli d asensi, api_key, secret, neɣ isefka uslig, ulac script deg templates.
- **Tawuri n wudem**: RGAA/WCAG, tawuri n tneflit, ARIA.
- **Tamyizt**: Tamulti (fr, en, ar, tz).
- **SEO**: Meta, title, description, tags.
- **Isemnisen**: Uselkim n wudem (data scientist, amḍan, acilay, admin, azay…).
- **Imtihanen**: Lint, tawuri, uskan, tawaḍit IA.
- **Aseggas n tmedyazt**: Ulac tazwara d isemlal ur nelli d n tmurt, IA n tmurt d amezwaru.

---

## 🚀 Structure & Bonnes pratiques / Best Practices

- Placez vos fichiers `.html` ici.
- Respectez la [policy.md](./policy.md) pour chaque template.
- Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- Ajoutez les balises `<html lang="">`, `<meta>`, `<title>`, et ARIA.
- Ne jamais afficher de données sensibles, clé API, secret, ou donnée IA confidentielle.
- Pour chaque nouveau template, ajoutez un test d’accessibilité, de rendu et de conformité IA.

---

## 🧩 Exemple de template conforme

```django
{# filepath: intelligence_artificielle/example.html #}
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}{% trans "Accueil IA" %}{% endblock %}</title>
  <meta name="description" content="{% trans 'Plateforme IA souveraine, éthique et sécurisée' %}">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% block extra_meta %}{% endblock %}
</head>
<body>
  <header>
    <h1>{% trans "Bienvenue sur la plateforme IA souveraine" %}</h1>
    {% if user.is_authenticated %}
      <p>{% trans "Connecté en tant que" %} {{ user.username }}</p>
      {% if user.is_superuser %}
        <span class="role">{% trans "Administrateur" %}</span>
      {% elif user.groups|length > 0 %}
        <span class="role">{% trans "Data Scientist" %}</span>
      {% else %}
        <span class="role">{% trans "Client" %}</span>
      {% endif %}
    {% else %}
      <a href="{% url 'login' %}">{% trans "Connexion" %}</a>
    {% endif %}
  </header>
  <main>
    {% block content %}{% endblock %}
  </main>
  <footer>
    <small>&copy; 2025 Dihya</small>
  </footer>
</body>
</html>
```

---

## 🧪 Tests & CI

- Chaque template est vérifié automatiquement (lint, accessibilité, i18n, sécurité, conformité IA) via CI/CD.
- Pour lancer les tests localement :
  ```bash
  python manage.py test app.tests.test_templates_intelligence_artificielle
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
- [Dihya Docs](../../../../docs/)

---

© 2025 Dihya – Souveraineté, sécurité, accessibilité, IA éthique, excellence.
