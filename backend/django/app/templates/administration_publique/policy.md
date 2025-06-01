# 📜 Dihya – Politique d’Utilisation & Sécurité des Templates Administration Publique

---

## Table des matières

- [Objectif](#objectif)
- [Sécurité & Souveraineté](#sécurité--souveraineté)
- [Règles d’intégration](#règles-dintégration)
- [Bonnes pratiques](#bonnes-pratiques)
- [Conformité RGPD/NIS2](#conformité-rgpdnis2)
- [Multilingue](#multilingue)
- [Contact & signalement](#contact--signalement)

---

## 🎯 Objectif

Garantir la sécurité, la souveraineté, la conformité et la qualité des templates métiers utilisés pour l’administration publique (démarches, formulaires, documents, workflows, IA, plugins) dans la plateforme Dihya.

---

## 🔒 Sécurité & Souveraineté

- **Open source only** : seuls les templates libres de droits, open source ou créés en interne sont acceptés.
- **Aucun code exécutable** dans les templates (pas de scripts embarqués, pas de macros, pas de code binaire non audité).
- **Auditabilité** : chaque template doit être traçable, versionné, documenté, et vérifiable.
- **Chiffrement** : les documents sensibles sont chiffrés au repos et en transit.
- **Anonymisation** : aucune donnée personnelle dans les templates ou métadonnées.
- **Fallback IA open source** pour la vérification automatique des templates (virus, intégrité, conformité).

---

## 📝 Règles d’intégration

- **Formats acceptés** : .json, .yaml, .yml, .py, .md, .pdf (formulaires, modèles, scripts de génération uniquement)
- **Documentation obligatoire** pour chaque template : origine, licence, usage, auteur, date, version, hash SHA256
- **Vérification automatique** à chaque ajout/modification (CI/CD, GitHub Actions)
- **Tests d’intégrité** : chaque template doit passer les scripts de validation fournis (`validate_admin_template.py`)
- **Accessibilité** : fournir une description textuelle pour chaque template (pour l’inclusion et l’accessibilité)

---

## 🛡️ Bonnes pratiques

- **Limiter la taille** des documents pour optimiser la performance (max 10 Mo par fichier)
- **Optimiser** les modèles pour l’usage numérique (accessibilité, champs structurés, signatures électroniques)
- **Séparer** les templates par usage (formulaires, documents, workflows, scripts)
- **Versionner** chaque modification (Git, changelog, hash)
- **Traduire** les métadonnées et descriptions (fr, en, ar, tzm)
- **Respecter la propriété intellectuelle** et les licences open source

---

## 🏛️ Conformité RGPD/NIS2

- **Aucune donnée personnelle** dans les templates, noms de fichiers, ou métadonnées
- **Suppression sur demande** : tout template peut être supprimé sur demande motivée (voir `/SECURITY.md`)
- **Auditabilité** : logs de chaque ajout, modification, suppression de template
- **Export** : possibilité d’exporter la liste des templates et leurs métadonnées (CSV, JSON)

---

## 🌍 Multilingue

- **Français** : Ce document est disponible en français.
- **English** : This policy is available in English.
- **العربية** : هذه السياسة متوفرة باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Tasertit agi tella s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## 📬 Contact & signalement

Pour toute question, suggestion, ou signalement de faille :
- Email : [security@dihya.io](mailto:security@dihya.io)
- Issues GitHub : [https://github.com/dihya-platform/issues](https://github.com/dihya-platform/issues)

---

**Dihya Coding** – Sécurité, souveraineté, accessibilité, conformité, innovation.

---
