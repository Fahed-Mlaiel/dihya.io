# 🍽️ Dihya – Module Restauration

---

## 🇫🇷 Présentation

Ce dossier contient les **templates Django** et outils pour la gestion de la restauration (cantine, menus, réservations, allergies, etc.) de Dihya.
Pensé pour :
- La souveraineté numérique (open source, hébergement souverain, fallback IA open source)
- La sécurité alimentaire et la conformité RGPD/HACCP
- L’accessibilité et l’inclusion (multilingue : fr, en, ar, amazigh)
- La compatibilité multi-stack (Django, React, Node, Flutter…)

---

## 🚀 Fonctionnalités principales

- **Gestion des menus et réservations** : menus dynamiques, allergies, régimes, réservation en ligne
- **Multilingue** : interfaces et données en français, anglais, arabe, amazigh
- **Sécurité** : chiffrement, gestion fine des accès, auditabilité, conformité RGPD
- **Accessibilité** : RGAA/WCAG, navigation clavier, ARIA
- **Extensible** : plugins, API REST/GraphQL, intégration mobile/web
- **Fallback IA open source** : suggestion de menus, analyse nutritionnelle

---

## 🛠️ Exemple d’intégration Django

```django
{% extends "base.html" %}
{% load i18n %}
{% block content %}
  <h1>{% trans "Menus du jour" %}</h1>
  <ul>
    <li>{% trans "Entrée" %}: {% trans "Salade fraîcheur" %}</li>
    <li>{% trans "Plat" %}: {% trans "Couscous végétarien" %}</li>
    <li>{% trans "Dessert" %}: {% trans "Fruits de saison" %}</li>
  </ul>
  <form method="post" action="{% url 'restauration:reserver' %}">
    {% csrf_token %}
    <input type="text" name="nom" placeholder="{% trans 'Nom' %}" required>
    <input type="text" name="allergies" placeholder="{% trans 'Allergies (optionnel)' %}">
    <button type="submit">{% trans "Réserver" %}</button>
  </form>
{% endblock %}
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Gestion restauration complète
- **English**: Full catering management
- **العربية**: إدارة مطاعم متكاملة
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

- [Politique restauration](./policy.md)
- [Guide API restauration](../../../../docs/api_restauration.md)
- [Tests](../../../../tests/restauration/)

---

## 🏁 Démarrage rapide

1. Copier les templates dans votre projet Django :
   ```bash
   cp -r ./templates/restauration/ <votre_app>/templates/restauration/
   ```
2. Ajouter `restauration` à `INSTALLED_APPS` dans `settings.py`
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
   python manage.py test restauration
   ```

---

## 🤝 Contribution

- Contributions, issues et suggestions bienvenues sur [GitHub](https://github.com/DihyaOrg/Dihya)
- Respect du [Code de Conduite](../../../../CODE_OF_CONDUCT.md)

---

## 🏆 Licence

Projet open source sous licence AGPLv3 – Respect de la souveraineté numérique.

---

> Ce module restauration est prêt à l’emploi, sécurisé, multilingue, accessible et souverain.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
