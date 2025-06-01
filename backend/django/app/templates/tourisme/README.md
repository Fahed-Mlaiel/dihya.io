# 🏞️ Dihya – Module Tourisme

---

## 🇫🇷 Présentation

Ce dossier contient les **templates Django** et outils pour la gestion du tourisme (sites, circuits, réservations, guides, avis, notifications, etc.) de Dihya.
Pensé pour :
- La souveraineté numérique (open source, hébergement souverain, fallback IA open source)
- La sécurité avancée et la conformité RGPD/tourisme
- L’accessibilité et l’inclusion (multilingue : fr, en, ar, amazigh)
- La compatibilité multi-stack (Django, React, Node, Flutter…)

---

## 🚀 Fonctionnalités principales

- **Gestion du tourisme** : sites, circuits, réservations, guides, avis, notifications, audit
- **Multilingue** : interfaces et données en français, anglais, arabe, amazigh
- **Sécurité** : chiffrement, permissions fines, auditabilité, conformité RGPD/tourisme
- **Accessibilité** : RGAA/WCAG, navigation clavier, ARIA
- **Extensible** : plugins, API REST/GraphQL, intégration mobile/web
- **Fallback IA open source** : suggestion de circuits, analyse d’avis, recommandations

---

## 🛠️ Exemple d’intégration Django

```django
{% extends "base.html" %}
{% load i18n %}
{% block content %}
  <h1>{% trans "Réserver une visite guidée" %}</h1>
  <form method="post" action="{% url 'tourisme:reserver' %}">
    {% csrf_token %}
    <input type="text" name="nom" placeholder="{% trans 'Nom du visiteur' %}" required>
    <select name="site">
      {% for site in sites %}
        <option value="{{ site.id }}">{{ site.nom }}</option>
      {% endfor %}
    </select>
    <button type="submit">{% trans "Réserver" %}</button>
  </form>
{% endblock %}
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Gestion touristique complète
- **English**: Full tourism management
- **العربية**: إدارة سياحية متكاملة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⴷⴷⴰⵔⴰⵏ ⵏ ⵜⵓⵔⵉⵙⵎ

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

- [Politique tourisme](./policy.md)
- [Guide API tourisme](../../../../docs/api_tourisme.md)
- [Tests](../../../../tests/tourisme/)

---

## 🏁 Démarrage rapide

1. Copier les templates dans votre projet Django :
   ```bash
   cp -r ./templates/tourisme/ <votre_app>/templates/tourisme/
   ```
2. Ajouter `tourisme` à `INSTALLED_APPS` dans `settings.py`
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
   python manage.py test tourisme
   ```

---

## 🤝 Contribution

- Contributions, issues et suggestions bienvenues sur [GitHub](https://github.com/DihyaOrg/Dihya)
- Respect du [Code de Conduite](../../../../CODE_OF_CONDUCT.md)

---

## 🏆 Licence

Projet open source sous licence AGPLv3 – Respect de la souveraineté numérique.

---

> Ce module tourisme est prêt à l’emploi, sécurisé, multilingue, accessible et souverain.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
