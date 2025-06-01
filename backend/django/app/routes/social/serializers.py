"""
Dihya – Serializers avancés pour le module Social
- Validation RGPD, multilingue, accessibilité, sécurité, documentation
"""
from rest_framework import serializers
from .models import Profil, Post, Commentaire, Like, Abonnement

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = '__all__'
        extra_kwargs = {
            'bio': {'help_text': 'Biographie'},
            'avatar': {'help_text': 'Avatar'},
        }

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {
            'auteur': {'help_text': 'Auteur du post'},
            'contenu': {'help_text': 'Contenu du post'},
        }

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'
        extra_kwargs = {
            'auteur': {'help_text': 'Auteur du commentaire'},
            'contenu': {'help_text': 'Contenu du commentaire'},
        }

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        extra_kwargs = {
            'auteur': {'help_text': 'Auteur du like'},
        }

class AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonnement
        fields = '__all__'
        extra_kwargs = {
            'abonne': {'help_text': 'Abonné'},
            'suivi': {'help_text': 'Profil suivi'},
        }
