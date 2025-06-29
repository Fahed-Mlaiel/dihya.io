# fallback.py
# Fallback validator Python pour Ressources_humaines – exemple clé en main


def validator_fallback(value):
    """
    Fallback minimal : valide toujours (utilisé en cas d'échec du vrai validateur)
    """
    return True
