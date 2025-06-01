# 📝 Dihya – Notes Techniques & Fonctionnelles (Ultra avancé, multilingue, souveraineté)

---

## Table des matières

- [Introduction](#introduction)
- [Notes techniques](#notes-techniques)
- [Notes fonctionnelles](#notes-fonctionnelles)
- [Retours d’expérience](#retours-dexpérience)
- [Tips & astuces multi-stack](#tips--astuces-multi-stack)
- [Templates & exemples](#templates--exemples)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce document centralise toutes les notes techniques, fonctionnelles, retours d’expérience, astuces et points d’attention du projet **Dihya**.
Il vise à faciliter la transmission du savoir, la montée en compétence, la souveraineté numérique, la conformité RGPD, l’accessibilité, et la compatibilité multi-stack (React, Flask, Node, Django, Flutter…).

---

## Notes techniques

- **Sécurité** : Toujours activer MFA, TLS 1.3, et vérifier les logs après chaque déploiement.
- **Fallback IA** : Prévoir un fallback open source (Ollama, LocalAI) pour toute intégration IA propriétaire.
- **CI/CD** : Utiliser des runners auto-hébergés pour la souveraineté, valider la conformité à chaque pipeline.
- **i18n** : Vérifier la couverture multilingue (fr, en, ar, tzm) à chaque release.
- **Accessibilité** : Tester avec axe-core, NVDA, VoiceOver, et vérifier le contraste.
- **Logs** : Jamais de données personnelles ou secrets dans les logs.

---

## Notes fonctionnelles

- **Consentement RGPD** : Toujours afficher et journaliser le consentement utilisateur.
- **Rollback** : Tester le rollback automatique à chaque release majeure.
- **Documentation** : Toute doc doit être multilingue, versionnée, et validée par le Doc Lead.
- **Traçabilité** : Chaque action critique (prod, sécurité, RGPD) doit être tracée et archivée.
- **Souveraineté** : Privilégier les solutions open source et l’hébergement souverain.

---

## Retours d’expérience

- **Migration cloud souverain** : Prévoir des tests de performance et de conformité RGPD avant bascule.
- **Déploiement multi-stack** : Bien synchroniser les versions des API et des modules i18n.
- **Accessibilité** : Les audits manuels restent indispensables malgré l’automatisation.
- **Fallback IA** : Les modèles open source nécessitent parfois un tuning spécifique pour la prod.

---

## Tips & astuces multi-stack

- **React** : Utiliser react-intl ou i18next pour la gestion multilingue.
- **Flask/Django** : Centraliser la configuration sécurité (CSP, HSTS, CORS).
- **Node** : Préférer winston/pino pour des logs structurés.
- **Flutter** : Tester l’accessibilité sur Android et iOS, valider la traduction dynamique.
- **DevOps** : Toujours versionner les scripts et playbooks, documenter chaque pipeline.

---

## Templates & exemples

### Template de note technique

```
- Date : YYYY-MM-DD
- Auteur :
- Sujet :
- Stack concernée :
- Description :
- Impact sécurité/conformité :
- Actions recommandées :
- Commentaire :
```

### Exemple rempli

```
- Date : 2025-05-20
- Auteur : @devops-lead
- Sujet : Sécurisation des secrets backend
- Stack concernée : Backend/Node
- Description : Passage de secrets en clair à HashiCorp Vault + rotation automatique.
- Impact sécurité/conformité : Critique (RGPD, souveraineté)
- Actions recommandées : Appliquer Vault sur tous les environnements, auditer les accès.
- Commentaire : Gain de sécurité, conformité RGPD assurée.
```

---

## Multilingue

- **Français** : Ce document est disponible en français.
- **English** : This document is available in English.
- **العربية** : هذا المستند متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-notes
- **Email** : notes@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/your-org/dihya/issues)

---

> **Ce document est validé pour la production. Toute modification doit être soumise via PR et validée par le Doc Lead et le RSSI.**

# Notes Dihya

- Notes techniques, produit, sécurité, architecture, métiers
- TODOs, idées, feedback, points à discuter
- Liens vers les guides, docs, backlog

Voir [PRODUCT_BACKLOG.md](PRODUCT_BACKLOG.md), [CONTRIBUTING.md](CONTRIBUTING.md)
