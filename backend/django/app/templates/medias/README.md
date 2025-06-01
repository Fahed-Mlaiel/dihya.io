# 🎥 Dihya – Medias Templates

---

## 🇫🇷 Présentation

Ce dossier contient les templates HTML du module **medias** (gestion de médias, DAM, streaming, galerie, upload, etc.) de Dihya.
Ils sont conçus pour garantir : sécurité, accessibilité, confidentialité, souveraineté numérique, conformité médias (RGPD, droits d’auteur, accessibilité), internationalisation, SEO, modularité.

- **Stack compatible** : Django, Jinja2, moteurs alternatifs, IA open source, DAM, streaming souverain, watermarking, CDN souverain.
- **Sécurité** : Pas de données personnelles, information sensible, ou secret média, pas de scripts inline, conformité RGPD/vie privée, gestion droits médias.
- **Accessibilité** : RGAA/WCAG, navigation clavier, ARIA, contrastes, médias alternatifs.
- **i18n** : Prise en charge multilingue (français, anglais, arabe, amazigh).
- **SEO** : Balises meta, titres, descriptions, données structurées.
- **Rôles** : Gestion dynamique des rôles utilisateur (gestionnaire médias, contributeur, admin, invité…).
- **Tests** : Couverture automatique (lint, accessibilité, rendu, conformité médias).
- **Souveraineté** : Aucun appel à des ressources externes non souveraines, CDN/streaming souverain uniquement, conformité RGPD, mentions légales.

---

## 🇬🇧 Overview

This folder contains the **medias** module HTML templates for Dihya (media management, DAM, streaming, gallery, upload, etc.).
Designed for : security, accessibility, privacy, digital sovereignty, media compliance (GDPR, copyright, accessibility), i18n, SEO, modularity.

- **Stack compatible**: Django, Jinja2, alternative engines, open source AI, DAM, sovereign streaming, watermarking, sovereign CDN.
- **Security**: No personal data, sensitive info, or media secrets, no inline scripts, GDPR/privacy compliant, media rights management.
- **Accessibility**: RGAA/WCAG, keyboard nav, ARIA, contrast, alternative media.
- **i18n**: Multilingual support (French, English, Arabic, Amazigh).
- **SEO**: Meta tags, titles, descriptions, structured data.
- **Roles**: Dynamic user role management (media manager, contributor, admin, guest…).
- **Tests**: Automatic coverage (lint, accessibility, rendering, media compliance).
- **Sovereignty**: No calls to non-sovereign external resources, only sovereign CDN/streaming, GDPR compliance, legal notices.

---

## 🇦🇪 مقدمة

يحتوي هذا المجلد على قوالب HTML لوحدة "الوسائط" في ديهيا (إدارة الوسائط، البث، المعرض، التحميل...).
مصممة للأمان، الخصوصية، الوصول، السيادة الرقمية، التوافق الإعلامي (RGPD، حقوق النشر، الوصول)، التعدد اللغوي، تحسين محركات البحث، التمدد.

- **التوافق**: Django، Jinja2، محركات أخرى، ذكاء اصطناعي مفتوح المصدر، DAM، بث سيادي، علامات مائية، CDN سيادي.
- **الأمان**: لا بيانات شخصية أو معلومات حساسة أو أسرار وسائط، لا سكريبتات داخلية، متوافق مع GDPR/خصوصية المستخدمين، إدارة حقوق الوسائط.
- **الوصول**: معايير RGAA/WCAG، تنقل لوحة المفاتيح، ARIA، تباين، وسائط بديلة.
- **تعدد اللغات**: دعم الفرنسية، الإنجليزية، العربية، الأمازيغية.
- **SEO**: وسوم meta، عناوين، أوصاف، بيانات منظمة.
- **الأدوار**: إدارة ديناميكية للأدوار (مدير وسائط، مساهم، مشرف، زائر...).
- **الاختبارات**: تغطية تلقائية (lint، وصول، عرض، توافق وسائط).
- **السيادة**: لا موارد خارجية غير سيادية، CDN وبث سيادي فقط، توافق RGPD، إشعارات قانونية.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n HTML n uγmis "medias" n Dihya (amedya, upload, gallery, streaming...).
Iɣewwaṛen i taɣult, tawuri, uslig, tmedyazt, tawaḍit n medias, tamyizt, SEO, tmedyazt.

- **Tawuri**: Ulac isefka ur nelli d asensi, isefka uslig, neɣ asensi n medias, ulac script deg templates.
- **Tawuri n wudem**: RGAA/WCAG, tawuri n tneflit, ARIA, tawuri n tneflit n amedya.
- **Tamyizt**: Tamulti (fr, en, ar, tz).
- **SEO**: Meta, title, description, tags.
- **Isemnisen**: Uselkim n wudem (media manager, contributor, admin, azay…).
- **Imtihanen**: Lint, tawuri, uskan, tawaḍit n medias.
- **Aseggas n tmedyazt**: Ulac tazwara d isemlal ur nelli d n tmurt, CDN/streaming n tmurt kan, RGPD ilaq ad yili, tazwart n taseddast ilaq ad tili.

---

## 🚀 Structure & Bonnes pratiques / Best Practices

- Placez vos fichiers `.html` ici.
- Respectez la [policy.md](./policy.md) pour chaque template.
- Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- Ajoutez les balises `<html lang="">`, `<meta>`, `<title>`, ARIA, et attributs d’accessibilité sur les médias.
- Ne jamais afficher d’information média confidentielle ou de donnée personnelle.
- Pour chaque nouveau template, ajoutez un test d’accessibilité, de rendu et de conformité médias.

---

## 🧩 Exemple de template conforme

```django
{# filepath: medias/example.html #}
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}{% trans "Accueil Médiathèque" %}{% endblock %}</title>
  <meta name="description" content="{% trans 'Plateforme médias souveraine, conforme RGPD et sécurisée' %}">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% block extra_meta %}{% endblock %}
</head>
<body>
  <header>
    <h1>{% trans "Bienvenue sur la médiathèque souveraine" %}</h1>
    {% if user.is_authenticated %}
      <p>{% trans "Connecté en tant que" %} {{ user.username }}</p>
      {% if user.is_superuser %}
        <span class="role">{% trans "Administrateur" %}</span>
      {% elif user.groups|length > 0 %}
        <span class="role">{% trans "Gestionnaire médias" %}</span>
      {% else %}
        <span class="role">{% trans "Contributeur" %}</span>
      {% endif %}
    {% else %}
      <a href="{% url 'login' %}">{% trans "Connexion" %}</a>
    {% endif %}
  </header>
  <main>
    <img src="{% static 'medias/exemple.jpg' %}" alt="{% trans 'Exemple média' %}" />
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

- Chaque template est vérifié automatiquement (lint, accessibilité, i18n, sécurité, conformité médias) via CI/CD.
- Pour lancer les tests localement :
  ```bash
  python manage.py test app.tests.test_templates_medias
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

© 2025 Dihya – Souveraineté, sécurité, accessibilité, conformité médias, excellence.
