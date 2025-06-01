# 🔬 Dihya – Module Science

---

## 🇫🇷 Présentation

Ce dossier contient les **templates Django** et outils pour la gestion des activités scientifiques (expériences, projets, laboratoires, publications, etc.) de Dihya.
Pensé pour :
- La souveraineté numérique (open source, hébergement souverain, fallback IA open source)
- La sécurité et la conformité RGPD/science
- L’accessibilité et l’inclusion (multilingue : fr, en, ar, amazigh)
- La compatibilité multi-stack (Django, React, Node, Flutter…)

---

## 🚀 Fonctionnalités principales

- **Gestion des projets scientifiques** : expériences, laboratoires, publications, suivi, audit
- **Multilingue** : interfaces et données en français, anglais, arabe, amazigh
- **Sécurité** : chiffrement, gestion fine des accès, auditabilité, conformité RGPD
- **Accessibilité** : RGAA/WCAG, navigation clavier, ARIA
- **Extensible** : plugins, API REST/GraphQL, intégration mobile/web
- **Fallback IA open source** : suggestion d’expériences, analyse scientifique

---

## 🛠️ Exemple d’intégration Django

```django
{% extends "base.html" %}
{% load i18n %}
{% block content %}
  <h1>{% trans "Projet scientifique" %}</h1>
  <form method="post" action="{% url 'science:ajouter' %}">
    {% csrf_token %}
    <input type="text" name="titre" placeholder="{% trans 'Titre du projet' %}" required>
    <textarea name="description" placeholder="{% trans 'Description scientifique' %}"></textarea>
    <button type="submit">{% trans "Enregistrer" %}</button>
  </form>
{% endblock %}
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Gestion science complète
- **English**: Full science management
- **العربية**: إدارة علمية متكاملة
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

- [Politique science](./policy.md)
- [Guide API science](../../../../docs/api_science.md)
- [Tests](../../../../tests/science/)

---

## 🏁 Démarrage rapide

1. Copier les templates dans votre projet Django :
   ```bash
   cp -r ./templates/science/ <votre_app>/templates/science/
   ```
2. Ajouter `science` à `INSTALLED_APPS` dans `settings.py`
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
   python manage.py test science
   ```

---

## 🤝 Contribution

- Contributions, issues et suggestions bienvenues sur [GitHub](https://github.com/DihyaOrg/Dihya)
- Respect du [Code de Conduite](../../../../CODE_OF_CONDUCT.md)

---

## 🏆 Licence

Projet open source sous licence AGPLv3 – Respect de la souveraineté numérique.

---

> Ce module science est prêt à l’emploi, sécurisé, multilingue, accessible et souverain.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
