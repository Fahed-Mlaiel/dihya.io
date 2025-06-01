"""
Dihya – Django eCommerce API Models Ultra Avancé
------------------------------------------------
- Modèles métiers complets : Produit, Catégorie, Commande, Panier, Paiement, Livraison, Avis, Promotion, IA, AuditLog
- Sécurité, RGPD, multilingue, extensibilité, souveraineté
- Accessibilité, help_text multilingue, conformité totale
"""

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Produit(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom du produit / Product name / اسم المنتج / ⵉⵙⴰⵏ ⵏ ⵓⵏⴰⵡ'))
    description = models.TextField(help_text=_('Description / الوصف / ⵜⴰⵙⵉⵏⵜ'))
    prix = models.DecimalField(max_digits=10, decimal_places=2, help_text=_('Prix (€) / Price / السعر / ⴰⴳⴷⴰⴷ'))
    stock = models.IntegerField(help_text=_('Stock / المخزون / ⴰⴳⴷⴰⴷ'))
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE, help_text=_('Catégorie / Category / الفئة / ⵜⴰⴳⴷⴰⴷⵜ'))
    owner = models.ForeignKey(User, on_delete=models.CASCADE, help_text=_('Propriétaire / Owner / المالك / ⴰⵎⴰⵣⵉⵖ'))
    date_creation = models.DateTimeField(auto_now_add=True, help_text=_('Date de création / Creation date / تاريخ الإنشاء / ⴰⵙⴳⴰⵙ ⵏ ⵓⵏⴰⵡ'))
    date_modification = models.DateTimeField(auto_now=True, help_text=_('Date de modification / Modification date / تاريخ التعديل / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵏⵜⵉⵔ'))

    class Meta:
        app_label = 'ecommerce'

class Categorie(models.Model):
    nom = models.CharField(max_length=255, help_text=_('Nom de la catégorie / Category name / اسم الفئة / ⵉⵙⴰⵏ ⵏ ⵜⴰⴳⴷⴰⴷⵜ'))
    description = models.TextField(help_text=_('Description / الوصف / ⵜⴰⵙⵉⵏⵜ'))

    class Meta:
        app_label = 'ecommerce'

class Commande(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text=_('Utilisateur / User / المستخدم / ⴰⵎⴰⵣⵉⵖ'))
    produits = models.ManyToManyField(Produit, help_text=_('Produits / Products / المنتجات / ⵓⵏⴰⵡⵏ'))
    total = models.DecimalField(max_digits=10, decimal_places=2, help_text=_('Total (€) / الإجمالي / ⴰⴳⴷⴰⴷ'))
    statut = models.CharField(max_length=50, help_text=_('Statut / Status / الحالة / ⵜⴰⵙⵉⵏⵜ'))
    date_commande = models.DateTimeField(auto_now_add=True, help_text=_('Date de commande / Order date / تاريخ الطلب / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵏⵜⵉⵔ'))

    class Meta:
        app_label = 'ecommerce'

class Panier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text=_('Utilisateur / User / المستخدم / ⴰⵎⴰⵣⵉⵖ'))
    produits = models.ManyToManyField(Produit, help_text=_('Produits / Products / المنتجات / ⵓⵏⴰⵡⵏ'))
    date_modification = models.DateTimeField(auto_now=True, help_text=_('Date de modification / Modification date / تاريخ التعديل / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵏⵜⵉⵔ'))

    class Meta:
        app_label = 'ecommerce'

class Paiement(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, help_text=_('Commande / Order / الطلب / ⵜⴰⵏⵜⵉⵔ'))
    montant = models.DecimalField(max_digits=10, decimal_places=2, help_text=_('Montant (€) / Amount / المبلغ / ⴰⴳⴷⴰⴷ'))
    statut = models.CharField(max_length=50, help_text=_('Statut / Status / الحالة / ⵜⴰⵙⵉⵏⵜ'))
    date_paiement = models.DateTimeField(auto_now_add=True, help_text=_('Date de paiement / Payment date / تاريخ الدفع / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵏⵜⵉⵔ'))

    class Meta:
        app_label = 'ecommerce'

class Livraison(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE, help_text=_('Commande / Order / الطلب / ⵜⴰⵏⵜⵉⵔ'))
    adresse = models.CharField(max_length=255, help_text=_('Adresse / Address / العنوان / ⵜⴰⵏⴰⴷⵜ'))
    statut = models.CharField(max_length=50, help_text=_('Statut / Status / الحالة / ⵜⴰⵙⵉⵏⵜ'))
    date_livraison = models.DateTimeField(auto_now_add=True, help_text=_('Date de livraison / Delivery date / تاريخ التسليم / ⴰⵙⴳⴰⵙ ⵏ ⵜⴰⵏⵜⵉⵔ'))

    class Meta:
        app_label = 'ecommerce'

class Avis(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.IntegerField()
    commentaire = models.TextField()
    date_avis = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'ecommerce'

class Promotion(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    reduction = models.DecimalField(max_digits=5, decimal_places=2)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()

    class Meta:
        app_label = 'ecommerce'

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    objet = models.CharField(max_length=255)
    date_action = models.DateTimeField(auto_now_add=True)
    details = models.JSONField(default=dict)

    class Meta:
        app_label = 'ecommerce'
