# fallback.py
# Fallback validator Python pour Immobilier – exemple clé en main


def validator_fallback(value):
    """
    Fallback minimal : valide toujours (utilisé en cas d'échec du vrai validateur)
    """
    return True
