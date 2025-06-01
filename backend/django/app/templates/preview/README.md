# 👁️ Dihya – Preview Templates

---

## 🇫🇷 Présentation

Ce dossier contient les templates HTML du module **preview** de Dihya (prévisualisation de contenus, assets, médias, documents, etc.).
Ils sont conçus pour garantir : sécurité, accessibilité, confidentialité, souveraineté numérique, conformité preview (RGPD, droits d’auteur, accessibilité), internationalisation, SEO, modularité, compatibilité multi-stack.

- **Stack compatible** : Django, Jinja2, moteurs alternatifs, IA open source, preview souverain, watermarking, audit, fallback IA.
- **Sécurité** : Pas de données personnelles, information sensible, ou secret preview, pas de scripts inline, conformité RGPD/vie privée, gestion droits preview.
- **Accessibilité** : RGAA/WCAG, navigation clavier/tactile, ARIA, responsive, contrastes.
- **i18n** : Prise en charge multilingue (français, anglais, arabe, amazigh).
- **SEO** : Balises meta, titres, descriptions, données structurées.
- **Rôles** : Gestion dynamique des rôles utilisateur (lecteur, éditeur, admin, invité…).
- **Tests** : Couverture automatique (lint, accessibilité, rendu, conformité preview).
- **Souveraineté** : Aucun appel à des ressources externes non souveraines, preview souverain uniquement, conformité RGPD, mentions légales.

---

## 🇬🇧 Overview

This folder contains the **preview** module HTML templates for Dihya (content, asset, media, document preview, etc.).
Designed for : security, accessibility, privacy, digital sovereignty, preview compliance (GDPR, copyright, accessibility), i18n, SEO, modularity, multi-stack compatibility.

- **Stack compatible**: Django, Jinja2, alternative engines, open source AI, sovereign preview, watermarking, audit, fallback AI.
- **Security**: No personal data, sensitive info, or preview secrets, no inline scripts, GDPR/privacy compliant, preview rights management.
- **Accessibility**: RGAA/WCAG, keyboard/touch nav, ARIA, responsive, contrast.
- **i18n**: Multilingual support (French, English, Arabic, Amazigh).
- **SEO**: Meta tags, titles, descriptions, structured data.
- **Roles**: Dynamic user role management (reader, editor, admin, guest…).
- **Tests**: Automatic coverage (lint, accessibility, rendering, preview compliance).
- **Sovereignty**: No calls to non-sovereign external resources, only sovereign preview, GDPR compliance, legal notices.

---

## 🇦🇪 مقدمة

يحتوي هذا المجلد على قوالب HTML لوحدة "المعاينة" في ديهيا (معاينة محتوى، وسائط، مستندات...).
مصممة للأمان، الخصوصية، الوصول، السيادة الرقمية، التوافق مع المعاينة (RGPD، حقوق النشر، الوصول)، التعدد اللغوي، تحسين محركات البحث، التمدد، التوافق مع عدة تقنيات.

- **التوافق**: Django، Jinja2، محركات أخرى، ذكاء اصطناعي مفتوح المصدر، معاينة سيادية، وسم مائي، تدقيق، ذكاء اصطناعي بديل.
- **الأمان**: لا بيانات شخصية أو معلومات حساسة أو أسرار معاينة، لا سكريبتات داخلية، متوافق مع GDPR/خصوصية المستخدمين، إدارة حقوق المعاينة.
- **الوصول**: معايير RGAA/WCAG، دعم لوحة المفاتيح/اللمس، ARIA، استجابة التصميم، تباين.
- **تعدد اللغات**: دعم الفرنسية، الإنجليزية، العربية، الأمازيغية.
- **SEO**: وسوم meta، عناوين، أوصاف، بيانات منظمة.
- **الأدوار**: إدارة ديناميكية للأدوار (قارئ، محرر، مشرف، زائر...).
- **الاختبارات**: تغطية تلقائية (lint، وصول، عرض، توافق معاينة).
- **السيادة**: لا موارد خارجية غير سيادية، معاينة سيادية فقط، توافق RGPD، إشعارات قانونية.

---

## ⵜⴰⵎⴰⵣⵉⵖ ⴰⵙⵏⴼⴰⵡ

Asegwas agi yegber templates n HTML n uγmis "preview" n Dihya (tawuri n preview n ugbur, amedya, isefka...).
Iɣewwaṛen i taɣult, tawuri, uslig, tmedyazt, tawaḍit n preview, tamyizt, SEO, tmedyazt, amsawal n multi-stack.

- **Tawuri**: Ulac isefka ur nelli d asensi, isefka uslig, neɣ asensi n preview, ulac script deg templates.
- **Tawuri n wudem**: RGAA/WCAG, tawuri n tneflit, ARIA, responsive, tawuri n tneflit n preview.
- **Tamyizt**: Tamulti (fr, en, ar, tz).
- **SEO**: Meta, title, description, tags.
- **Isemnisen**: Uselkim n wudem (reader, editor, admin, azay…).
- **Imtihanen**: Lint, tawuri, uskan, tawaḍit n preview.
- **Aseggas n tmedyazt**: Ulac tazwara d isemlal ur nelli d n tmurt, preview n tmurt kan, RGPD ilaq ad yili, tazwart n taseddast ilaq ad tili.

---

## 🚀 Structure & Bonnes pratiques / Best Practices

- Placez vos fichiers `.html` ici.
- Respectez la [policy.md](./policy.md) pour chaque template.
- Utilisez `{% trans %}` ou `{% blocktrans %}` pour tout texte affiché.
- Ajoutez les balises `<html lang="">`, `<meta>`, `<title>`, ARIA, et attributs d’accessibilité sur les images.
- Ne jamais afficher d’information preview confidentielle ou de donnée personnelle.
- Pour chaque nouveau template, ajoutez un test d’accessibilité, de rendu et de conformité preview.

---

## 🧩 Exemple de template conforme

```django
{# filepath: preview/example.html #}
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}{% trans "Aperçu de document" %}{% endblock %}</title>
  <meta name="description" content="{% trans 'Prévisualisation souveraine, conforme RGPD et sécurisée' %}">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  {% block extra_meta %}{% endblock %}
</head>
<body>
  <header>
    <h1>{% trans "Prévisualisation de document" %}</h1>
    {% if user.is_authenticated %}
      <p>{% trans "Connecté en tant que" %} {{ user.username }}</p>
      {% if user.is_superuser %}
        <span class="role">{% trans "Administrateur" %}</span>
      {% elif user.groups|length > 0 %}
        <span class="role">{% trans "Éditeur" %}</span>
      {% else %}
        <span class="role">{% trans "Lecteur" %}</span>
      {% endif %}
    {% else %}
      <a href="{% url 'login' %}">{% trans "Connexion" %}</a>
    {% endif %}
  </header>
  <main>
    <img src="{% static 'preview/doc.jpg' %}" alt="{% trans 'Document à prévisualiser' %}" />
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

- Chaque template est vérifié automatiquement (lint, accessibilité, i18n, sécurité, conformité preview) via CI/CD.
- Pour lancer les tests localement :
  ```bash
  python manage.py test app.tests.test_templates_preview
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

© 2025 Dihya – Souveraineté, sécurité, accessibilité, conformité preview, excellence.
