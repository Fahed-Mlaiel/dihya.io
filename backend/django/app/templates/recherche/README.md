# 🔎 Dihya – Module Recherche

---

## 🇫🇷 Présentation

Ce dossier contient les **templates Django** pour le module de recherche de Dihya.
Il est conçu pour offrir :
- Une expérience utilisateur multilingue (français, anglais, arabe, amazigh)
- Une sécurité et une souveraineté numérique maximales
- Une accessibilité totale (RGAA/WCAG)
- Une compatibilité multi-stack (Django, React, Node, Flutter…)

---

## 🚀 Fonctionnalités principales

- **Recherche avancée** (full-text, filtres dynamiques, suggestions IA)
- **Support multilingue** (i18n natif, fallback open source)
- **Gestion des rôles** (admin, utilisateur, invité)
- **Sécurité** : protection CSRF, XSS, gestion fine des permissions
- **Accessibilité** : navigation clavier, ARIA, contraste optimisé
- **SEO** : balisage sémantique, microdata, performance optimale

---

## 🛠️ Exemple d’intégration

```django
{% extends "base.html" %}
{% load i18n %}
{% block content %}
  <h1>{% trans "Recherche" %}</h1>
  <form method="get" action="{% url 'recherche:resultats' %}">
    <input type="text" name="q" placeholder="{% trans 'Votre recherche...' %}" aria-label="{% trans 'Recherche' %}">
    <button type="submit">{% trans "Chercher" %}</button>
  </form>
{% endblock %}
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Interface et résultats en français
- **English**: Interface and results in English
- **العربية**: واجهة ونتائج باللغة العربية
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⵏⴰⵡⴰⵏ ⴷ ⴰⵎⴰⵣⵉⵖⴰⵏ

---

## 🔒 Sécurité & Souveraineté

- Chiffrement des requêtes et des résultats
- Aucune donnée transmise à des tiers
- Compatible avec IA open source fallback (GPT4All, Mistral…)

---

## 🧩 Extensibilité

- Personnalisation facile via plugins Django ou React
- Prêt pour intégration API REST/GraphQL
- Compatible mobile (Flutter, PWA)

---

## 🧪 Tests & Qualité

- Templates testés (unitaires, intégration, accessibilité)
- Aucun warning, aucune erreur CI/CD
- Compatible GitHub Actions & Codespaces

---

## 📄 Documentation associée

- [Politique d’utilisation](./policy.md)
- [Guide d’intégration API](../../../../docs/api_recherche.md)
- [Tests](../../../../tests/recherche/)

---

## 🏁 Démarrage rapide

1. Copier les templates dans votre projet Django :
   ```bash
   cp -r ./templates/recherche/ <votre_app>/templates/recherche/
   ```
2. Ajouter `recherche` à `INSTALLED_APPS` dans `settings.py`
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
   python manage.py test recherche
   ```

---

## 🤝 Contribution

- Contributions, issues et suggestions bienvenues sur [GitHub](https://github.com/DihyaOrg/Dihya)
- Respect du [Code de Conduite](../../../../CODE_OF_CONDUCT.md)

---

## 🏆 Licence

Projet open source sous licence AGPLv3 – Respect de la souveraineté numérique.

---

> Ce module est prêt à l’emploi, sécurisé, multilingue, accessible et souverain.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
