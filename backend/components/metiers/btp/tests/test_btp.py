# Test BTP principal
def test_btp_main():
    assert 'chantier' in {'chantier': 'test'}

def test_btp_audit():
    from ..utils.audit import auditChantier
    chantier = {'id': 1, 'etat': 'en_cours'}
    log = auditChantier(chantier)
    assert log['event'] == 'audit'

def test_btp_anonymisation():
    from ..utils.sample_util import anonymiser_chantier
    chantier = {'id': 1, 'responsable': 'Chef'}
    anonyme = anonymiser_chantier(chantier)
    assert anonyme['responsable'] == 'ANONYMISED'
