# Test plugin pour le module vr_ar
# Vérifie la génération automatique de scène.

from ..plugins import generer_scene_auto

def test_generer_scene_auto_fr():
    result = generer_scene_auto('Musée', 'Visite immersive', lang='fr')
    assert '[Auto]' in result['title']
    assert '[Généré automatiquement]' in result['description']
