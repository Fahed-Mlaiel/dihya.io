"""
Vues Compliance (conformité, audit, RGPD, plugins, multitenant, multilingue, accessibilité)
"""
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .schema import ComplianceReportSchema
from .audit import compliance_audit_logger

class ComplianceReportViewSet(viewsets.ViewSet):
    """Endpoint REST/GraphQL pour les rapports de conformité (audit, RGPD, plugins, multitenant, multilingue)"""
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        # Exemple de rapport structuré, multilingue, RGPD-ready
        data = [
            {
                "id": 1,
                "tenant": "default",
                "report_type": "audit",
                "created_at": "2025-05-24T10:00:00Z",
                "lang": request.LANGUAGE_CODE or "fr",
                "details": {"status": "ok", "audit": True}
            }
        ]
        compliance_audit_logger.log(request.user, 'list', 'ComplianceReport', None, details="List reports", language=request.LANGUAGE_CODE)
        return Response(data)
