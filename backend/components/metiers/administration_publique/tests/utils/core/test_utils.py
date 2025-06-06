from .core_utils import audit_log
from ..i18n.i18n_utils import translate

def auditThreed(payload):
    # Simule un audit ultra basique pour test
    return {'score': 97.0, 'payload': payload}

def i18n(msg, lang):
    return translate(msg, lang)

def test_audit_threed():
    result = auditThreed({'status': 'active'})
    assert 'score' in result
    assert result['score'] == 97.0

def test_i18n():
    assert '[FR]' in i18n('Test', 'fr')
    assert '[EN]' in i18n('Test', 'en')
    assert '[DE]' in i18n('Test', 'de')
