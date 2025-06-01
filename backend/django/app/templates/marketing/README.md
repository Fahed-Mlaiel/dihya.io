# 📈 Dihya – Marketing Templates

---

## 🇫🇷 Présentation

Ce dossier contient les templates HTML du module **marketing** de Dihya.
Ils sont conçus pour garantir : sécurité, accessibilité, confidentialité, souveraineté numérique, conformité marketing (RGPD, analytics souverain), internationalisation, SEO, modularité.

- **Stack compatible** : Django, Jinja2, moteurs alternatifs, IA open source, analytics souverain, campagnes multicanal.
- **Sécurité** : Pas de données personnelles, information sensible, ou secret marketing, pas de scripts inline, conformité RGPD/vie privée.
- **Accessibilité** : RGAA/WCAG, navigation clavier, ARIA, contrastes.
- **i18n** : Prise en charge multilingue (français, anglais, arabe, amazigh).
- **SEO** : Balises meta, titres, descriptions, données structurées.
- **Rôles** : Gestion dynamique des rôles utilisateur (marketeur, analyste, admin, invité…).
- **Tests** : Couverture automatique (lint, accessibilité, rendu, conformité marketing).
- **Souveraineté** : Aucun appel à des ressources externes non souveraines, analytics souverain uniquement, conformité RGPD, mentions légales.

---

## 🇬🇧 Overview

This folder contains the **marketing** module HTML templates for Dihya.
Designed for : security, accessibility, privacy, digital sovereignty, marketing compliance (GDPR, sovereign analytics), i18n, SEO, modularity.

- **Stack compatible**: Django, Jinja2, alternative engines, open source AI, sovereign analytics, multichannel campaigns.
- **Security**: No personal data, sensitive info, or marketing secrets, no inline scripts, GDPR/privacy compliant.
- **Accessibility**: RGAA/WCAG, keyboard nav, ARIA, contrast.
- **i18n**: Multilingual support (French, English, Arabic, Amazigh).
- **SEO**: Meta tags, titles, descriptions, structured data.
- **Roles**: Dynamic user role management (marketer, analyst, admin, guest…).
- **Tests**: Automatic coverage (lint, accessibility, rendering, marketing compliance).
- **Sovereignty**: No calls to non-sovereign external resources, only sovereign analytics, GDPR compliance, legal notices.

---

## 🇦🇪 مقدمة

يحتوي هذا المجلد على قوالب HTML لوحدة "التسويق" في ديهيا.
مصممة للأمان، الخصوصية، الوصول، السيادة الرقمية، التوافق التسويقي (RGPD، تحليلات سيادية)، التعدد اللغوي، تحسين محركات البحث، التمدد.

- **التوافق**: Django، Jinja2، محركات أخرى، ذكاء اصطناعي مفتوح المصدر، تحليلات سيادية، حملات متعددة القنوات.
- **الأمان**: لا بيانات شخصية أو معلومات حساسة أو أسرار تسويقية، لا سكريبتات داخلية، متوافق مع GDPR/خصوصية المستخدمين.
- **الوصول**: معايير RGAA/WCAG، تنقل لوحة المفاتيح، ARIA.
- **تعدد اللغات**: دعم الفرنسية، الإنجليزية، العربية، الأمازيغية.
- **SEO**: وسوم meta، عناوين، أوصاف، بيانات منظمة.
- **الأدوار**: إدارة ديناميكية للأدوار (مسوق، محلل، مشرف، زائر...).
- **الاختبارات**: تغطية تلقائية (lint، وصول، عرض، توافق تسويقي).
- **السيادة**: لا موارد خارجية غير سيادية، تحليلات سيادية فقط، توافق RGPD، إشعارات قانونية.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n HTML n uγmis "marketing" n Dihya.
Iɣewwaṛen i taɣult, tawuri, uslig, tmedyazt, tawaḍit n marketing, tamyizt, SEO, tmedyazt.

- **Tawuri**: Ulac isefka ur nelli d asensi, isefka uslig, neɣ asensi n marketing, ulac script deg templates.
- **Tawuri n wudem**: RGAA/WCAG, tawuri n tneflit, ARIA.
- **Tamyizt**: Tamulti (fr, en, ar, tz).
- **SEO**: Meta, title, description, tags.
- **Isemnisen**: Uselkim n wudem (marketer, analyst, admin, azay…).
- **Imtihanen**: Lint, tawuri, uskan, tawaḍit n marketing.
- **Aseggas n tmedyazt**: Ulac tazwara d isemlal ur nelli d n tmurt, analytics n tmurt kan, RGPD ilaq ad yili, tazwart n taseddast ilaq ad tili.

---

## 🚀 Structure & Bonnes pratiques / Best Practices

- Placez vos fichiers `.html` ici.
- Respectez la [policy.md](./policy.md) pour chaque template.
- Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- Ajoutez les balises `<html lang="">`, `<meta>`, `<title>`, et ARIA.
- Ne jamais afficher d’information marketing confidentielle ou de donnée personnelle.
- Pour chaque nouveau template, ajoutez un test d’accessibilité, de rendu et de conformité marketing.

---

## 🧩 Exemple de template conforme

```django
{# filepath: marketing/example.html #}
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}{% trans "Accueil Marketing" %}{% endblock %}</title>
  <meta name="description" content="{% trans 'Plateforme marketing souveraine, conforme RGPD et sécurisée' %}">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% block extra_meta %}{% endblock %}
</head>
<body>
  <header>
    <h1>{% trans "Bienvenue sur la plateforme marketing souveraine" %}</h1>
    {% if user.is_authenticated %}
      <p>{% trans "Connecté en tant que" %} {{ user.username }}</p>
      {% if user.is_superuser %}
        <span class="role">{% trans "Administrateur" %}</span>
      {% elif user.groups|length > 0 %}
        <span class="role">{% trans "Marketeur" %}</span>
      {% else %}
        <span class="role">{% trans "Analyste" %}</span>
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

- Chaque template est vérifié automatiquement (lint, accessibilité, i18n, sécurité, conformité marketing) via CI/CD.
- Pour lancer les tests localement :
  ```bash
  python manage.py test app.tests.test_templates_marketing
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

© 2025 Dihya – Souveraineté, sécurité, accessibilité, conformité marketing, excellence.
