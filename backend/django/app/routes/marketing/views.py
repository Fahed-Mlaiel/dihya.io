"""
Dihya – Vues avancées Django REST pour le module Marketing
- Sécurité, RBAC, multilingue, accessibilité, RGPD, audit, souveraineté
"""
from rest_framework import viewsets, permissions
from .models import Campagne, Lead, Audience, Canal, Contenu, Analytics, ABTesting, Notification, Rapport, AuditLog
from .serializers import (
    CampagneSerializer, LeadSerializer, AudienceSerializer, CanalSerializer, ContenuSerializer,
    AnalyticsSerializer, ABTestingSerializer, NotificationSerializer, RapportSerializer, AuditLogSerializer
)
from .permissions import IsMarketingAdminOrReadOnly

class CampagneViewSet(viewsets.ModelViewSet):
    queryset = Campagne.objects.all()
    serializer_class = CampagneSerializer
    permission_classes = [IsMarketingAdminOrReadOnly]

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    permission_classes = [IsMarketingAdminOrReadOnly]

class AudienceViewSet(viewsets.ModelViewSet):
    queryset = Audience.objects.all()
    serializer_class = AudienceSerializer
    permission_classes = [IsMarketingAdminOrReadOnly]

class CanalViewSet(viewsets.ModelViewSet):
    queryset = Canal.objects.all()
    serializer_class = CanalSerializer
    permission_classes = [IsMarketingAdminOrReadOnly]

class ContenuViewSet(viewsets.ModelViewSet):
    queryset = Contenu.objects.all()
    serializer_class = ContenuSerializer
    permission_classes = [IsMarketingAdminOrReadOnly]

class AnalyticsViewSet(viewsets.ModelViewSet):
    queryset = Analytics.objects.all()
    serializer_class = AnalyticsSerializer
    permission_classes = [IsMarketingAdminOrReadOnly]

class ABTestingViewSet(viewsets.ModelViewSet):
    queryset = ABTesting.objects.all()
    serializer_class = ABTestingSerializer
    permission_classes = [IsMarketingAdminOrReadOnly]

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsMarketingAdminOrReadOnly]

class RapportViewSet(viewsets.ModelViewSet):
    queryset = Rapport.objects.all()
    serializer_class = RapportSerializer
    permission_classes = [IsMarketingAdminOrReadOnly]

class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAdminUser]
