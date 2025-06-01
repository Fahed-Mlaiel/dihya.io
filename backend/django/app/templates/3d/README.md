# 🧩 Dihya – 3D Templates & Assets Ultra Avancés (Sécurité, Multilingue, Souveraineté, Extensible)

---

## Table des matières

- [Rôle du dossier `templates/3d`](#rôle-du-dossier-templates3d)
- [Fonctions principales](#fonctions-principales)
- [Structure recommandée](#structure-recommandée)
- [Sécurité & conformité](#sécurité--conformité)
- [Exemple d’intégration d’un asset 3D](#exemple-dintégration-dun-asset-3d)
- [Bonnes pratiques](#bonnes-pratiques)
- [Multilingue](#multilingue)
- [Documentation associée](#documentation-associée)

---

## 🧩 Rôle du dossier `templates/3d`

Ce dossier centralise tous les templates, assets, scripts et plugins 3D utilisés par la plateforme Dihya pour la VR/AR, la visualisation, la simulation, l’IA 3D, etc.

- **Multi-stack** : compatible Django, Node, Unity, Unreal, WebXR, Blender, etc.
- **Souveraineté** : assets open source, traçables, versionnés, audités
- **Sécurité** : aucun code exécutable non contrôlé, audit automatique, conformité RGPD/NIS2
- **Extensible** : ajoutez vos propres modèles, scènes, scripts, plugins, assets IA

---

## 🧠 Fonctions principales

- **Gestion centralisée** des assets 3D (objets, scènes, textures, scripts de génération)
- **Découverte automatique** des templates/plugins (voir `__init__.py`)
- **Interopérabilité** avec moteurs 3D, IA, pipelines CI/CD, outils métiers
- **Documentation et métadonnées** pour chaque asset (origine, licence, usage, hash)
- **Scripts de validation** et d’intégrité pour chaque ajout/modification

---

## 📁 Structure recommandée

```
3d/
├── __init__.py           # Initialisation, auto-discovery, sécurité
├── policy.md             # Politique d’utilisation, sécurité, conformité
├── README.md             # Ce fichier (documentation multilingue)
├── validate_3d_asset.py  # Script de validation d’intégrité et de conformité
├── assets/               # Assets 3D (obj, gltf, glb, fbx, dae, json, textures…)
│   ├── exemple_maison_kabyle.obj
│   ├── exemple_scene_village.gltf
│   └── README.assets.md
├── plugins/              # Plugins/scripts de génération ou traitement 3D
│   └── exemple_plugin_blender.py
└── tests/                # Tests unitaires et d’intégration pour assets/scripts
    └── test_validate_3d_asset.py
```

---

## 🔒 Sécurité & conformité

- **Aucun code exécutable** dans les assets 3D (pas de scripts embarqués, pas de macros)
- **Auditabilité** : chaque asset est versionné, documenté, hashé (SHA256)
- **Chiffrement** des assets sensibles (au repos et en transit)
- **Anonymisation** des métadonnées (pas de données personnelles)
- **Vérification automatique** via `validate_3d_asset.py` (CI/CD, GitHub Actions)
- **Suppression sur demande** et export des métadonnées (conformité RGPD/NIS2)
- **Fallback IA open source** pour la vérification automatique des assets

---

## 🛠️ Exemple d’intégration d’un asset 3D

### Ajout d’un asset

1. Placez le fichier dans `assets/` (ex : `maison_kabyle.obj`)
2. Ajoutez une entrée dans `README.assets.md` :

```markdown
### maison_kabyle.obj
- Origine : Création interne
- Licence : CC-BY-SA 4.0
- Auteur : A. Dihya
- Usage : Scène village amazigh
- Date : 2025-05-21
- Version : 1.0
- SHA256 : `a1b2c3...`
- Description : Modèle 3D d’une maison kabyle traditionnelle pour VR/AR
```

3. Lancez le script de validation :

```bash
python3 validate_3d_asset.py assets/maison_kabyle.obj
```

---

## 📝 Bonnes pratiques

- **Limiter la taille** des assets (max 50 Mo)
- **Optimiser** pour le web et la VR/AR (LOD, textures compressées)
- **Séparer** scènes, objets, textures, scripts
- **Versionner** chaque modification (Git, changelog, hash)
- **Traduire** les métadonnées et descriptions (fr, en, ar, tzm)
- **Respecter la propriété intellectuelle** et les licences open source

---

## 🌍 Multilingue

- **Français** : Ce dossier est documenté en français.
- **English** : This folder is documented in English.
- **العربية** : هذا المجلد موثق باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Afaylu agi yettwarnan s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## 📚 Documentation associée

- [Politique d’utilisation & sécurité](./policy.md)
- [Script de validation](./validate_3d_asset.py)
- [Architecture backend](../../../../docs/architecture.md)
- [Sécurité & RGPD](../../../../SECURITY.md)
- [Changelog technique](../../../../TECHNICAL_CHANGELOG.md)
- [Tests E2E](../../../../E2E_TESTS_GUIDE.md)

---

**Dihya Coding** – 3D souverain, extensible, multilingue, prêt pour la production, la démo et la contribution.

---
