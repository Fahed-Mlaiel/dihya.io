# 🖥️ Dihya – IT & DevOps Templates

---

## 🇫🇷 Présentation

Ce dossier contient les templates HTML du module **it_devops** de Dihya.
Ils sont conçus pour garantir : sécurité, accessibilité, confidentialité, souveraineté numérique, conformité DevSecOps, internationalisation, SEO, modularité.

- **Stack compatible** : Django, Jinja2, moteurs alternatifs, CI/CD, monitoring, fallback open source.
- **Sécurité** : Pas de données sensibles, secret, token, mot de passe, clé ou information d’infrastructure, pas de scripts inline, conformité RGPD/vie privée.
- **Accessibilité** : RGAA/WCAG, navigation clavier, ARIA, contrastes.
- **i18n** : Prise en charge multilingue (français, anglais, arabe, amazigh).
- **SEO** : Balises meta, titres, descriptions, données structurées.
- **Rôles** : Gestion dynamique des rôles utilisateur (dev, ops, devops, admin, invité…).
- **Tests** : Couverture automatique (lint, accessibilité, rendu, conformité DevOps).
- **Souveraineté** : Aucun appel à des ressources externes non souveraines, monitoring local priorisé.

---

## 🇬🇧 Overview

This folder contains the **it_devops** module HTML templates for Dihya.
Designed for : security, accessibility, privacy, digital sovereignty, DevSecOps compliance, i18n, SEO, modularity.

- **Stack compatible**: Django, Jinja2, alternative engines, CI/CD, monitoring, open source fallback.
- **Security**: No sensitive data, secret, token, password, key, or infrastructure info, no inline scripts, GDPR/privacy compliant.
- **Accessibility**: RGAA/WCAG, keyboard nav, ARIA, contrast.
- **i18n**: Multilingual support (French, English, Arabic, Amazigh).
- **SEO**: Meta tags, titles, descriptions, structured data.
- **Roles**: Dynamic user role management (dev, ops, devops, admin, guest…).
- **Tests**: Automatic coverage (lint, accessibility, rendering, DevOps compliance).
- **Sovereignty**: No calls to non-sovereign external resources, local monitoring prioritized.

---

## 🇦🇪 مقدمة

يحتوي هذا المجلد على قوالب HTML لوحدة "تكنولوجيا المعلومات و DevOps" في ديهيا.
مصممة للأمان، الخصوصية، الوصول، السيادة الرقمية، توافق DevSecOps، التعدد اللغوي، تحسين محركات البحث، التمدد.

- **التوافق**: Django، Jinja2، محركات أخرى، CI/CD، مراقبة، مفتوح المصدر.
- **الأمان**: لا بيانات حساسة أو أسرار أو رموز أو كلمات مرور أو مفاتيح أو معلومات بنية تحتية، لا سكريبتات داخلية، متوافق مع GDPR/خصوصية المستخدمين.
- **الوصول**: معايير RGAA/WCAG، تنقل لوحة المفاتيح، ARIA.
- **تعدد اللغات**: دعم الفرنسية، الإنجليزية، العربية، الأمازيغية.
- **SEO**: وسوم meta، عناوين، أوصاف، بيانات منظمة.
- **الأدوار**: إدارة ديناميكية للأدوار (مطور، عمليات، ديفوبس، مشرف، زائر...).
- **الاختبارات**: تغطية تلقائية (lint، وصول، عرض، توافق DevOps).
- **السيادة**: لا موارد خارجية غير سيادية، أولوية للمراقبة المحلية.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n HTML n uγmis "it_devops" n Dihya.
Iɣewwaṛen i taɣult, tawuri, uslig, tmedyazt, tawaḍit DevOps, tamyizt, SEO, tmedyazt.

- **Tawuri**: Ulac isefka ur nelli d asensi, secret, token, password, key, neɣ isefka n tneflit, ulac script deg templates.
- **Tawuri n wudem**: RGAA/WCAG, tawuri n tneflit, ARIA.
- **Tamyizt**: Tamulti (fr, en, ar, tz).
- **SEO**: Meta, title, description, tags.
- **Isemnisen**: Uselkim n wudem (dev, ops, devops, admin, azay…).
- **Imtihanen**: Lint, tawuri, uskan, tawaḍit DevOps.
- **Aseggas n tmedyazt**: Ulac tazwara d isemlal ur nelli d n tmurt, monitoring n tmurt d amezwaru.

---

## 🚀 Structure & Bonnes pratiques / Best Practices

- Placez vos fichiers `.html` ici.
- Respectez la [policy.md](./policy.md) pour chaque template.
- Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- Ajoutez les balises `<html lang="">`, `<meta>`, `<title>`, et ARIA.
- Ne jamais afficher de secret, token, mot de passe, clé ou information d’infrastructure.
- Pour chaque nouveau template, ajoutez un test d’accessibilité, de rendu et de conformité DevOps.

---

## 🧩 Exemple de template conforme

```django
{# filepath: it_devops/example.html #}
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}{% trans "Accueil DevOps" %}{% endblock %}</title>
  <meta name="description" content="{% trans 'Plateforme DevOps souveraine, sécurisée et conforme' %}">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% block extra_meta %}{% endblock %}
</head>
<body>
  <header>
    <h1>{% trans "Bienvenue sur la plateforme DevOps souveraine" %}</h1>
    {% if user.is_authenticated %}
      <p>{% trans "Connecté en tant que" %} {{ user.username }}</p>
      {% if user.is_superuser %}
        <span class="role">{% trans "Administrateur" %}</span>
      {% elif user.groups|length > 0 %}
        <span class="role">{% trans "DevOps" %}</span>
      {% else %}
        <span class="role">{% trans "Dev" %}</span>
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

- Chaque template est vérifié automatiquement (lint, accessibilité, i18n, sécurité, conformité DevOps) via CI/CD.
- Pour lancer les tests localement :
  ```bash
  python manage.py test app.tests.test_templates_it_devops
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

© 2025 Dihya – Souveraineté, sécurité, accessibilité, DevSecOps, excellence.
