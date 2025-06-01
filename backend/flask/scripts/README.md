# Dihya Coding – Scripts & Automatisations Backend

## Présentation

Ce dossier regroupe tous les **scripts Python** et utilitaires d’automatisation pour le backend Flask de Dihya Coding. Ces scripts facilitent la gestion, la génération, la maintenance, la migration, le déploiement, l’import/export de données, la génération de code, la sécurité et l’industrialisation de la plateforme. Ils sont conçus pour répondre aux exigences de robustesse, sécurité, conformité RGPD, auditabilité et extensibilité du projet.

---

## Objectifs & rôle du dossier

- **Automatiser les tâches récurrentes** (maintenance, migration, backup, génération, nettoyage)
- **Faciliter la génération de code multi-stack** (frontend, backend, scripts IA, DevOps, Blockchain)
- **Assurer la conformité RGPD** (suppression/export des données, logs)
- **Garantir la sécurité et la traçabilité des opérations**
- **Permettre l’extension facile via nouveaux scripts métiers**
- **Documenter chaque script (usage, paramètres, sécurité, rollback)**

---

## Structure du dossier

```
/scripts/
├── generate_project.py      # Génération automatique de projets à partir d’un cahier des charges
├── import_templates.py      # Import/export de templates métiers (JSON, YAML, JS)
├── backup_db.py             # Sauvegarde/restauration de la base de données
├── migrate_data.py          # Migration et transformation de données
├── cleanup.py               # Nettoyage des données/logs obsolètes (RGPD)
├── send_test_mail.py        # Envoi d’emails de test (mailing, notifications)
├── security_audit.py        # Audit de sécurité automatisé (vulnérabilités, permissions)
├── export_user_data.py      # Export RGPD des données utilisateur
├── run_scheduler.py         # Lancement manuel du scheduler/tâches planifiées
├── README.md                # (ce fichier)
└── ...                      # Ajouter ici tout nouveau script métier ou d’automatisation
```

---

## Bonnes pratiques

- **Docstring** détaillée pour chaque script (but, usage, paramètres, sécurité)
- **Typage** et validation stricte des entrées
- **Logs horodatés** pour chaque opération (auditabilité)
- **Aucune donnée sensible en clair dans les scripts ou logs**
- **Rollback possible pour toute opération destructive**
- **Tests unitaires pour les scripts critiques**
- **Respect de la conformité RGPD (suppression/export, logs, anonymisation)**
- **Extensibilité : chaque nouveau script doit être documenté et testé**

---

## Exemples de cas d’usage

- Génération automatique d’un projet web complet à partir d’un cahier des charges écrit ou vocal
- Import/export de templates métiers personnalisés (JSON, YAML, JS)
- Sauvegarde quotidienne de la base de données avec logs d’audit
- Nettoyage automatisé des logs et données obsolètes (conformité RGPD)
- Audit de sécurité périodique (permissions, vulnérabilités, secrets)
- Export des données utilisateur sur demande (RGPD)
- Lancement manuel ou planifié de tâches métiers (génération, mailing, synchronisation)

---

## Contribution

- Ajouter tout nouveau script dans ce dossier avec une docstring claire
- Documenter l’usage, les paramètres et les impacts de chaque script
- Ajouter des tests pour les scripts critiques ou sensibles
- Respecter la structure, la sécurité et la conformité RGPD

---

## Licence

Projet sous licence **AGPL** – open source, souveraineté numérique garantie.

---

*Pour toute suggestion ou amélioration, ouvrez une issue ou une PR sur GitHub.*