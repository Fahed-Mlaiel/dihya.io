"""
templates_helper.py – Fonctions utilitaires pour les templates Sport (Python)
Inclut : helpers, mocks, validateurs, génération, audit, sécurité, CI/CD
"""

from jinja2 import Environment, FileSystemLoader
import os
from datetime import datetime


def render_template(template_name, **kwargs):
    env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))
    template = env.get_template(template_name)
    return template.render(**kwargs)


def is_valid_template(template_name):
    return template_name.endswith((".html.j2", ".json.j2", ".xml", ".txt"))


def mock_template_context():
    return {
        "model_name": "Cube Ultra",
        "status": "OK",
        "date": "2025-06-03",
        "result": "OK",
        "details": "Test",
    }


class TemplatesHelper:
    def __init__(self, options=None):
        self.options = options or {}
        self.audit_trail = []
        self.config = None

    def init(self, config):
        self.config = config
        self._audit("init", config)
        return True

    def assist(self, operation, data):
        if not isinstance(operation, str) or not operation:
            self._audit("error", {"error": "Invalid operation"})
            raise ValueError("Invalid operation")
        result = {
            "success": True,
            "operation": operation,
            "data": data,
            "config": self.config,
        }
        self._audit("assist", result)
        return result

    def _audit(self, action, payload):
        self.audit_trail.append(
            {
                "action": action,
                "payload": payload,
                "timestamp": datetime.utcnow().isoformat(),
            }
        )

    def get_audit_trail(self):
        return self.audit_trail


# Exemples d’utilisation, edge cases, synchronisation JS/Python
