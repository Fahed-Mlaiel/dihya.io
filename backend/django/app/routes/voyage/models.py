from django.db import models
from django.conf import settings

class Itineraire(models.Model):
    depart = models.CharField(max_length=128, help_text="Ville de départ")
    arrivee = models.CharField(max_length=128, help_text="Ville d'arrivée")
    distance_km = models.PositiveIntegerField(help_text="Distance en kilomètres")
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='itineraires_gérés')

    class Meta:
        app_label = 'voyage'

    def __str__(self):
        return f"{self.depart} → {self.arrivee} ({self.distance_km} km)"

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reservations')
    voyage = models.CharField(max_length=256, help_text="Nom du voyage ou itinéraire")
    date = models.DateTimeField(help_text="Date de la réservation")
    status = models.CharField(max_length=64, help_text="Statut de la réservation (confirmée, annulée, etc.)")
    lang = models.CharField(max_length=16, default='fr', help_text="Langue de la réservation")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'voyage'

    def __str__(self):
        return f"{self.voyage} ({self.status}) - {self.user}"
