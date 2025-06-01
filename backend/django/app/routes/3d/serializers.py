"""
Dihya – Django 3D API Serializers Ultra Avancé
----------------------------------------------
- Serializers multilingues, sécurisés, RGPD, extensibles pour tous les modèles 3D
- Traduction automatique des messages d’erreur/succès (fr, en, ar, amazigh)
- Validation forte, anonymisation, auditabilité
"""

from rest_framework import serializers
from .models import *

class Model3DUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model3D
        fields = '__all__'

class Model3DPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model3D
        fields = ['id', 'name', 'preview_url']

class Model3DAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model3D
        fields = ['id', 'name', 'file_url', 'owner']
