# Tests legacy pour BTP
def test_legacy_chantier():
    assert True

def test_legacy_audit():
    from ..legacy.api_legacy import auditLegacy, getOldChantier
    chantier = getOldChantier()
    log = auditLegacy(chantier)
    assert log['event'] == 'legacy_access'

def test_legacy_anonymisation():
    from ..legacy.api_legacy import anonymiseLegacy, getOldChantier
    chantier = getOldChantier()
    anonyme = anonymiseLegacy(chantier)
    assert anonyme['responsable'] == 'ANONYMISED'
