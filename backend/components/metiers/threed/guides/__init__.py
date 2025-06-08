# __init__.py – Initialisation des guides Threed

# Point d’entrée guides ultra avancé, clé en main
# from core.guide_plugins import get_plugin_guide  # Suppression ou correction car ce module n'existe pas dans la structure métier Python
# from helpers.helpers_plugins import validate_plugin_config  # supprimé car le module n'existe pas en Python
# from fallback.fallback_plugins import fallback_plugin_config  # supprimé car le module n'existe pas en Python
# from core.guide_services import get_service_guide  # supprimé car le module n'existe pas en Python
from helpers.helpers_services import validate_service_config
from fallback.fallback_services import fallback_service_config
from core.guide_accessibility import get_accessibility_guide
from helpers.helpers_accessibility import validate_accessibility_config
from fallback.fallback_accessibility import fallback_accessibility_config
# autres guides à ajouter ici
