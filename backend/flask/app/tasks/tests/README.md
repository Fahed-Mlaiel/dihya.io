# tests/ — Tests unitaires tâches asynchrones (Dihya Coding)

Ce dossier regroupe les tests unitaires pour tous les helpers et workers de tâches asynchrones du backend Flask Dihya Coding.

## Objectif

- Vérifier la robustesse, la sécurité et la conformité RGPD/OWASP des tâches de fond (emails, génération, nettoyage, etc.).
- Garantir la non-régression et la fiabilité des traitements asynchrones.
- Faciliter l’audit, la maintenance et l’évolution des workers.

## Bonnes pratiques

- Un fichier de test par type de tâche (`test_email_tasks.py`, `test_cleanup_tasks.py`, etc.).
- Couvrir tous les cas d’usage, y compris les erreurs, dry-run et cas limites.
- Ne jamais stocker ou logguer de secrets réels ou de données personnelles dans les tests.
- Utiliser des mocks ou des fixtures pour isoler les dépendances externes (fichiers, services email, etc.).
- Documenter chaque test avec une docstring claire.
- Exécuter les tests automatiquement en CI/CD.

## Exemple de structure

- `test_email_tasks.py` : tests pour l’envoi d’e-mails transactionnels.
- `test_cleanup_tasks.py` : tests pour le nettoyage périodique.
- `test_generation_tasks.py` : tests pour la génération de projets ou rapports.

## Exemple d’exécution

```bash
pytest .