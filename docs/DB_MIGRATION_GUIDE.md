# Guide de Migration de Base de Données Dihya

Ce guide détaille les étapes pour migrer la base de données du projet Dihya Coding en toute sécurité.

## 1. Outils recommandés
- Alembic (Python)
- Flyway (multi-SGBD)
- Scripts SQL versionnés

## 2. Procédure
1. Créez un backup complet ([DB_BACKUP_GUIDE.md](./DB_BACKUP_GUIDE.md))
2. Appliquez les migrations sur un environnement de staging
3. Vérifiez la conformité RGPD (logs, anonymisation)
4. Exécutez les tests d’intégration et d’audit
5. Appliquez en production avec monitoring

## 3. Sécurité & Audit
- Journalisation de chaque migration
- Rollback automatique en cas d’échec
- Accès restreint aux scripts de migration

## 4. Multitenancy
- Migrations isolées par tenant (schéma ou base dédiée)
- Synchronisation des versions

## 5. Exemples
```bash
alembic revision --autogenerate -m "add new field"
alembic upgrade head
```

## 6. Ressources
- [DB_TROUBLESHOOTING.md](./DB_TROUBLESHOOTING.md)
- [DB_ROADMAP.md](./DB_ROADMAP.md)
