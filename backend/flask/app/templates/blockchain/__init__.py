"""
Template Blockchain – Flask
- Sécurité, i18n, plugins, multitenancy, audit, RGPD
- Prêt à l’emploi, extensible, documenté
"""

from .template import blockchain_bp
bp_blockchain = blockchain_bp
__all__ = ["blockchain_bp", "bp_blockchain"]
