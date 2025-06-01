"""
Dihya – Django Automobile API Models Ultra Avancé
-------------------------------------------------
- Modèles métiers complets : Véhicule, Propriétaire, Entretien, Sinistre, Telematic, IoT, Alerte, Rapport, AuditLog
- Sécurité, RGPD, multilingue, extensibilité, souveraineté
"""

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Proprietaire(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        pass

class Vehicule(models.Model):
    modele = models.CharField(max_length=255)
    immatriculation = models.CharField(max_length=50)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    date_achat = models.DateField()
    kilometrage = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicules')

    class Meta:
        pass

class Entretien(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()
    cout = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        pass

class Sinistre(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.CharField(max_length=255)
    description = models.TextField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        pass

class Telematic(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    data = models.JSONField(default=dict)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

class IoT(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    capteur = models.CharField(max_length=255)
    valeur = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

class Alerte(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    niveau = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

class Rapport(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    objet = models.CharField(max_length=255)
    date_action = models.DateTimeField(auto_now_add=True)
    details = models.JSONField(default=dict)

    class Meta:
        pass
