# Exemple d’utilisation avancée du moteur RBAC (Python)
from ...engine import rbac_engine

rbac_engine.check_access('user1', 'resource1', 'read')
