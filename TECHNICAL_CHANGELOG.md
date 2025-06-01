# 📝 Dihya – Technical Changelog Ultra Avancé (Multi-stack, Multilingue, Souveraineté, Sécurité)

---

## Table des matières

- [Introduction](#introduction)
- [Format du changelog](#format-du-changelog)
- [Changelog technique détaillé](#changelog-technique-détaillé)
- [Templates & exemples](#templates--exemples)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce changelog technique documente toutes les évolutions majeures et mineures du projet **Dihya** : code, sécurité, accessibilité, RGPD, plugins, templates, DevOps, souveraineté numérique, etc.
Il est multilingue (fr, en, ar, tzm), structuré, compatible CI/CD, et prêt pour l’audit RGPD/NIS2.

---

## Format du changelog

Chaque entrée doit inclure :
- Version, date, auteur, stack concernée
- Type de changement (ajout, correction, sécurité, refactor, breaking, doc…)
- Description multilingue (fr, en, ar, tzm)
- Lien PR/commit, preuve de test, impact sécurité/accessibilité/souveraineté

---

## Changelog technique détaillé

### [1.0.0] – 2025-05-20

#### Ajouts

- **[FR]** Génération automatique de SBOM CycloneDX multi-stack, souverain, RGPD-ready
- **[EN]** Automatic generation of CycloneDX SBOM, multi-stack, sovereign, RGPD-ready
- **[AR]** إنشاء تلقائي لـ SBOM CycloneDX متعدد الطبقات، سيادي، متوافق مع RGPD
- **[TZM]** Asnul n SBOM CycloneDX, multi-stack, amatu, RGPD-ready
  - Stack : DevOps, Backend, CI/CD
  - PR : #12
  - Tests : `pytest`, `sbom-validate`
  - Impact : conformité, auditabilité, souveraineté

- **[FR]** Implémentation RBAC/MFA multi-stack, logs d’attribution, audit
- **[EN]** RBAC/MFA implementation, multi-stack, attribution logs, audit
- **[AR]** تنفيذ RBAC/MFA متعدد الطبقات، سجلات الإسناد، تدقيق
- **[TZM]** Asnul RBAC/MFA, multi-stack, logs n ttwassna, audit
  - Stack : Backend, Frontend, Mobile
  - PR : #15
  - Tests : `pytest`, `e2e`, `axe-core`
  - Impact : sécurité, conformité RGPD/NIS2

#### Corrections

- **[FR]** Correction du fallback IA open source (Ollama, Mixtral)
- **[EN]** Fixed open source AI fallback (Ollama, Mixtral)
- **[AR]** تصحيح fallback IA مفتوح المصدر (Ollama, Mixtral)
- **[TZM]** Issef fallback IA open source (Ollama, Mixtral)
  - Stack : Backend, Plugins
  - PR : #18
  - Tests : `pytest`, `integration`
  - Impact : robustesse, souveraineté

#### Sécurité

- **[FR]** Audit Bandit, Snyk, npm audit automatisé en CI
- **[EN]** Automated Bandit, Snyk, npm audit in CI
- **[AR]** تدقيق Bandit و Snyk و npm تلقائي في CI
- **[TZM]** Audit Bandit, Snyk, npm audit s CI
  - Stack : CI/CD, DevOps
  - PR : #20
  - Tests : `ci-audit`
  - Impact : sécurité, conformité

#### Accessibilité

- **[FR]** Audit accessibilité AA/AAA, navigation clavier, i18n complet
- **[EN]** Accessibility audit AA/AAA, keyboard navigation, full i18n
- **[AR]** تدقيق الوصولية AA/AAA، تنقل لوحة المفاتيح، دعم i18n كامل
- **[TZM]** Audit n tazwart n useqdec AA/AAA, tazwart n taddart, i18n
  - Stack : Frontend, Mobile
  - PR : #22
  - Tests : `axe-core`, `pa11y`, `lighthouse`
  - Impact : accessibilité, inclusion

---

## Templates & exemples

### Template d’entrée changelog

```
- Version :
- Date :
- Auteur :
- Stack concernée :
- Type de changement : Ajout / Correction / Sécurité / Refactor / Breaking / Doc
- Description :
    - fr :
    - en :
    - ar :
    - tzm :
- Lien PR/commit :
- Preuve de test :
- Impact sécurité/accessibilité/souveraineté :
```

### Exemple rempli

```
- Version : 1.0.0
- Date : 2025-05-20
- Auteur : @devops-lead
- Stack concernée : Backend, CI/CD
- Type de changement : Ajout
- Description :
    - fr : Génération automatique de SBOM CycloneDX multi-stack, souverain, RGPD-ready
    - en : Automatic generation of CycloneDX SBOM, multi-stack, sovereign, RGPD-ready
    - ar : إنشاء تلقائي لـ SBOM CycloneDX متعدد الطبقات، سيادي، متوافق مع RGPD
    - tzm : Asnul n SBOM CycloneDX, multi-stack, amatu, RGPD-ready
- Lien PR/commit : #12
- Preuve de test : pytest, sbom-validate
- Impact sécurité/accessibilité/souveraineté : conformité, auditabilité, souveraineté
```

---

## Multilingue

- **Français** : Ce changelog est disponible en français.
- **English** : This changelog is available in English.
- **العربية** : سجل التغييرات هذا متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-changelog
- **Email** : changelog@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/votre-org/dihya/issues)

---

> **Ce changelog est validé pour la production. Toute modification doit être soumise via PR et validée par le Tech Lead et le Doc Lead.**

# Changelog technique Dihya

- Historique détaillé des évolutions techniques, refactors, migrations, changements d’architecture, mises à jour de dépendances, correctifs critiques, etc.
- Liens vers les PR, commits, issues, releases.

Voir [CHANGELOG.md](CHANGELOG.md), [ROADMAP.md](ROADMAP.md)
