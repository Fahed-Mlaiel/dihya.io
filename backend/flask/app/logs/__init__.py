"""
Initialisation du module de logs structurés pour Dihya Coding.

Ce package centralise la configuration et l’utilisation du logger structuré (JSON)
pour garantir la traçabilité, l’auditabilité et la compatibilité avec les outils modernes (ELK, Datadog, etc.).

Bonnes pratiques :
- Importer ici le helper principal get_logger
- Ne jamais logger de données personnelles ou sensibles
- Prévoir l’extensibilité pour de nouveaux formats ou destinations de logs
- Documenter l’usage du logger dans l’application
"""

from .structured_logger import get_logger