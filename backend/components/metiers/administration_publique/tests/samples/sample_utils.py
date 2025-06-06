# sample_utils.py – Exemples ultra avancés d’utilitaires pour tests, audit, conformité, RGPD
from ..utils.core.core_utils import generate_id, audit_log
from ..utils.i18n.i18n_utils import translate
from ..utils.rbac.rbac_utils import has_permission

def sample_user():
    return {
        'id': generate_id('user'),
        'username': 'sampleuser',
        'email': 'sample@dihya.io',
        'roles': ['admin', 'auditor']
    }

def sample_audit_action():
    user = sample_user()
    return audit_log('SAMPLE_ACTION', user['id'], {'lang': translate('audit', 'fr')})

def sample_permission_check():
    user = sample_user()
    return has_permission(user, 'audit')
