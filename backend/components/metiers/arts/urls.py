# URLs pour le module Arts

from .views import accueil, liste_expositions, liste_oeuvres, recherche_oeuvre_view

routes = [
    {"path": "/arts", "view": accueil, "methods": ["GET"]},
    {"path": "/arts/expositions", "view": liste_expositions, "methods": ["GET"]},
    {"path": "/arts/oeuvres", "view": liste_oeuvres, "methods": ["GET"]},
    {"path": "/arts/recherche/<nom>", "view": recherche_oeuvre_view, "methods": ["GET"]}
]
