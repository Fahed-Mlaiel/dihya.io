# 🧳 Dihya – Module Voyage

---

## 🇫🇷 Présentation

Ce dossier regroupe les **templates Django** et outils pour la gestion avancée des voyages sur la plateforme Dihya :
- Réservation, itinéraires, gestion des passagers, notifications, accessibilité, audit, etc.
- Multilingue (fr, en, ar, amazigh)
- Sécurité avancée (permissions, chiffrement, audit, conformité RGPD/voyage)
- Extensible, compatible multi-stack (Django, React, Node, Flutter…)
- Prêt CI/CD, testé, souveraineté numérique garantie

---

## 🚀 Fonctionnalités principales

- **Réservation** : gestion multilingue, validation, notifications, audit
- **Itinéraires** : calcul, affichage, accessibilité, export PDF/JSON
- **Passagers** : gestion profils, rôles, sécurité, RGPD
- **Sécurité** : chiffrement AES-256, permissions fines, audit, conformité RGPD/voyage
- **Accessibilité** : interfaces conformes RGAA/WCAG, multilingue
- **Extensible** : plugins, API REST/GraphQL, intégration mobile/web, fallback IA open source

---

## 🛠️ Exemple d’intégration Django

```django
{% extends "base.html" %}
{% load i18n %}
{% block content %}
  <h1>{% trans "Réserver un voyage" %}</h1>
  <form method="post">
    {% csrf_token %}
    <label for="destination">{% trans "Destination" %}</label>
    <input id="destination" name="destination" required>
    <button type="submit">{% trans "Réserver" %}</button>
  </form>
{% endblock %}
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Gestion voyage avancée, sécurité, accessibilité
- **English**: Advanced travel management, security, accessibility
- **العربية**: إدارة سفر متقدمة، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⴷⴷⴰⵔⴰⵏ ⵏ ⵜⵓⵜⵉⵍⵉⵜⴰⵍ

---

## 🔒 Sécurité & Souveraineté

- Chiffrement AES-256, TLS 1.3, audit, alertes
- Authentification forte (SSO, 2FA)
- Hébergement souverain, code open source

---

## 🧩 Extensibilité

- Personnalisation via plugins Django/React/Node
- API REST/GraphQL pour intégration voyage
- Compatible mobile (Flutter, PWA)

---

## 🧪 Tests & Qualité

- Templates et scripts testés (unitaires, intégration, accessibilité)
- Zéro warning, zéro erreur CI/CD
- Compatible GitHub Actions & Codespaces

---

## 📄 Documentation associée

- [Politique voyage](./policy.md)
- [Guide API voyage](../../../../docs/api_voyage.md)
- [Tests](../../../../tests/voyage/)

---

## 🏁 Démarrage rapide

1. Copier les templates dans votre projet Django :
   ```bash
   cp -r ./templates/voyage/ <votre_app>/templates/voyage/
   ```
2. Ajouter `voyage` à `INSTALLED_APPS` dans `settings.py`
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
   python manage.py test voyage
   ```

---

## 🤝 Contribution

- Contributions, issues et suggestions bienvenues sur [GitHub](https://github.com/DihyaOrg/Dihya)
- Respect du [Code de Conduite](../../../../CODE_OF_CONDUCT.md)

---

## 🏆 Licence

Projet open source sous licence AGPLv3 – Respect de la souveraineté numérique.

---

> Ce module voyage est prêt à l’emploi, sécurisé, multilingue, accessible et souverain.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
