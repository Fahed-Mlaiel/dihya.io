# 📜 Dihya – Politique d’Utilisation & Sécurité des Templates 3D

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

Garantir la sécurité, la souveraineté, la conformité et la qualité des assets et templates 3D utilisés dans la plateforme Dihya (VR/AR, visualisation, simulation, IA).

---

## 🔒 Sécurité & Souveraineté

- **Open source only** : seuls les assets 3D libres de droits, open source ou créés en interne sont acceptés.
- **Aucun code exécutable** dans les assets 3D (pas de scripts embarqués, pas de macros, pas de code binaire).
- **Auditabilité** : chaque asset doit être traçable, versionné, documenté, et vérifiable.
- **Chiffrement** : les assets sensibles sont chiffrés au repos et en transit.
- **Anonymisation** : aucune donnée personnelle dans les assets ou métadonnées.
- **Fallback IA open source** pour la vérification automatique des assets (virus, intégrité, conformité).

---

## 📝 Règles d’intégration

- **Format accepté** : .obj, .gltf, .glb, .fbx, .dae, .json (scènes), .py (scripts de génération uniquement)
- **Documentation obligatoire** pour chaque asset : origine, licence, usage, auteur, date, version, hash SHA256
- **Vérification automatique** à chaque ajout/modification (CI/CD, GitHub Actions)
- **Tests d’intégrité** : chaque asset doit passer les scripts de validation fournis (`validate_3d_asset.py`)
- **Accessibilité** : fournir une description textuelle pour chaque asset (pour l’inclusion et l’accessibilité)

---

## 🛡️ Bonnes pratiques

- **Limiter la taille** des assets pour optimiser la performance (max 50 Mo par fichier)
- **Optimiser** les modèles pour le web et la VR/AR (LOD, textures compressées, pas de polygones inutiles)
- **Séparer** les assets par usage (scènes, objets, textures, scripts)
- **Versionner** chaque modification (Git, changelog, hash)
- **Traduire** les métadonnées et descriptions (fr, en, ar, tzm)
- **Respecter la propriété intellectuelle** et les licences open source

---

## 🏛️ Conformité RGPD/NIS2

- **Aucune donnée personnelle** dans les assets, noms de fichiers, ou métadonnées
- **Suppression sur demande** : tout asset peut être supprimé sur demande motivée (voir `/SECURITY.md`)
- **Auditabilité** : logs de chaque ajout, modification, suppression d’asset
- **Export** : possibilité d’exporter la liste des assets et leurs métadonnées (CSV, JSON)

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
