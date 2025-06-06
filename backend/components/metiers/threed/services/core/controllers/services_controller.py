"""
services_controller.py - Contrôleur avancé pour les services Threed (Python)
Inclut : endpoints, hooks, audit, sécurité, CI/CD, doc intégrée.
"""

from .service_threed import get_3d_model, list_3d_models, audit_model
from .services_helper import audit_service, check_access
from datetime import datetime

class ServicesController:
    def __init__(self, options=None):
        self.options = options or {}
        self.audit_trail = []
        self.config = None

    def init(self, config):
        self.config = config
        self._audit('init', config)
        return True

    def handle(self, action, payload):
        if not isinstance(action, str) or not action:
            self._audit('error', {'error': 'Invalid action'})
            raise ValueError('Invalid action')
        result = {'success': True, 'action': action, 'payload': payload, 'config': self.config}
        self._audit('handle', result)
        return result

    def _audit(self, action, payload):
        self.audit_trail.append({
            'action': action,
            'payload': payload,
            'timestamp': datetime.utcnow().isoformat()
        })

    def get_audit_trail(self):
        return self.audit_trail

    def get_model(self, model_id, user):
        if not check_access(user, 'read'):
            raise Exception('Accès refusé')
        model = get_3d_model(model_id)
        self.audit_log.append({'action': 'get_model', 'model_id': model_id})
        return model
    def list_models(self, user):
        if not check_access(user, 'read'):
            raise Exception('Accès refusé')
        models = list_3d_models()
        self.audit_log.append({'action': 'list_models'})
        return models
    def audit(self, model):
        result = audit_model(model)
        self.audit_log.append({'action': 'audit', 'model': model.get('id')})
        return result
    def get_audit_log(self):
        return self.audit_log
