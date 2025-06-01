# Guide de Restauration Base de Données Dihya

## 1. Procédure de restauration
- Identifiez le backup à restaurer (voir [DB_BACKUP_GUIDE.md](./DB_BACKUP_GUIDE.md))
- Vérifiez l’intégrité du fichier
- Restaurez sur un environnement isolé avant production

```bash
# Restauration PostgreSQL
zcat backup_2025-05-24.sql.gz | psql -U dihya_user -h localhost dihya_db
```

## 2. Sécurité & RGPD
- Accès restreint à la restauration
- Journalisation de chaque opération
- Anonymisation des données restaurées si besoin

## 3. Audit & Rollback
- Vérifiez la cohérence post-restauration
- Préparez un plan de rollback

## 4. Ressources
- [DB_TROUBLESHOOTING.md](./DB_TROUBLESHOOTING.md)
- [DB_ROADMAP.md](./DB_ROADMAP.md)
