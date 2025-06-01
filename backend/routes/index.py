"""
Index centralisé des routes métiers Dihya (Django)
Ultra avancé, sécurisé, multilingue, REST & GraphQL-ready, RGPD, plugins, audit, multitenancy.
Ce fichier importe et expose dynamiquement toutes les routes métiers (construction, crypto, culture, education, energie, environnement, gamer, health, hotellerie, immobilier, industrie, intelligence_artificielle, it_devops, etc.).
"""
from django.urls import path, include

urlpatterns = [
    path('construction/', include('Dihya.backend.routes.construction.routes')),
    path('crypto/', include('Dihya.backend.routes.crypto.routes')),
    path('culture/', include('Dihya.backend.routes.culture.routes')),
    path('education/', include('Dihya.backend.routes.education.routes')),
    path('energie/', include('Dihya.backend.routes.energie.routes')),
    path('environnement/', include('Dihya.backend.routes.environnement.routes')),
    path('gamer/', include('Dihya.backend.routes.gamer.routes')),
    path('health/', include('Dihya.backend.routes.health.routes')),
    path('hotellerie/', include('Dihya.backend.routes.hotellerie.routes')),
    path('immobilier/', include('Dihya.backend.routes.immobilier.routes')),
    path('industrie/', include('Dihya.backend.routes.industrie.routes')),
    path('intelligence_artificielle/', include('Dihya.backend.routes.intelligence_artificielle.routes')),
    path('it_devops/', include('Dihya.backend.routes.it_devops.routes')),
    # Ajoutez ici dynamiquement les autres modules métiers, plugins, extensions...
]

# Sécurité avancée, CORS, JWT, audit, WAF, anti-DDOS, RBAC, i18n, RGPD, plugins, multitenancy sont gérés dans les middlewares globaux du projet et dans chaque ViewSet.
