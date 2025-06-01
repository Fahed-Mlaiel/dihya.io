# Guide Seed Base de Données Dihya

## 1. Objectif
Initialiser la base avec des données de référence, multilingues, sécurisées, et auditables.

## 2. Procédure
- Utilisez des scripts versionnés (`seed_*.sql` ou Python)
- Séparez les seeds par tenant (multitenancy)
- Anonymisez les données de test
- Journalisez chaque opération de seed

## 3. Sécurité & RGPD
- Accès restreint aux scripts de seed
- Logs d’exécution et rollback possible

## 4. Exemples
```sql
INSERT INTO roles (name) VALUES ('admin'), ('user'), ('guest');
INSERT INTO languages (code, name) VALUES ('fr', 'Français'), ('en', 'English'), ('ar', 'العربية');
```

## 5. Ressources
- [DB_MIGRATION_GUIDE.md](./DB_MIGRATION_GUIDE.md)
- [DB_TROUBLESHOOTING.md](./DB_TROUBLESHOOTING.md)
