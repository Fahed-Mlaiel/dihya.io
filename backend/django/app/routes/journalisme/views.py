"""
Views Journalisme (API ultra avancée, sécurité, accessibilité, multilingue)
"""
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleSerializer
from .permissions import IsAuteur

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuteur]
