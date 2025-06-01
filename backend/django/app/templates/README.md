# 🏗️ Dihya – Templates Ultra Avancés

---

## 🇫🇷 Présentation

Ce dossier regroupe tous les **templates ultra avancés** de la plateforme Dihya :
- Validators, Voice, Voyage, VR/AR, et extensions métiers.
- Multilingue (fr, en, ar, amazigh)
- Sécurité avancée, modularité, extensibilité, souveraineté numérique
- Prêt CI/CD, testé, compatible multi-stack (Django, React, Node, Flutter…)

---

## 📚 Structure

- `validators/` : Validation avancée, sécurité, fallback IA, multilingue
- `voice/` : Gestion voix (reconnaissance, synthèse, accessibilité, notifications audio…)
- `voyage/` : Gestion voyage (réservation, itinéraires, passagers, notifications…)
- `vr_ar/` : Réalité virtuelle/augmentée (scènes immersives, assets 3D, interactions…)
- `README.md` : Ce guide
- `policy.md` : Politique de sécurité, souveraineté, accessibilité, RGPD
- `test_*.py` : Couverture de tests maximale, multilingue, sécurité, CI/CD

---

## 🚀 Fonctionnalités clés

- **Multilingue** : français, anglais, arabe, amazigh
- **Sécurité** : permissions, chiffrement, audit, fallback IA open source, conformité RGPD
- **Accessibilité** : RGAA/WCAG, notifications, interfaces inclusives
- **Extensible** : plugins, API REST/GraphQL, intégration mobile/web
- **Souveraineté numérique** : hébergement souverain, code open source, conformité européenne
- **Prêt CI/CD** : zéro warning, zéro erreur, compatible Codespaces & GitHub Actions

---

## 🛠️ Exemple d’intégration Django

```django
{% extends "base.html" %}
{% load i18n %}
{% block content %}
  <h1>{% trans "Bienvenue sur Dihya" %}</h1>
  {% include "voice/voice_widget.html" %}
  {% include "voyage/form_reservation.html" %}
{% endblock %}
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Templates avancés, sécurité, accessibilité, souveraineté
- **English**: Advanced templates, security, accessibility, sovereignty
- **العربية**: قوالب متقدمة، أمان، إتاحة، سيادة رقمية
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⴷⴷⴰⵔⴰⵏ ⵏ ⵜⵓⵜⵉⵍⵉⵜⴰⵍ ⴰⴳⴳⴰⵔⴰⵡ

---

## 🧪 Tests & Qualité

- Couverture maximale (unit, intégration, accessibilité)
- Zéro faux positif, zéro warning, zéro erreur CI/CD
- Compatible GitHub Actions & Codespaces

---

## 📄 Documentation associée

- [Politique globale](./policy.md)
- [README Voice](./voice/README.md)
- [README Voyage](./voyage/README.md)
- [README VR/AR](./vr_ar/README.md)
- [Tests](../tests/)

---

## 🏁 Démarrage rapide

1. Copier les templates dans votre projet Django :
   ```bash
   cp -r ./templates/ <votre_app>/templates/
   ```
2. Ajouter les modules à `INSTALLED_APPS` dans `settings.py`
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
   python manage.py test
   ```

---

## 🤝 Contribution

- Contributions, issues et suggestions bienvenues sur [GitHub](https://github.com/DihyaOrg/Dihya)
- Respect du [Code de Conduite](../../../../CODE_OF_CONDUCT.md)

---

## 🏆 Licence

Projet open source sous licence AGPLv3 – Respect de la souveraineté numérique.

---

> Ce dossier templates est prêt à l’emploi, sécurisé, multilingue, accessible et souverain.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
