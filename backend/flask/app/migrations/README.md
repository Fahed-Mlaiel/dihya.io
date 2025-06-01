# Dihya Coding – Migrations & Gestion de la Base de Données

## Présentation

Ce dossier contient les scripts et la documentation relatifs aux **migrations de base de données** pour le backend Flask de Dihya Coding. Les migrations assurent l’évolution structurée du schéma de la base de données, la traçabilité des changements, la conformité RGPD et la robustesse des données pour tous les modules métiers (utilisateurs, projets, logs, plugins, etc.).

---

## Objectifs & Bonnes pratiques

- **Automatiser la création, modification et suppression des tables**
- **Garantir la cohérence et la traçabilité des évolutions du schéma**
- **Permettre le rollback et la gestion des versions**
- **Assurer la conformité RGPD (suppression/export des données)**
- **Sécuriser les migrations (validation, logs, auditabilité)**
- **Supporter l’extensibilité (ajout de nouveaux modules métiers, plugins, templates)**
- **Documenter chaque migration (but, impact, rollback)**

---

## Structure du dossier

```
/migrations/
├── versions/           # Scripts de migration générés (par ex. Alembic)
├── README.md           # (ce fichier)
├── env.py              # Configuration des migrations
├── script.py.mako      # Template de script de migration
└── alembic.ini         # Fichier de configuration Alembic
```

---

## Fonctionnement

- Utilisation d’**Alembic** (ou équivalent) pour la gestion des migrations SQLAlchemy.
- Chaque modification du modèle (ajout de champ, table, index, suppression, etc.) doit être suivie d’une migration.
- Les migrations sont versionnées, traçables et auditées.
- Les scripts de migration doivent inclure :
  - **Docstring** claire (but, contexte, impact)
  - **Rollback** possible (downgrade)
  - **Logs** d’exécution pour auditabilité

---

## Sécurité & conformité RGPD

- **Suppression/export des données** sur demande utilisateur (scripts dédiés)
- **Logs horodatés** pour chaque migration appliquée
- **Validation stricte** avant application (pré-migration checks)
- **Rollback** sécurisé en cas d’erreur
- **Aucune donnée sensible dans les scripts ou logs**

---

## Commandes principales

Initialiser les migrations :

```bash
alembic init migrations
```

Générer une nouvelle migration après modification des modèles :

```bash
alembic revision --autogenerate -m "Description de la migration"
```

Appliquer les migrations :

```bash
alembic upgrade head
```

Revenir à une version précédente :

```bash
alembic downgrade <version>
```

---

## Contribution

- Documenter chaque migration (docstring, contexte, rollback)
- Vérifier la conformité RGPD et la sécurité à chaque modification
- Ajouter des tests pour les migrations critiques
- Respecter la structure et les conventions du projet

---

## Licence

Projet sous licence **AGPL** – open source, souveraineté numérique garantie.

---

*Pour toute question ou suggestion, consultez la documentation ou ouvrez une issue sur GitHub.*