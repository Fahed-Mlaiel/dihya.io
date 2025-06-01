# 🧪 Dihya – Tests du module Restauration

## Objectif
Garantir la robustesse, la sécurité, la conformité RGPD, la souveraineté et la qualité du module restauration via des tests unitaires, d’intégration et E2E.

## Types de tests
- **Unitaires** : modèles, serializers, permissions, vues
- **Intégration** : endpoints REST, RBAC, audit, logs
- **E2E** : scénarios utilisateurs, CI/CD, accessibilité, multilingue

## Exécution
```bash
python manage.py test backend/django/app/routes/restauration/
```

## Bonnes pratiques
- Couverture > 95% sur les modules critiques
- Tests multilingues (fr, en, ar, tzm)
- Vérification RGPD, accessibilité, sécurité
- Utilisation de fixtures anonymisées

## Documentation
Voir `/E2E_TESTS_GUIDE.md` et `/docs/` pour les guides avancés.
