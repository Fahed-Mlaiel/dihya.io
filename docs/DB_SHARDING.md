# Guide Sharding Base de Données Dihya

## 1. Objectif
Scalabilité horizontale, isolation des tenants, performance.

## 2. Stratégies
- Sharding par tenant (schéma ou base dédiée)
- Sharding par plage de données (hash, range)

## 3. Sécurité & RGPD
- Chiffrement inter-shards
- Journalisation des accès inter-shards
- Synchronisation RGPD (droit à l’oubli, export)

## 4. Monitoring
- Suivi de la latence et de la cohérence
- Alertes sur désynchronisation

## 5. Exemples
- Utilisation de Citus (PostgreSQL)
- Partitionnement natif

## 6. Ressources
- [DB_PERFORMANCE.md](./DB_PERFORMANCE.md)
- [DB_REPLICATION.md](./DB_REPLICATION.md)
