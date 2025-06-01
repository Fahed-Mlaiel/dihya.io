# 📦 Dihya – Fixtures pour le module Ressources Humaines

## Objectif
Fournir des jeux de données anonymisés, multilingues, RGPD-compliant pour les tests, la démo, la CI/CD et la documentation.

## Exemples de fixtures
```json
[
  {"model": "ressources_humaines.employe", "pk": 1, "fields": {"nom": "Doe", "prenom": "John", "email": "john.doe@example.com", "poste": "Développeur", "date_embauche": "2025-01-01", "manager": 1}},
  {"model": "ressources_humaines.poste", "pk": 1, "fields": {"titre": "Développeur", "ouvert": true}},
  {"model": "ressources_humaines.candidature", "pk": 1, "fields": {"employe": 1, "poste": 1, "statut": "en_attente"}}
]
```

## Utilisation
```bash
python manage.py loaddata backend/django/app/routes/ressources_humaines/fixtures.json
```

## Bonnes pratiques
- Données anonymisées, multilingues
- Respect RGPD, accessibilité
- Documentation dans `/README_tests.md`
