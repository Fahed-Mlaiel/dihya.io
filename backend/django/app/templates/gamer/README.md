# 🎮 Dihya – Gamer Templates

---

## 🇫🇷 Présentation

Ce dossier contient les templates HTML du module **gamer** de Dihya.
Ils sont conçus pour garantir : sécurité, accessibilité, internationalisation, SEO, modularité, et souveraineté numérique.

- **Stack compatible** : Django, Jinja2, moteurs alternatifs.
- **Sécurité** : Pas de données sensibles, pas de scripts inline, conformité RGPD.
- **Accessibilité** : RGAA/WCAG, navigation clavier, ARIA, contrastes.
- **i18n** : Prise en charge multilingue (français, anglais, arabe, amazigh).
- **SEO** : Balises meta, titres, descriptions, données structurées.
- **Rôles** : Gestion dynamique des rôles utilisateur (admin, joueur, invité…).
- **Tests** : Couverture automatique (lint, accessibilité, rendu).
- **Souveraineté** : Aucun appel à des ressources externes non souveraines.

---

## 🇬🇧 Overview

This folder contains the **gamer** module HTML templates for Dihya.
Designed for : security, accessibility, i18n, SEO, modularity, and digital sovereignty.

- **Stack compatible**: Django, Jinja2, alternative engines.
- **Security**: No sensitive data, no inline scripts, GDPR compliant.
- **Accessibility**: RGAA/WCAG, keyboard nav, ARIA, contrast.
- **i18n**: Multilingual support (French, English, Arabic, Amazigh).
- **SEO**: Meta tags, titles, descriptions, structured data.
- **Roles**: Dynamic user role management (admin, player, guest…).
- **Tests**: Automatic coverage (lint, accessibility, rendering).
- **Sovereignty**: No calls to non-sovereign external resources.

---

## 🇦🇪 مقدمة

يحتوي هذا المجلد على قوالب HTML لوحدة "gamer" في ديهيا.
مصممة للأمان، الوصول، التعدد اللغوي، تحسين محركات البحث، السيادة الرقمية.

- **التوافق**: Django، Jinja2، محركات أخرى.
- **الأمان**: لا بيانات حساسة، لا سكريبتات داخلية، متوافق مع GDPR.
- **الوصول**: معايير RGAA/WCAG، تنقل لوحة المفاتيح، ARIA.
- **تعدد اللغات**: دعم الفرنسية، الإنجليزية، العربية، الأمازيغية.
- **SEO**: وسوم meta، عناوين، أوصاف، بيانات منظمة.
- **الأدوار**: إدارة ديناميكية للأدوار (مشرف، لاعب، زائر...).
- **الاختبارات**: تغطية تلقائية (lint، وصول، عرض).
- **السيادة**: لا موارد خارجية غير سيادية.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n HTML n uγmis "gamer" n Dihya.
Iɣewwaṛen i taɣult, tawuri, tamyizt, SEO, tmedyazt.

- **Tawuri**: Ulac isefka ur nelli d asensi, ulac script deg templates.
- **Tawuri n wudem**: RGAA/WCAG, tawuri n tneflit, ARIA.
- **Tamyizt**: Tamulti (fr, en, ar, tz).
- **SEO**: Meta, title, description, tags.
- **Isemnisen**: Uselkim n wudem (admin, amaynut, azay…).
- **Imtihanen**: Lint, tawuri, uskan.
- **Aseggas n tmedyazt**: Ulac tazwara d isemlal ur nelli d n tmurt.

---

## 🚀 Structure & Bonnes pratiques / Best Practices

- Placez vos fichiers `.html` ici.
- Respectez la [policy.md](./policy.md) pour chaque template.
- Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- Ajoutez les balises `<html lang="">`, `<meta>`, `<title>`, et ARIA.
- Ne jamais afficher de données sensibles.
- Pour chaque nouveau template, ajoutez un test d’accessibilité et de rendu.

---

## 🧩 Exemple de template conforme

```django
{# filepath: gamer/example.html #}
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}{% trans "Accueil Gamer" %}{% endblock %}</title>
  <meta name="description" content="{% trans 'Plateforme gaming souveraine' %}">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% block extra_meta %}{% endblock %}
</head>
<body>
  <header>
    <h1>{% trans "Bienvenue joueur" %}</h1>
    {% if user.is_authenticated %}
      <p>{% trans "Connecté en tant que" %} {{ user.username }}</p>
      {% if user.is_superuser %}
        <span class="role">{% trans "Administrateur" %}</span>
      {% elif user.groups|length > 0 %}
        <span class="role">{% trans "Joueur" %}</span>
      {% else %}
        <span class="role">{% trans "Invité" %}</span>
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

- Chaque template est vérifié automatiquement (lint, accessibilité, i18n, sécurité) via CI/CD.
- Pour lancer les tests localement :
  ```bash
  python manage.py test app.tests.test_templates_gamer
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

© 2025 Dihya – Souveraineté, sécurité, accessibilité, excellence.
