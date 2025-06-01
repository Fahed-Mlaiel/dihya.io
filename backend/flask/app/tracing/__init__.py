"""
Initialisation du module de tracing distribué pour Dihya Coding.

Ce package centralise l’intégration d’OpenTelemetry (et autres outils de tracing)
pour permettre l’observabilité, le debug et l’audit des requêtes backend.

Bonnes pratiques :
- Importer ici les helpers d’initialisation du tracing (OpenTelemetry, Jaeger, etc.)
- Ne jamais tracer de données personnelles ou sensibles
- Documenter chaque point d’instrumentation ajouté
- Prévoir l’extensibilité pour d’autres backends de tracing si besoin
"""

from .opentelemetry_setup import init_tracing