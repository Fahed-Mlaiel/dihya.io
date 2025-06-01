# Guide de Sauvegarde des Bases de Données Dihya

Ce guide explique comment sauvegarder, sécuriser et restaurer les bases de données du projet Dihya Coding.

## 1. Stratégie de sauvegarde
- Sauvegarde incrémentale quotidienne, complète hebdomadaire
- Chiffrement AES-256, stockage multi-sites (cloud + local)
- Automatisation via cron + scripts Docker

## 2. Procédure de sauvegarde
```bash
# Sauvegarde PostgreSQL
pg_dump -U dihya_user -h localhost dihya_db | gzip > backup_$(date +%F).sql.gz
```
- Vérifiez l’intégrité avec `pg_restore --list`
- Stockez les logs dans `/var/log/dihya/db_backup.log`

## 3. Sécurité & RGPD
- Accès restreint (ACL, VPN, MFA)
- Journalisation des accès et restaurations
- Anonymisation des données sensibles avant export

## 4. Restauration
Voir [DB_RESTORE_GUIDE.md](./DB_RESTORE_GUIDE.md)

## 5. Automatisation
- Utilisez GitHub Actions pour sauvegardes cloud
- Scripts de monitoring et alertes (voir [DB_MONITORING.md](./DB_MONITORING.md))

## 6. Ressources
- [DB_SCHEMA.png](./DB_SCHEMA.png)
- [DB_TROUBLESHOOTING.md](./DB_TROUBLESHOOTING.md)
