"""
Schéma OpenAPI/GraphQL pour la conformité (compliance)
- RGPD, audit, plugins, multitenant, multilingue, accessibilité
"""
from drf_spectacular.utils import extend_schema
from rest_framework import serializers

class ComplianceReportSchema(serializers.Serializer):
    id = serializers.IntegerField()
    tenant = serializers.CharField()
    report_type = serializers.CharField()
    created_at = serializers.DateTimeField()
    lang = serializers.CharField()
    details = serializers.JSONField()
