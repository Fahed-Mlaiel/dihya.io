"""
Dihya – Views avancées pour le module Sport
- Sécurité, accessibilité, multilingue, RGPD, audit, documentation
"""
from rest_framework import viewsets, permissions
from .models import Club, Equipe, Athlete, Competition, Resultat
from .serializers import ClubSerializer, EquipeSerializer, AthleteSerializer, CompetitionSerializer, ResultatSerializer

class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [permissions.IsAuthenticated]

class EquipeViewSet(viewsets.ModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    permission_classes = [permissions.IsAuthenticated]

class AthleteViewSet(viewsets.ModelViewSet):
    queryset = Athlete.objects.all()
    serializer_class = AthleteSerializer
    permission_classes = [permissions.IsAuthenticated]

class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ResultatViewSet(viewsets.ModelViewSet):
    queryset = Resultat.objects.all()
    serializer_class = ResultatSerializer
    permission_classes = [permissions.IsAuthenticated]

# TODO: Ajouter EntrainementViewSet, BilletterieViewSet, IASportViewSet, NotificationViewSet, RapportViewSet, LogSportViewSet, AuditLogViewSet
