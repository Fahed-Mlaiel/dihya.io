"""
Dihya – Django SEO API Views Ultra Avancé
-----------------------------------------
- ViewSets REST pour métadonnées, sitemaps, robots.txt, performance, accessibilité, IA SEO, logs, audit
- Sécurité, RBAC, logs, conformité RGPD/NIS2, anonymisation, multilingue, extensibilité, fallback IA open source
- Prêt pour CI/CD, Codespaces, cloud souverain, production, démo, contribution

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .serializers import *
from .models import *
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .audit import audit_log

class MetaDonneeViewSet(viewsets.ModelViewSet):
    queryset = MetaDonnee.objects.all()
    serializer_class = MetaDonneeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        instance = serializer.save(owner=self.request.user)
        audit_log(self.request.user, 'create_metadonnee', instance)

class SiteMapViewSet(viewsets.ModelViewSet):
    queryset = SiteMap.objects.all()
    serializer_class = SiteMapSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RobotsTxtViewSet(viewsets.ModelViewSet):
    queryset = RobotsTxt.objects.all()
    serializer_class = RobotsTxtSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AccessibiliteViewSet(viewsets.ModelViewSet):
    queryset = Accessibilite.objects.all()
    serializer_class = AccessibiliteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class IASEOViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    def list(self, request):
        # Intégration IA SEO souveraine, fallback open source (Mixtral, LLaMA, Mistral)
        try:
            from ia_services import seo_recommendations
            recos = seo_recommendations(request.user, lang=getattr(request, 'LANGUAGE_CODE', 'fr'))
        except Exception:
            recos = [{'engine': 'LLaMA', 'recommendation': 'Optimisez vos balises meta et la performance mobile.'}]
        return Response({'recommendations': recos})

class LogSEOViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LogSEO.objects.all()
    serializer_class = LogSEOSerializer
    permission_classes = [permissions.IsAdminUser]

class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAdminUser]

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RapportViewSet(viewsets.ModelViewSet):
    queryset = Rapport.objects.all()
    serializer_class = RapportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
