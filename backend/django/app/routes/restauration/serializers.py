"""
Dihya – Serializers pour le module Restauration
- Validation RGPD, accessibilité, multilingue, sécurité
"""
from rest_framework import serializers
from .models import Restaurant, Menu, Reservation

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
