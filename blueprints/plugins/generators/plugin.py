"""
Générateur de plugin Python ultra avancé, clé en main.
Permet de créer dynamiquement des plugins métiers avec hooks, configuration, et extension.
"""

def create_plugin(metier: str, config: dict = None, hooks: dict = None) -> dict:
    """
    Génère un plugin métier clé en main.
    - metier : nom du métier
    - config : configuration spécifique (optionnelle)
    - hooks : hooks personnalisés (optionnels)
    Retourne un dictionnaire représentant le plugin prêt à l'emploi.
    """
    plugin = {
        "metier": metier,
        "config": config or {},
        "hooks": hooks or {},
        "enabled": True,
        "activate": lambda: f"Plugin {metier} activé",
        "deactivate": lambda: f"Plugin {metier} désactivé",
    }
    # Extension possible : ajout de méthodes dynamiques, validation, etc.
    return plugin
