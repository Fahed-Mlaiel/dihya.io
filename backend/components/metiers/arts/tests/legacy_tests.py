# Tests legacy pour le module Arts

def test_legacy_artworks():
    from ..legacy.api_legacy import getLegacyArtworks
    artworks = getLegacyArtworks()
    assert len(artworks) == 2
    assert artworks[0]['titre'] == 'La Joconde'
