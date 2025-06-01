# 🗣️ Dihya – Module Voice

---

## 🇫🇷 Présentation

Ce dossier contient les **templates Django** et outils pour la gestion de la voix sur la plateforme Dihya :
- Reconnaissance vocale, synthèse, transcription, commandes vocales, notifications audio, accessibilité
- Multilingue (fr, en, ar, amazigh)
- Sécurité avancée (permissions, chiffrement, audit, conformité RGPD/voix)
- Extensible, compatible multi-stack (Django, React, Node, Flutter…)
- Prêt CI/CD, testé, souveraineté numérique garantie

---

## 🚀 Fonctionnalités principales

- **Reconnaissance vocale** : transcription multilingue, détection de commandes, accessibilité
- **Synthèse vocale** : génération audio multilingue, notifications, feedback utilisateur
- **Sécurité** : chiffrement AES-256, permissions fines, audit, conformité RGPD/voix
- **Accessibilité** : commandes vocales, navigation audio, support ARIA, multilingue
- **Extensible** : plugins, API REST/GraphQL, intégration mobile/web, fallback IA open source

---

## 🛠️ Exemple d’intégration Django

```django
{% extends "base.html" %}
{% load i18n %}
{% block content %}
  <h1>{% trans "Synthèse vocale" %}</h1>
  <button onclick="speakText('{% trans 'Bienvenue sur Dihya' %}')">
    {% trans "Lire ce texte" %}
  </button>
  <script>
    function speakText(text) {
      if ('speechSynthesis' in window) {
        const utter = new SpeechSynthesisUtterance(text);
        window.speechSynthesis.speak(utter);
      }
    }
  </script>
{% endblock %}
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Gestion voix avancée, sécurité, accessibilité
- **English**: Advanced voice management, security, accessibility
- **العربية**: إدارة صوت متقدمة، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⴷⴷⴰⵔⴰⵏ ⵏ ⵜⵓⵜⵉⵍⵉⵜⴰⵍ

---

## 🔒 Sécurité & Souveraineté

- Chiffrement AES-256, TLS 1.3, audit, alertes
- Authentification forte (SSO, 2FA)
- Hébergement souverain, code open source

---

## 🧩 Extensibilité

- Personnalisation via plugins Django/React/Node
- API REST/GraphQL pour intégration voix
- Compatible mobile (Flutter, PWA)

---

## 🧪 Tests & Qualité

- Templates et scripts testés (unitaires, intégration, accessibilité)
- Zéro warning, zéro erreur CI/CD
- Compatible GitHub Actions & Codespaces

---

## 📄 Documentation associée

- [Politique voix](./policy.md)
- [Guide API voix](../../../../docs/api_voice.md)
- [Tests](../../../../tests/voice/)

---

## 🏁 Démarrage rapide

1. Copier les templates dans votre projet Django :
   ```bash
   cp -r ./templates/voice/ <votre_app>/templates/voice/
   ```
2. Ajouter `voice` à `INSTALLED_APPS` dans `settings.py`
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
   python manage.py test voice
   ```

---

## 🤝 Contribution

- Contributions, issues et suggestions bienvenues sur [GitHub](https://github.com/DihyaOrg/Dihya)
- Respect du [Code de Conduite](../../../../CODE_OF_CONDUCT.md)

---

## 🏆 Licence

Projet open source sous licence AGPLv3 – Respect de la souveraineté numérique.

---

> Ce module voice est prêt à l’emploi, sécurisé, multilingue, accessible et souverain.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
