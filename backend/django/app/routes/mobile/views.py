"""
Dihya – Vues Django REST pour le module Mobile
- Sécurité, RBAC, accessibilité, RGPD
"""
from rest_framework import viewsets, permissions
from .models import MobileApp, Device, PushNotification
from .serializers import MobileAppSerializer, DeviceSerializer, PushNotificationSerializer
from .permissions import IsMobileAdminOrReadOnly

class MobileAppViewSet(viewsets.ModelViewSet):
    queryset = MobileApp.objects.all()
    serializer_class = MobileAppSerializer
    permission_classes = [IsMobileAdminOrReadOnly]

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsMobileAdminOrReadOnly]

class PushNotificationViewSet(viewsets.ModelViewSet):
    queryset = PushNotification.objects.all()
    serializer_class = PushNotificationSerializer
    permission_classes = [IsMobileAdminOrReadOnly]
