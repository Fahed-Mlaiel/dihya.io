"""
Initialisation du tracing distribué OpenTelemetry pour Dihya Coding.

Ce module configure le tracing pour Flask avec OpenTelemetry, compatible Jaeger, Zipkin, etc.
Permet le suivi bout-en-bout des requêtes pour l’observabilité, le debug et l’audit.

Bonnes pratiques :
- Ne jamais tracer de données personnelles ou sensibles
- Configurer l’exporter via variables d’environnement pour la portabilité
- Ajouter des spans personnalisés sur les endpoints critiques
- Documenter chaque point d’instrumentation
"""

import os

from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

# Exporters possibles : Jaeger, Zipkin, OTLP, Console...
from opentelemetry.exporter.jaeger.thrift import JaegerExporter

def init_tracing(app):
    """
    Initialise OpenTelemetry pour l’application Flask.
    À appeler dans create_app().
    """
    service_name = os.getenv("OTEL_SERVICE_NAME", "dihya-backend")
    jaeger_host = os.getenv("JAEGER_HOST", "localhost")
    jaeger_port = int(os.getenv("JAEGER_PORT", "6831"))

    resource = Resource(attributes={
        "service.name": service_name
    })
    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)

    # Jaeger exporter (par défaut)
    jaeger_exporter = JaegerExporter(
        agent_host_name=jaeger_host,
        agent_port=jaeger_port,
    )
    provider.add_span_processor(BatchSpanProcessor(jaeger_exporter))

    # Console exporter (debug)
    if os.getenv("OTEL_CONSOLE_EXPORTER", "false").lower() == "true":
        provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))

    # Instrumentation Flask
    FlaskInstrumentor().instrument_app(app)

    # Exemple d’ajout de span custom dans une route :
    # from opentelemetry import trace
    # tracer = trace.get_tracer(__name__)
    # with tracer.start_as_current_span("nom_span"):
    #     ... code critique ...

# Exemple d’utilisation dans app/__init__.py :
# from backend.flask.app.tracing.opentelemetry_setup import init_tracing
# init_tracing(app)