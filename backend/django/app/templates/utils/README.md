# 🛠️ Dihya – Module Utils

---

## 🇫🇷 Présentation

Ce dossier regroupe les **utilitaires avancés** pour tous les modules Dihya :
- Fonctions d’aide génériques (formatage, sécurité, i18n, accessibilité, audit, fallback IA open source…)
- Multilingue (fr, en, ar, amazigh)
- Sécurité avancée (sanitization, logging, conformité RGPD)
- Compatible multi-stack (Django, React, Node, Flutter…)
- Prêt CI/CD, testé, zéro warning, souveraineté numérique garantie

---

## 🚀 Fonctionnalités principales

- **Formatage & validation** : chaînes, dates, emails, numéros, etc.
- **Sécurité** : sanitization, chiffrement, audit, logging, conformité RGPD
- **i18n & accessibilité** : helpers multilingues, fallback, adaptation ARIA
- **Fallback IA open source** : suggestion, analyse, modération
- **Extensible** : surcharge, injection de vos propres helpers

---

## 🛠️ Exemple d’utilisation Python

```python
from utils.format import sanitize_input, format_date
from utils.i18n import translate

# Sécurisation d'une entrée utilisateur
safe = sanitize_input("<script>alert('xss')</script>")
print(safe)  # Résultat : alert('xss')

# Formatage de date multilingue
print(format_date("2025-05-21", lang="fr"))  # 21/05/2025

# Traduction multilingue
print(translate("Bienvenue", lang="ar"))  # مرحبا
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Utilitaires avancés, sécurité, accessibilité
- **English**: Advanced utils, security, accessibility
- **العربية**: أدوات متقدمة، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⴷⴷⴰⵔⴰⵏ ⵏ ⵓⵜⵉⵍⵉⵜⴰⵍ

---

## 🔒 Sécurité & Souveraineté

- Sanitization systématique, chiffrement AES-256, logs sécurisés
- Journalisation, audit, alertes
- Hébergement souverain, code open source

---

## 🧩 Extensibilité

- Ajoutez vos propres helpers via plugins Python/JS
- API REST/GraphQL pour utils critiques
- Compatible mobile (Flutter, PWA)

---

## 🧪 Tests & Qualité

- Couverture maximale (unitaires, intégration, accessibilité)
- Zéro warning, zéro erreur CI/CD
- Compatible GitHub Actions & Codespaces

---

## 📄 Documentation associée

- [Politique utils](./policy.md)
- [Guide API utils](../../../../docs/api_utils.md)
- [Tests](../../../../tests/utils/)

---

## 🏁 Démarrage rapide

1. Copier les utilitaires dans votre projet :
   ```bash
   cp -r ./templates/utils/ <votre_app>/templates/utils/
   ```
2. Importer les helpers dans vos modules Python :
   ```python
   from utils.format import sanitize_input
   ```
3. Lancer les tests :
   ```bash
   python manage.py test utils
   ```

---

## 🤝 Contribution

- Contributions, issues et suggestions bienvenues sur [GitHub](https://github.com/DihyaOrg/Dihya)
- Respect du [Code de Conduite](../../../../CODE_OF_CONDUCT.md)

---

## 🏆 Licence

Projet open source sous licence AGPLv3 – Respect de la souveraineté numérique.

---

> Ce module utils est prêt à l’emploi, sécurisé, multilingue, accessible et souverain.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
