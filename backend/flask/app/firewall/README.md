# Web Application Firewall custom

Ce dossier contient les modules et scripts du Web Application Firewall (WAF) personnalisé pour le backend Dihya Coding.

## Objectif

Protéger l’API et l’application contre les attaques courantes (injections, XSS, brute force, scans automatisés, etc.) grâce à des règles dynamiques et extensibles.

## Bonnes pratiques Dihya Coding

- **Détection proactive** : filtrer et bloquer les requêtes suspectes avant qu’elles n’atteignent la logique métier.
- **Extensibilité** : permettre l’ajout facile de nouvelles règles ou signatures d’attaque.
- **Logging** : journaliser chaque tentative bloquée pour audit et amélioration continue.
- **Performance** : ne pas ralentir l’application, privilégier des contrôles rapides et efficaces.
- **Sécurité** : ne jamais exposer de détails techniques sur les règles ou les raisons de blocage dans les réponses API.
- **Maintenance** : documenter chaque règle et prévoir des scripts de mise à jour automatique.

## Exemples de fonctionnalités à implémenter

- Filtrage d’IP (blacklist/whitelist dynamique)
- Détection d’injections SQL/XSS dans les paramètres
- Limitation de requêtes suspectes (user-agents, patterns connus)
- Blocage de scans automatisés (ex : scanners de vulnérabilité)
- Intégration avec les logs de sécurité et alerting

## Utilisation

À intégrer dans l’initialisation de l’application Flask :

```python
from app.firewall import waf_middleware
waf_middleware(app)
```

---

*Ce dossier fait partie de la documentation technique interne Dihya Coding.*