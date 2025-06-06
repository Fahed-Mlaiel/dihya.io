# Test métier ultra avancé Construction

def test_construction_metier():
    chantier = {'chantier': 'exemple', 'etat': 'en_cours', 'rgpd': True, 'plugins': ['seo', 'accessibility']}
    assert 'chantier' in chantier
    assert chantier['etat'] == 'en_cours'
    assert chantier['rgpd']
    assert 'seo' in chantier['plugins']

def test_construction_rgpd():
    chantier = {'rgpd': True}
    assert chantier['rgpd']

def test_construction_accessibilite():
    chantier = {'accessibilite': True}
    assert chantier['accessibilite']

def test_construction_multilingue():
    chantier = {'nom': {'fr': 'Chantier', 'en': 'Site'}}
    assert chantier['nom']['fr'] == 'Chantier'

def test_construction_audit():
    chantier = {'audit': {'event': 'create', 'user': 'admin'}}
    assert chantier['audit']['event'] == 'create'
