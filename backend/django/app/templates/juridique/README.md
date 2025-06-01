# ⚖️ Dihya – Juridique Templates

---

## 🇫🇷 Présentation

Ce dossier contient les templates HTML du module **juridique** de Dihya.
Ils sont conçus pour garantir : sécurité, accessibilité, confidentialité, souveraineté numérique, conformité juridique (RGPD, obligations légales), internationalisation, SEO, modularité.

- **Stack compatible** : Django, Jinja2, moteurs alternatifs, IA open source, audit, conformité RGPD.
- **Sécurité** : Pas de données personnelles, clause confidentielle, secret, ou information juridique sensible, pas de scripts inline, conformité RGPD/vie privée.
- **Accessibilité** : RGAA/WCAG, navigation clavier, ARIA, contrastes.
- **i18n** : Prise en charge multilingue (français, anglais, arabe, amazigh).
- **SEO** : Balises meta, titres, descriptions, données structurées.
- **Rôles** : Gestion dynamique des rôles utilisateur (juriste, avocat, admin, invité…).
- **Tests** : Couverture automatique (lint, accessibilité, rendu, conformité juridique).
- **Souveraineté** : Aucun appel à des ressources externes non souveraines, conformité RGPD, mentions légales.

---

## 🇬🇧 Overview

This folder contains the **juridique** (legal) module HTML templates for Dihya.
Designed for : security, accessibility, privacy, digital sovereignty, legal compliance (GDPR, legal obligations), i18n, SEO, modularity.

- **Stack compatible**: Django, Jinja2, alternative engines, open source AI, audit, GDPR compliance.
- **Security**: No personal data, confidential clause, secret, or sensitive legal info, no inline scripts, GDPR/privacy compliant.
- **Accessibility**: RGAA/WCAG, keyboard nav, ARIA, contrast.
- **i18n**: Multilingual support (French, English, Arabic, Amazigh).
- **SEO**: Meta tags, titles, descriptions, structured data.
- **Roles**: Dynamic user role management (legal expert, lawyer, admin, guest…).
- **Tests**: Automatic coverage (lint, accessibility, rendering, legal compliance).
- **Sovereignty**: No calls to non-sovereign external resources, GDPR compliance, legal notices.

---

## 🇦🇪 مقدمة

يحتوي هذا المجلد على قوالب HTML لوحدة "القانون" في ديهيا.
مصممة للأمان، الخصوصية، الوصول، السيادة الرقمية، التوافق القانوني (RGPD)، التعدد اللغوي، تحسين محركات البحث، التمدد.

- **التوافق**: Django، Jinja2، محركات أخرى، ذكاء اصطناعي مفتوح المصدر، تدقيق، توافق RGPD.
- **الأمان**: لا بيانات شخصية أو بنود سرية أو أسرار أو معلومات قانونية حساسة، لا سكريبتات داخلية، متوافق مع GDPR/خصوصية المستخدمين.
- **الوصول**: معايير RGAA/WCAG، تنقل لوحة المفاتيح، ARIA.
- **تعدد اللغات**: دعم الفرنسية، الإنجليزية، العربية، الأمازيغية.
- **SEO**: وسوم meta، عناوين، أوصاف، بيانات منظمة.
- **الأدوار**: إدارة ديناميكية للأدوار (خبير قانوني، محامي، مشرف، زائر...).
- **الاختبارات**: تغطية تلقائية (lint، وصول، عرض، توافق قانوني).
- **السيادة**: لا موارد خارجية غير سيادية، توافق RGPD، إشعارات قانونية.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n HTML n uγmis "juridique" n Dihya.
Iɣewwaṛen i taɣult, tawuri, uslig, tmedyazt, tawaḍit n taseddast, tamyizt, SEO, tmedyazt.

- **Tawuri**: Ulac isefka ur nelli d asensi, clause uslig, secret, neɣ isefka n tneflit n taseddast, ulac script deg templates.
- **Tawuri n wudem**: RGAA/WCAG, tawuri n tneflit, ARIA.
- **Tamyizt**: Tamulti (fr, en, ar, tz).
- **SEO**: Meta, title, description, tags.
- **Isemnisen**: Uselkim n wudem (ajurist, amnas, admin, azay…).
- **Imtihanen**: Lint, tawuri, uskan, tawaḍit n taseddast.
- **Aseggas n tmedyazt**: Ulac tazwara d isemlal ur nelli d n tmurt, RGPD ilaq ad yili, tazwart n taseddast ilaq ad tili.

---

## 🚀 Structure & Bonnes pratiques / Best Practices

- Placez vos fichiers `.html` ici.
- Respectez la [policy.md](./policy.md) pour chaque template.
- Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- Ajoutez les balises `<html lang="">`, `<meta>`, `<title>`, et ARIA.
- Ne jamais afficher de clause confidentielle, donnée personnelle ou information juridique sensible.
- Pour chaque nouveau template, ajoutez un test d’accessibilité, de rendu et de conformité juridique.

---

## 🧩 Exemple de template conforme

```django
{# filepath: juridique/example.html #}
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}{% trans "Accueil Juridique" %}{% endblock %}</title>
  <meta name="description" content="{% trans 'Plateforme juridique souveraine, conforme RGPD et sécurisée' %}">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% block extra_meta %}{% endblock %}
</head>
<body>
  <header>
    <h1>{% trans "Bienvenue sur la plateforme juridique souveraine" %}</h1>
    {% if user.is_authenticated %}
      <p>{% trans "Connecté en tant que" %} {{ user.username }}</p>
      {% if user.is_superuser %}
        <span class="role">{% trans "Administrateur" %}</span>
      {% elif user.groups|length > 0 %}
        <span class="role">{% trans "Juriste" %}</span>
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
    <a href="{% url 'legal_mentions' %}">{% trans "Mentions légales" %}</a>
  </footer>
</body>
</html>
```

---

## 🧪 Tests & CI

- Chaque template est vérifié automatiquement (lint, accessibilité, i18n, sécurité, conformité juridique) via CI/CD.
- Pour lancer les tests localement :
  ```bash
  python manage.py test app.tests.test_templates_juridique
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

© 2025 Dihya – Souveraineté, sécurité, accessibilité, conformité juridique, excellence.
