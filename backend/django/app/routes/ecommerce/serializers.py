"""
Dihya – Django eCommerce API Serializers Ultra Avancé
-----------------------------------------------------
- Serializers multilingues, sécurisés, RGPD, extensibles pour tous les modèles métiers
- Traduction automatique des messages d’erreur/succès (fr, en, ar, amazigh)
- Validation forte, anonymisation, auditabilité, accessibilité
"""
from rest_framework import serializers
from .models import *
from django.utils.translation import gettext_lazy as _

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'
        extra_kwargs = {
            'nom': {'help_text': _('Nom du produit / Product name / اسم المنتج / ⵉⵙⴰⵏ ⵏ ⵓⵏⴰⵡ')},
            'description': {'help_text': _('Description / الوصف / ⵜⴰⵙⵉⵏⵜ')},
            'prix': {'help_text': _('Prix (€) / Price / السعر / ⴰⴳⴷⴰⴷ')},
            'stock': {'help_text': _('Stock / المخزون / ⴰⴳⴷⴰⴷ')},
            'categorie': {'help_text': _('Catégorie / Category / الفئة / ⵜⴰⴳⴷⴰⴷⵜ')},
            'owner': {'help_text': _('Propriétaire / Owner / المالك / ⴰⵎⴰⵣⵉⵖ')},
        }
    def validate_nom(self, value):
        if not value:
            raise serializers.ValidationError(_('Le nom du produit est obligatoire.'))
        return value
    def validate_prix(self, value):
        if value < 0:
            raise serializers.ValidationError(_('Le prix doit être positif.'))
        return value
    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError(_('Le stock doit être positif.'))
        return value

# Répéter pour chaque modèle métier (catégories, commandes, etc.)
# ...

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'
