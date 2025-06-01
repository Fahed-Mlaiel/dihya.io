from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Scene, Asset
from .serializers import SceneSerializer, AssetSerializer
from .permissions import IsSceneOwnerOrReadOnly, IsAssetManagerOrReadOnly
from .audit import vr_ar_audit_logger
from .i18n import VR_AR_I18N

class SceneViewSet(viewsets.ModelViewSet):
    queryset = Scene.objects.all()
    serializer_class = SceneSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsSceneOwnerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        vr_ar_audit_logger.log(self.request.user, 'create', 'Scene', obj.id, details=obj.title, language=obj.lang)

    def perform_destroy(self, instance):
        vr_ar_audit_logger.log(self.request.user, 'delete', 'Scene', instance.id, details=instance.title, language=instance.lang)
        instance.delete()

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAssetManagerOrReadOnly]

    def perform_create(self, serializer):
        obj = serializer.save()
        vr_ar_audit_logger.log(self.request.user, 'upload', 'Asset', obj.id, details=obj.file.name, language=obj.lang)
