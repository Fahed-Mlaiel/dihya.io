# README – Dihya Backend Assets

Ce dossier contient les assets spécifiques au backend Dihya : scripts, configs, templates, données de test, etc.

- Structure claire, versionnée, sécurisée
- Exemples d’utilisation, conventions, scripts d’import/export
- Contribution, extension, personnalisation

Voir [../README.md](../README.md)

---

## 📦 Rôle du dossier `backend/assets`

Ce dossier centralise toutes les ressources statiques, médias et fichiers nécessaires au fonctionnement du backend de la plateforme Dihya Coding.

---

## 🧩 Contenu typique

- **Logos et branding backend** (pour génération automatique de docs, emails, etc.)
- **Fichiers de configuration statiques** (ex : exemples de secrets, configs par défaut)
- **Templates statiques** (emails transactionnels, notifications, rapports PDF)
- **Assets pour génération de code** (snippets, exemples, blueprints backend)
- **Images ou icônes utilisées côté backend** (ex : pour génération de rapports ou d’exports)
- **Exports de logs ou d’audit** (fichiers horodatés, anonymisés pour conformité RGPD)

---

## 📁 Structure recommandée
assets/ ├── branding/ # Logos backend, signatures email, favicon API ├── templates/ # Templates statiques (emails, rapports, notifications) ├── config/ # Exemples de fichiers de configuration ├── snippets/ # Exemples de code backend, blueprints, helpers ├── logs/ # Exports de logs/audit (RGPD, sécurité) └── README.md # Ce fichier
---

## 🔒 Sécurité & conformité

- **Aucune donnée personnelle** ne doit être stockée ici.
- **Logs et exports** : toujours anonymiser et horodater pour conformité RGPD.
- **Accès restreint** : seuls les assets nécessaires au backend doivent être présents.
- **Auditabilité** : chaque ajout/modification d’asset doit être documenté dans les PR.

---

## 🛠️ Bonnes pratiques

- **Nommez clairement** chaque fichier (ex : `template-reset-password.html`, `logo-backend.svg`).
- **Optimisez** les fichiers pour usage serveur (taille, format).
- **Versionnez** les assets critiques pour la traçabilité.
- **Séparez** bien les assets frontend et backend pour éviter les confusions.

---

## 📝 Contribution

- Toute contribution d’asset backend doit respecter la charte de sécurité et de conformité Dihya Coding.
- Pour proposer un nouveau template ou asset, ouvrez une PR avec une description claire.
- Voir [CONTRIBUTING.md](../../CONTRIBUTING.md) pour les guidelines.

---

**Dihya Coding** – Backend robuste, conforme, extensible.
