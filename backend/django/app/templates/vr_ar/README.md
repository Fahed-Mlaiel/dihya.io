# 🕶️ Dihya – Module VR/AR

---

## 🇫🇷 Présentation

Ce dossier contient les **templates Django** et outils pour la gestion avancée de la réalité virtuelle (VR) et augmentée (AR) sur la plateforme Dihya :
- Scènes immersives, assets 3D, interactions vocales et gestuelles, notifications, accessibilité, audit, fallback IA open source
- Multilingue (fr, en, ar, amazigh)
- Sécurité avancée (permissions, chiffrement, audit, conformité RGPD/VR-AR)
- Extensible, compatible multi-stack (Django, React, Node, Flutter, Unity…)
- Prêt CI/CD, testé, souveraineté numérique garantie

---

## 🚀 Fonctionnalités principales

- **Scènes immersives** : création, gestion, partage, export
- **Assets 3D** : import/export, validation, gestion des droits, accessibilité
- **Interactions** : vocales, gestuelles, multi-utilisateur, notifications immersives
- **Sécurité** : chiffrement AES-256, permissions fines, audit, conformité RGPD/VR-AR
- **Accessibilité** : interfaces immersives conformes RGAA/WCAG, multilingue
- **Extensible** : plugins, API REST/GraphQL, intégration mobile/web/Unity, fallback IA open source

---

## 🛠️ Exemple d’intégration Django

```django
{% extends "base.html" %}
{% load i18n %}
{% block content %}
  <h1>{% trans "Scène immersive VR/AR" %}</h1>
  <div id="vr-ar-canvas"></div>
  <script src="https://cdn.jsdelivr.net/npm/aframe/dist/aframe.min.js"></script>
  <a-scene embedded arjs>
    <a-box position="0 1 -3" rotation="0 45 0" color="#4CC3D9"></a-box>
    <a-sky color="#ECECEC"></a-sky>
  </a-scene>
{% endblock %}
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Gestion VR/AR avancée, sécurité, accessibilité
- **English**: Advanced VR/AR management, security, accessibility
- **العربية**: إدارة واقع افتراضي/معزز متقدمة، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⴷⴷⴰⵔⴰⵏ ⵏ VR/AR ⴷ ⵜⵓⵜⵉⵍⵉⵜⴰⵍ

---

## 🔒 Sécurité & Souveraineté

- Chiffrement AES-256, TLS 1.3, audit, alertes
- Authentification forte (SSO, 2FA)
- Hébergement souverain, code open source

---

## 🧩 Extensibilité

- Personnalisation via plugins Django/React/Node/Unity
- API REST/GraphQL pour intégration VR/AR
- Compatible mobile (Flutter, PWA, Unity)

---

## 🧪 Tests & Qualité

- Templates et scripts testés (unitaires, intégration, accessibilité)
- Zéro warning, zéro erreur CI/CD
- Compatible GitHub Actions & Codespaces

---

## 📄 Documentation associée

- [Politique VR/AR](./policy.md)
- [Guide API VR/AR](../../../../docs/api_vr_ar.md)
- [Tests](../../../../tests/vr_ar/)

---

## 🏁 Démarrage rapide

1. Copier les templates dans votre projet Django :
   ```bash
   cp -r ./templates/vr_ar/ <votre_app>/templates/vr_ar/
   ```
2. Ajouter `vr_ar` à `INSTALLED_APPS` dans `settings.py`
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
   python manage.py test vr_ar
   ```

---

## 🤝 Contribution

- Contributions, issues et suggestions bienvenues sur [GitHub](https://github.com/DihyaOrg/Dihya)
- Respect du [Code de Conduite](../../../../CODE_OF_CONDUCT.md)

---

## 🏆 Licence

Projet open source sous licence AGPLv3 – Respect de la souveraineté numérique.

---

> Ce module VR/AR est prêt à l’emploi, sécurisé, multilingue, accessible et souverain.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
