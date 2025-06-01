"""
Dihya – Vues Django REST pour le module Restauration
- Sécurité, RBAC, accessibilité, RGPD
"""
from rest_framework import viewsets, permissions
from .models import Restaurant, Menu, Reservation
from .serializers import RestaurantSerializer, MenuSerializer, ReservationSerializer
from .permissions import IsRestaurationAdminOrReadOnly

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsRestaurationAdminOrReadOnly]

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsRestaurationAdminOrReadOnly]

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsRestaurationAdminOrReadOnly]
