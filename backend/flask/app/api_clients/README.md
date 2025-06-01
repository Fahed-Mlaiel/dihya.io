# api_clients

Documentation interne Dihya Coding.

## Objectif

Ce dossier contient les wrappers et clients Python pour l’intégration d’APIs externes (ex : SendGrid, Stripe, Mailgun, Notion, etc.).
Il centralise la gestion des appels API, la validation des réponses, la gestion des erreurs et la sécurité des échanges.

## Bonnes pratiques Dihya Coding

- **Séparation claire** : un fichier par service externe (ex : `sendgrid_client.py`, `stripe_client.py`).
- **Sécurité** : ne jamais stocker de credentials/API keys en dur ; utiliser les variables d’environnement ou le vault sécurisé.
- **Validation** : toujours valider les réponses API et gérer les erreurs de façon robuste.
- **Docstring** : chaque client/fonction doit être documenté (but, paramètres, exceptions).
- **Tests** : prévoir des tests unitaires avec mocks pour chaque client.
- **Extensibilité** : prévoir la possibilité d’ajouter facilement de nouveaux services.

## Exemple de structure

```
api_clients/
├── README.md
├── sendgrid_client.py
├── stripe_client.py
└── notion_client.py
```

## Exemple d’utilisation

```python
from api_clients.sendgrid_client import send_email

send_email(to="user@example.com", subject="Bienvenue", body="Merci pour votre inscription.")
```

## Notion
from api_clients.notion_client import create_page

page_id = create_page("dbid", "Exemple Dihya", {"Test": {"rich_text": [{"text": {"content": "valeur"}}]}})
print("Page Notion créée :", page_id)

## Monitoring/Prometheus
from api_clients.monitoring_client import push_metric, send_alert_sentry

push_metric("testjob", {"test": 1})
send_alert_sentry("Alerte test Dihya", "warning")

---

*Ce dossier fait partie de la documentation technique interne Dihya Coding.*
