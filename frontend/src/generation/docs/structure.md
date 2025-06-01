# 🏗️ Structure – Dihya Coding

Ce document décrit la structure recommandée des templates et blueprints générés par Dihya Coding.  
Chaque structure vise : design moderne, sécurité, conformité RGPD, auditabilité, extensibilité, robustesse, SEO et documentation claire.

---

## 🚀 Objectifs de la structure

- **Organisation claire** : Faciliter la navigation, la compréhension et la maintenance des projets générés
- **Extensibilité** : Permettre l’ajout de nouveaux modules, templates ou fonctionnalités sans rupture
- **Sécurité & RGPD** : Structurer les dossiers pour isoler les données sensibles, logs, et garantir la conformité
- **Auditabilité** : Permettre la traçabilité des modifications et l’audit des évolutions structurelles

---

## 📁 Structure type recommandée

```
/generation/
  ├── fields/         # Types de champs, validations, blueprints de formulaires
  ├── i18n/           # Internationalisation, traductions, dialectes
  ├── infra/          # Infrastructure, sauvegardes, restauration, logs
  ├── mobile/         # Génération mobile (Flutter, React Native, etc.)
  ├── preview/        # Prévisualisation, gestion des aperçus, logs
  ├── security/       # Sécurité, rate limiting, CORS, headers, validation
  ├── seo/            # SEO, audits Lighthouse, utils, configuration
  └── templates/
        ├── ai/           # Templates IA (assistants, fallback, quotas)
        ├── blockchain/   # Templates blockchain (contrats, wallets, intégrations)
        ├── branding/     # Templates branding (logos, palettes, guidelines)
        ├── devops/       # Templates DevOps (CI/CD, Docker, monitoring, IaC)
        └── docs/         # Documentation, guides, compatibilité, sécurité, SEO, structure
```

---

## 🛡️ Bonnes pratiques de structuration

- **Séparation des responsabilités** : Un dossier par domaine fonctionnel (sécurité, SEO, mobile, etc.)
- **Nommage explicite** : Utiliser des noms clairs, cohérents et SEO-friendly pour les dossiers et fichiers
- **Documentation intégrée** : Chaque dossier doit contenir un `README.md` et, si besoin, des guides spécifiques
- **Logs & auditabilité** : Dossiers dédiés pour les logs locaux, avec fonctions de purge (RGPD)
- **Extensibilité** : Prévoir des sous-dossiers pour de futurs modules ou intégrations
- **Sécurité** : Isoler les configurations sensibles, valider les accès et anonymiser les logs

---

## 📝 Exemple d’ajout d’un nouveau module

Pour ajouter un module de génération d’API GraphQL :

1. Créer `/generation/graphql/`
2. Ajouter `graphqlGen.js`, `README.md`, et éventuellement des sous-modules (validation, logs…)
3. Documenter la structure et les bonnes pratiques dans `/generation/templates/docs/`

---

## 📚 Documentation associée

- [Compatibilité](./compatibility.md)
- [Sécurité](./security.md)
- [SEO](./seo.md)
- [AI Templates](../ai/README.md)
- [DevOps Templates](../devops/README.md)
- [Blockchain Templates](../blockchain/README.md)
- [Branding Templates](../branding/README.md)
- [Cahier des charges Dihya Coding](../../../../../docs/user_guide/README.md)

---

> **Dihya Coding : structure moderne, claire, évolutive et conforme RGPD pour chaque génération.**