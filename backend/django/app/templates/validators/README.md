# ✅ Dihya – Module Validators

---

## 🇫🇷 Présentation

Ce dossier regroupe les **validateurs avancés** pour tous les modules Dihya :
- Validation de données (emails, mots de passe, formats, accès, RGPD…)
- Multilingue (fr, en, ar, amazigh)
- Sécurité avancée (anti-injection, conformité RGPD, audit)
- Compatible multi-stack (Django, React, Node, Flutter…)
- Prêt CI/CD, testé, zéro warning, souveraineté numérique garantie

---

## 🚀 Fonctionnalités principales

- **Validation** : emails, mots de passe, formats, accès, RGPD, etc.
- **Sécurité** : anti-injection, audit, chiffrement, conformité RGPD
- **Multilingue** : messages d’erreur et validation en français, anglais, arabe, amazigh
- **Accessibilité** : messages accessibles, compatibles RGAA/WCAG
- **Extensible** : surcharge, injection de vos propres validateurs

---

## 🛠️ Exemple d’utilisation Python

```python
from validators.email import validate_email
from validators.password import validate_password

# Validation d'un email
is_valid, msg = validate_email("test@dihya.eu", lang="fr")
print(is_valid, msg)  # True, "Adresse email valide."

# Validation d'un mot de passe
is_valid, msg = validate_password("S3cur3!", lang="ar")
print(is_valid, msg)  # True, "كلمة المرور قوية."
```

---

## 🌐 Multilingue / Multilingual / متعدد اللغات / ⴰⵎⴰⵣⵉⵖ

- **Français** : Validation avancée, sécurité, accessibilité
- **English**: Advanced validation, security, accessibility
- **العربية**: تحقق متقدم، أمان، إتاحة
- **ⵜⴰⵎⴰⵣⵉⵖⵜ**: ⴰⴷⴷⴰⵔⴰⵏ ⵏ ⵜⵓⵜⵉⵍⵉⵜⴰⵍ

---

## 🔒 Sécurité & Souveraineté

- Validation anti-injection, chiffrement, logs sécurisés
- Journalisation, audit, alertes
- Hébergement souverain, code open source

---

## 🧩 Extensibilité

- Ajoutez vos propres validateurs via plugins Python/JS
- API REST/GraphQL pour validation distante
- Compatible mobile (Flutter, PWA)

---

## 🧪 Tests & Qualité

- Couverture maximale (unitaires, intégration, accessibilité)
- Zéro warning, zéro erreur CI/CD
- Compatible GitHub Actions & Codespaces

---

## 📄 Documentation associée

- [Politique validators](./policy.md)
- [Guide API validators](../../../../docs/api_validators.md)
- [Tests](../../../../tests/validators/)

---

## 🏁 Démarrage rapide

1. Copier les validateurs dans votre projet :
   ```bash
   cp -r ./templates/validators/ <votre_app>/templates/validators/
   ```
2. Importer les validateurs dans vos modules Python :
   ```python
   from validators.email import validate_email
   ```
3. Lancer les tests :
   ```bash
   python manage.py test validators
   ```

---

## 🤝 Contribution

- Contributions, issues et suggestions bienvenues sur [GitHub](https://github.com/DihyaOrg/Dihya)
- Respect du [Code de Conduite](../../../../CODE_OF_CONDUCT.md)

---

## 🏆 Licence

Projet open source sous licence AGPLv3 – Respect de la souveraineté numérique.

---

> Ce module validators est prêt à l’emploi, sécurisé, multilingue, accessible et souverain.
> Pour toute question : [contact@dihya.eu](mailto:contact@dihya.eu)
