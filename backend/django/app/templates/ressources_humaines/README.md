# 👥 Dihya – Module Ressources Humaines (RH)

---

## 🇫🇷 Présentation

Ce dossier contient les **templates Django** et outils pour la gestion des ressources humaines (RH) de Dihya.
Pensé pour :
- La souveraineté numérique (open source, hébergement souverain, fallback IA open source)
- La sécurité et la conformité RGPD
- L’accessibilité et l’inclusion (multilingue : fr, en, ar, amazigh)
- La compatibilité multi-stack (Django, React, Node, Flutter…)

---

## 🚀 Fonctionnalités principales

- **Gestion RH avancée** : profils, rôles, permissions, audit, historique
- **Multilingue** : interfaces et données en français, anglais, arabe, amazigh
- **Sécurité** : chiffrement, gestion fine des accès, auditabilité, conformité RGPD
- **Accessibilité** : RGAA/WCAG, navigation clavier, ARIA
- **Extensible** : plugins, API REST/GraphQL, intégration mobile/web
- **Fallback IA open source** : suggestion, matching, analyse RH

---

## 🛠️ Exemple d’intégration Django

```django
{% extends "base.html" %}
{% load i18n %}
{% block content %}
  <h1>{% trans "Gestion RH" %}</h1>
  <form method="post" action="{% url 'ressources_humaines:ajouter' %}">
    {% csrf_token %}
    <input type="text" name="nom" placeholder="{% trans 'Nom' %}" required>
    <input type="email" name="email" placeholder="{% trans 'Email' %}" required>
    <button type="submit">{% trans "Ajouter" %}</button>
  </form>
{% endblock %}
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Gestion RH complète
- **English**: Full HR management
- **العربية**: إدارة موارد بشرية متكاملة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⴷⴷⴰⵔⴰⵏ ⵏ ⵓⵙⴻⵏⴰⵡⴰⵏ

---

## 🔒 Sécurité & Souveraineté

- Chiffrement AES-256, TLS 1.3
- Authentification forte (SSO, 2FA)
- Journalisation, audit, alertes
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

- [Politique RH](./policy.md)
- [Guide API RH](../../../../docs/api_rh.md)
- [Tests](../../../../tests/ressources_humaines/)

---

## 🏁 Démarrage rapide

1. Copier les templates dans votre projet Django :
   ```bash
   cp -r ./templates/ressources_humaines/ <votre_app>/templates/ressources_humaines/
   ```
2. Ajouter `ressources_humaines` à `INSTALLED_APPS` dans `settings.py`
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
   python manage.py test ressources_humaines
   ```

---

## 🤝 Contribution

- Contributions, issues et suggestions bienvenues sur [GitHub](https://github.com/DihyaOrg/Dihya)
- Respect du [Code de Conduite](../../../../CODE_OF_CONDUCT.md)

---

## 🏆 Licence

Projet open source sous licence AGPLv3 – Respect de la souveraineté numérique.

---

> Ce module RH est prêt à l’emploi, sécurisé, multilingue, accessible et souverain.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
