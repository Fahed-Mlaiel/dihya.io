# 🌍 Dihya – Module Social

---

## 🇫🇷 Présentation

Ce dossier contient les **templates Django** et outils pour la gestion des interactions sociales (réseaux, communautés, posts, commentaires, notifications, etc.) de Dihya.
Pensé pour :
- La souveraineté numérique (open source, hébergement souverain, fallback IA open source)
- La sécurité avancée et la conformité RGPD/social
- L’accessibilité et l’inclusion (multilingue : fr, en, ar, amazigh)
- La compatibilité multi-stack (Django, React, Node, Flutter…)

---

## 🚀 Fonctionnalités principales

- **Gestion des interactions sociales** : posts, commentaires, notifications, modération, audit
- **Multilingue** : interfaces et données en français, anglais, arabe, amazigh
- **Sécurité** : chiffrement, permissions fines, auditabilité, conformité RGPD/social
- **Accessibilité** : RGAA/WCAG, navigation clavier, ARIA
- **Extensible** : plugins, API REST/GraphQL, intégration mobile/web
- **Fallback IA open source** : modération, suggestion de contenu, analyse sociale

---

## 🛠️ Exemple d’intégration Django

```django
{% extends "base.html" %}
{% load i18n %}
{% block content %}
  <h1>{% trans "Mur social" %}</h1>
  <form method="post" action="{% url 'social:poster' %}">
    {% csrf_token %}
    <textarea name="message" placeholder="{% trans 'Exprimez-vous...' %}" required></textarea>
    <button type="submit">{% trans "Publier" %}</button>
  </form>
  <ul>
    {% for post in posts %}
      <li>
        <strong>{{ post.user }}</strong> : {{ post.message }}
        <span>({{ post.created_at|date:"SHORT_DATETIME_FORMAT" }})</span>
      </li>
    {% endfor %}
  </ul>
{% endblock %}
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Gestion sociale complète
- **English**: Full social management
- **العربية**: إدارة تواصل اجتماعي متكاملة
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

- [Politique social](./policy.md)
- [Guide API social](../../../../docs/api_social.md)
- [Tests](../../../../tests/social/)

---

## 🏁 Démarrage rapide

1. Copier les templates dans votre projet Django :
   ```bash
   cp -r ./templates/social/ <votre_app>/templates/social/
   ```
2. Ajouter `social` à `INSTALLED_APPS` dans `settings.py`
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
   python manage.py test social
   ```

---

## 🤝 Contribution

- Contributions, issues et suggestions bienvenues sur [GitHub](https://github.com/DihyaOrg/Dihya)
- Respect du [Code de Conduite](../../../../CODE_OF_CONDUCT.md)

---

## 🏆 Licence

Projet open source sous licence AGPLv3 – Respect de la souveraineté numérique.

---

> Ce module social est prêt à l’emploi, sécurisé, multilingue, accessible et souverain.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
