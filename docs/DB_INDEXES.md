# Guide des Index de Base de Données Dihya

## 1. Types d’index utilisés
- B-tree (par défaut)
- Hash (pour recherche rapide)
- GIN/GiST (pour JSONB, full-text)

## 2. Bonnes pratiques
- Indexer les colonnes utilisées dans les WHERE, JOIN, ORDER BY
- Éviter la sur-indexation (impact sur les performances d’écriture)
- Utiliser des index partiels pour les tables volumineuses

## 3. Sécurité
- Restreindre l’accès aux commandes CREATE/DROP INDEX
- Journaliser les modifications d’index

## 4. Audit & Monitoring
- Utiliser `pg_stat_user_indexes` pour surveiller l’utilisation
- Alertes sur index inutilisés ou fragmentés

## 5. Exemples
```sql
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_logs_ts ON logs(timestamp DESC);
```

Voir aussi : [DB_PERFORMANCE.md](./DB_PERFORMANCE.md), [DB_TROUBLESHOOTING.md](./DB_TROUBLESHOOTING.md)
