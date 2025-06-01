# Guide Troubleshooting Base de Données Dihya

## 1. Problèmes courants
- Requêtes lentes : analysez avec `EXPLAIN ANALYZE`
- Verrous : vérifiez `pg_locks`
- Index inutilisés : consultez `pg_stat_user_indexes`

## 2. Sécurité & RGPD
- Journalisez tous les accès et erreurs
- Anonymisez les logs en production

## 3. Rollback
- Préparez des scripts de rollback pour chaque migration
- Testez les rollbacks sur un environnement de staging

## 4. Monitoring
- Utilisez Prometheus, Grafana, alertes personnalisées

## 5. Ressources
- [DB_MIGRATION_GUIDE.md](./DB_MIGRATION_GUIDE.md)
- [DB_PERFORMANCE.md](./DB_PERFORMANCE.md)
