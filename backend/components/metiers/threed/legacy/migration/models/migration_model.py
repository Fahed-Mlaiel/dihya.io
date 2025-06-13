"""
Modèle de données de migration legacy Threed (Python)
Ultra avancé, clé en main, conforme au cahier des charges.
"""


class MigrationLog:
    def __init__(self, source, target, status, details=None):
        self.source = source
        self.target = target
        self.status = status
        self.details = details or {}

    def to_dict(self):
        return {
            "source": self.source,
            "target": self.target,
            "status": self.status,
            "details": self.details,
        }
