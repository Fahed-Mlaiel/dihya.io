# Tracing distribué (OpenTelemetry, Jaeger...)

Ce dossier contient les modules et scripts pour l’implémentation du tracing distribué dans le backend Dihya Coding.

## Objectif

Permettre le suivi bout-en-bout des requêtes à travers les différents services et composants de la plateforme, afin de faciliter le debug, l’optimisation des performances et l’audit de sécurité.

## Bonnes pratiques Dihya Coding

- **Interopérabilité** : utiliser des standards ouverts (OpenTelemetry, Jaeger…) pour garantir la compatibilité avec les outils du marché.
- **Respect de la vie privée** : ne jamais tracer ou stocker de données personnelles ou sensibles dans les traces.
- **Extensibilité** : prévoir l’ajout facile de nouveaux points de trace (spans) dans le code métier.
- **Performance** : minimiser l’impact du tracing sur la latence et la charge serveur.
- **Sécurité** : sécuriser l’accès aux dashboards et exporter les traces de façon contrôlée.
- **Documentation** : chaque module ou script doit être documenté (usage, configuration, intégration).

## Exemples de fonctionnalités à implémenter

- Initialisation d’OpenTelemetry pour Flask
- Export des traces vers Jaeger, Zipkin ou autre backend compatible
- Ajout de spans personnalisés sur les endpoints critiques
- Scripts de configuration et de test du tracing

## Utilisation

Dans votre app Flask principale :

```python
from app.tracing.opentelemetry_setup import init_tracing
init_tracing(app)
```

---

*Ce dossier fait partie de la documentation technique interne Dihya Coding.*