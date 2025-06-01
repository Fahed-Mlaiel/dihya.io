# 🌐 Dihya – Module SEO

---

## 🇫🇷 Présentation

Ce dossier contient les **templates Django** et outils pour l’optimisation SEO (Search Engine Optimization) de Dihya.
Pensé pour :
- La souveraineté numérique (open source, hébergement souverain, fallback IA open source)
- La sécurité et la conformité RGPD
- L’accessibilité et l’inclusion (multilingue : fr, en, ar, amazigh)
- La compatibilité multi-stack (Django, React, Node, Flutter…)

---

## 🚀 Fonctionnalités principales

- **Optimisation technique et sémantique** : balisage HTML5, microdata, Open Graph, Twitter Cards, JSON-LD, sitemap.xml, robots.txt
- **Multilingue** : interfaces et données en français, anglais, arabe, amazigh
- **Sécurité** : aucune fuite de données, logs anonymisés, conformité RGPD
- **Accessibilité** : RGAA/WCAG, navigation clavier, ARIA
- **Extensible** : plugins, API REST/GraphQL, intégration mobile/web
- **Fallback IA open source** : suggestion de balisage, analyse SEO

---

## 🛠️ Exemple d’intégration Django

```django
{% load seo_tags %}
<title>{% seo_title page_title %}</title>
<meta name="description" content="{% seo_description page_description %}">
<meta property="og:title" content="{% seo_og_title page_title %}">
<meta property="og:description" content="{% seo_og_description page_description %}">
<link rel="canonical" href="{% seo_canonical request %}">
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Optimisation SEO complète
- **English**: Full SEO optimization
- **العربية**: تحسين سيو متكامل
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⴳⴳⴰⵔⴰⵡ ⵏ SEO ⴷⴰⵏⴰⵡⴰⵏⴰⵏ

---

## 🔒 Sécurité & Souveraineté

- Aucune donnée personnelle collectée sans consentement explicite
- Logs SEO anonymisés, stockage souverain
- Hébergement souverain, code open source

---

## 🧩 Extensibilité

- Personnalisation via plugins Django/React
- API REST/GraphQL prête à l’emploi
- Compatible mobile (Flutter, PWA)

---

## 🧪 Tests & Qualité

- Templates et scripts testés (unitaires, intégration, accessibilité)
- Zéro warning, zéro erreur CI/CD
- Compatible GitHub Actions & Codespaces

---

## 📄 Documentation associée

- [Politique SEO](./policy.md)
- [Guide API SEO](../../../../docs/api_seo.md)
- [Tests](../../../../tests/seo/)

---

## 🏁 Démarrage rapide

1. Copier les templates dans votre projet Django :
   ```bash
   cp -r ./templates/seo/ <votre_app>/templates/seo/
   ```
2. Ajouter `seo` à `INSTALLED_APPS` dans `settings.py`
3. Configurer les langues dans `settings.py` :
   ```python
   LANGUAGES = [
       ('fr', 'Français'),
       ('en', 'English'),
       ('ar', 'العربية'),
       ('ber', 'ⵜⴰⵎⴰⵣⵉⵖⵜ'),
   ]
   ```
4. Lancer les tests :
   ```bash
   python manage.py test seo
   ```

---

## 🤝 Contribution

- Contributions, issues et suggestions bienvenues sur [GitHub](https://github.com/DihyaOrg/Dihya)
- Respect du [Code de Conduite](../../../../CODE_OF_CONDUCT.md)

---

## 🏆 Licence

Projet open source sous licence AGPLv3 – Respect de la souveraineté numérique.

---

> Ce module SEO est prêt à l’emploi, sécurisé, multilingue, accessible et souverain.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
