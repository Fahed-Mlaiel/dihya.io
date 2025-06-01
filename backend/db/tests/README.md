# Tests unitaires et d'intégration pour le module DB

Ce dossier contient les tests unitaires et d'intégration pour le module `backend/db` de Dihya.

## Objectifs
- Vérifier la conformité du schéma SQL (PostgreSQL, MySQL, SQLite)
- Tester la sécurité (accès, anonymisation, RGPD)
- Tester la performance (index, vues, triggers)
- Tester la migration et la restauration
- Tester la compatibilité multilingue (fr, en, ar, tzm)

## Structure recommandée
- test_schema.py : tests de validation du schéma
- test_security.py : tests RGPD, anonymisation, accès
- test_performance.py : benchmarks, index, vues
- test_migration.py : tests de migration, rollback
- test_multilingue.py : tests d'internationalisation des données

## Bonnes pratiques
- Utiliser des fixtures anonymisées
- Couvrir tous les cas critiques (fail, edge, rollback)
- Générer des rapports de couverture

## Lancement des tests

```bash
pytest
```

## Multilingue
- Les messages d'erreur et de succès doivent être testés dans toutes les langues supportées.

## 🚦 Intégration CI/CD & Couverture
- Les tests sont exécutés automatiquement à chaque build CI (voir `.github/workflows/ci.yml`)
- Un rapport de couverture automatisé est généré et archivé (`coverage_db.xml`, `htmlcov/`)
- Les tests e2e (performance, triggers, vues) sont inclus pour garantir la robustesse
- Exemples d’utilisation avancés et scripts de reporting sont fournis dans `EXAMPLES_ADVANCED_DB_TESTS.md`

## 🏅 Badge de couverture automatisé
- Un badge SVG de couverture (`coverage_db_badge.svg`) est généré et publié à chaque build CI/CD
- Voir `README_BADGE.md` pour l’intégration dans la documentation ou le dashboard conformité

---

> Voir la documentation principale dans `../README.md` et le schéma SQL dans `../database_schema.sql`.
