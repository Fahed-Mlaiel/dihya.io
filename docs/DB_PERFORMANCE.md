# Guide Performance Base de Données Dihya

## 1. Indexation
- Utilisez des index adaptés (voir [DB_INDEXES.md](./DB_INDEXES.md))
- Analysez les requêtes lentes avec `EXPLAIN ANALYZE`

## 2. Optimisation des requêtes
- Préférez les requêtes paramétrées
- Limitez les jointures complexes
- Utilisez le cache applicatif (Redis, Memcached)

## 3. Sécurité & RGPD
- Chiffrez les données sensibles
- Limitez les accès en lecture/écriture
- Anonymisez les logs de requêtes

## 4. Monitoring
- Utilisez `pg_stat_statements`, Prometheus, Grafana
- Alertes sur latence, verrous, saturation

## 5. Exemples
```sql
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'test@dihya.org';
```

## 6. Ressources
- [DB_TROUBLESHOOTING.md](./DB_TROUBLESHOOTING.md)
- [DB_MONITORING.md](./DB_MONITORING.md)
