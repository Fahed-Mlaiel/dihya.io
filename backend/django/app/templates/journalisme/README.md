# 📰 Dihya – Journalisme Templates

---

## 🇫🇷 Présentation

Ce dossier contient les templates HTML du module **journalisme** de Dihya.
Ils sont conçus pour garantir : sécurité, accessibilité, confidentialité, souveraineté numérique, éthique journalistique, internationalisation, SEO, modularité.

- **Stack compatible** : Django, Jinja2, moteurs alternatifs, IA open source, fact-checking.
- **Sécurité** : Pas de données sensibles, source confidentielle, ou information non vérifiée, pas de scripts inline, conformité RGPD/vie privée.
- **Accessibilité** : RGAA/WCAG, navigation clavier, ARIA, contrastes.
- **i18n** : Prise en charge multilingue (français, anglais, arabe, amazigh).
- **SEO** : Balises meta, titres, descriptions, données structurées.
- **Rôles** : Gestion dynamique des rôles utilisateur (journaliste, éditeur, lecteur, admin, invité…).
- **Tests** : Couverture automatique (lint, accessibilité, rendu, conformité éthique).
- **Souveraineté** : Aucun appel à des ressources externes non souveraines, IA locale priorisée.

---

## 🇬🇧 Overview

This folder contains the **journalisme** (journalism) module HTML templates for Dihya.
Designed for : security, accessibility, privacy, digital sovereignty, journalistic ethics, i18n, SEO, modularity.

- **Stack compatible**: Django, Jinja2, alternative engines, open source AI, fact-checking.
- **Security**: No sensitive data, confidential source, or unverified info, no inline scripts, GDPR/privacy compliant.
- **Accessibility**: RGAA/WCAG, keyboard nav, ARIA, contrast.
- **i18n**: Multilingual support (French, English, Arabic, Amazigh).
- **SEO**: Meta tags, titles, descriptions, structured data.
- **Roles**: Dynamic user role management (journalist, editor, reader, admin, guest…).
- **Tests**: Automatic coverage (lint, accessibility, rendering, ethics compliance).
- **Sovereignty**: No calls to non-sovereign external resources, local AI prioritized.

---

## 🇦🇪 مقدمة

يحتوي هذا المجلد على قوالب HTML لوحدة "الصحافة" في ديهيا.
مصممة للأمان، الخصوصية، الوصول، السيادة الرقمية، أخلاقيات الصحافة، التعدد اللغوي، تحسين محركات البحث، التمدد.

- **التوافق**: Django، Jinja2، محركات أخرى، ذكاء اصطناعي مفتوح المصدر، تدقيق الحقائق.
- **الأمان**: لا بيانات حساسة أو مصادر سرية أو معلومات غير موثقة، لا سكريبتات داخلية، متوافق مع GDPR/خصوصية المستخدمين.
- **الوصول**: معايير RGAA/WCAG، تنقل لوحة المفاتيح، ARIA.
- **تعدد اللغات**: دعم الفرنسية، الإنجليزية، العربية، الأمازيغية.
- **SEO**: وسوم meta، عناوين، أوصاف، بيانات منظمة.
- **الأدوار**: إدارة ديناميكية للأدوار (صحفي، محرر، قارئ، مشرف، زائر...).
- **الاختبارات**: تغطية تلقائية (lint، وصول، عرض، توافق أخلاقي).
- **السيادة**: لا موارد خارجية غير سيادية، أولوية للذكاء الاصطناعي المحلي.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n HTML n uγmis "journalisme" n Dihya.
Iɣewwaṛen i taɣult, tawuri, uslig, tmedyazt, tawaḍit n ajurnalist, tamyizt, SEO, tmedyazt.

- **Tawuri**: Ulac isefka ur nelli d asensi, source uslig, neɣ isefka ur nettwaselkem, ulac script deg templates.
- **Tawuri n wudem**: RGAA/WCAG, tawuri n tneflit, ARIA.
- **Tamyizt**: Tamulti (fr, en, ar, tz).
- **SEO**: Meta, title, description, tags.
- **Isemnisen**: Uselkim n wudem (ajurnalist, amsefrak, agrawli, admin, azay…).
- **Imtihanen**: Lint, tawuri, uskan, tawaḍit n tawaḍit.
- **Aseggas n tmedyazt**: Ulac tazwara d isemlal ur nelli d n tmurt, IA n tmurt d amezwaru.

---

## 🚀 Structure & Bonnes pratiques / Best Practices

- Placez vos fichiers `.html` ici.
- Respectez la [policy.md](./policy.md) pour chaque template.
- Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- Ajoutez les balises `<html lang="">`, `<meta>`, `<title>`, et ARIA.
- Ne jamais afficher de source confidentielle ou d’information non vérifiée.
- Pour chaque nouveau template, ajoutez un test d’accessibilité, de rendu et de conformité éthique.

---

## 🧩 Exemple de template conforme

```django
{# filepath: journalisme/example.html #}
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}{% trans "Accueil Journalisme" %}{% endblock %}</title>
  <meta name="description" content="{% trans 'Plateforme journalistique souveraine, éthique et sécurisée' %}">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% block extra_meta %}{% endblock %}
</head>
<body>
  <header>
    <h1>{% trans "Bienvenue sur la plateforme journalistique souveraine" %}</h1>
    {% if user.is_authenticated %}
      <p>{% trans "Connecté en tant que" %} {{ user.username }}</p>
      {% if user.is_superuser %}
        <span class="role">{% trans "Administrateur" %}</span>
      {% elif user.groups|length > 0 %}
        <span class="role">{% trans "Journaliste" %}</span>
      {% else %}
        <span class="role">{% trans "Lecteur" %}</span>
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

- Chaque template est vérifié automatiquement (lint, accessibilité, i18n, sécurité, conformité éthique) via CI/CD.
- Pour lancer les tests localement :
  ```bash
  python manage.py test app.tests.test_templates_journalisme
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

© 2025 Dihya – Souveraineté, sécurité, accessibilité, éthique, excellence.
