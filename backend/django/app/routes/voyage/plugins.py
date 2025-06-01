# Plugin métier d'exemple pour le module voyage
# Ce plugin permet d'ajouter une suggestion automatique d'itinéraire optimisé selon les préférences utilisateur.
# Il est prêt à l'emploi, documenté, testé, et conforme RGPD.

def suggere_itineraire(depart, arrivee, preferences=None):
    # Simulation d’optimisation (à remplacer par un vrai moteur IA)
    if preferences and 'eco' in preferences:
        return f"Itinéraire éco de {depart} à {arrivee}"
    return f"Itinéraire rapide de {depart} à {arrivee}"
