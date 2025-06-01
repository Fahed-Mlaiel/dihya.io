# Test plugin pour le module voyage
# Vérifie la suggestion d’itinéraire automatique.

from ..plugins import suggere_itineraire

def test_suggere_itineraire_eco():
    result = suggere_itineraire('Paris', 'Marseille', preferences=['eco'])
    assert 'éco' in result

def test_suggere_itineraire_rapide():
    result = suggere_itineraire('Paris', 'Marseille')
    assert 'rapide' in result
