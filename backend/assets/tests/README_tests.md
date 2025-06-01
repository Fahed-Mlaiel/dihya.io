# Dihya Backend Assets – Tests automatisés des jeux de données

Ce fichier documente les tests automatisés pour valider la conformité, l’anonymisation, la multilingue et la structure des jeux de données de test :

- **Conformité RGPD** : aucune donnée réelle, uniquement des exemples anonymisés.
- **Multilingue** : présence de champs de langue, diversité des valeurs.
- **Structure** : validation du schéma (JSON, CSV, YAML).
- **Automatisation** : scripts de test à placer dans ce dossier (ex : test_datasets.py, test_datasets.sh).
- **Nouveaux jeux de données** : projects_sample.json, consent_events_sample.yaml, notifications_sample.csv
- **Tests Bash** : test_datasets.sh (structure, RGPD, anonymisation)
- **Contrôles avancés** : détection automatique de données personnelles, diversité multilingue, statuts, etc.
- **Types de jeux de données** : utilisateurs, transactions, audit, projets, consentements, notifications, logs, rôles, policies, métriques, exports, etc.
- **Formats supportés** : JSON, CSV, YAML, XML, XLSX, PDF, TOML, Markdown
- **Cas métiers spécifiques** : consentement, audit, notifications, transactions, rôles, policies, logs, métriques, exports, accessibilité, incidents, etc.

## Exécution
Ajoutez vos scripts/tests ici pour automatiser la validation des datasets.

## Exécution Bash
```bash
cd backend/assets/tests
chmod +x test_datasets.sh
./test_datasets.sh
```
