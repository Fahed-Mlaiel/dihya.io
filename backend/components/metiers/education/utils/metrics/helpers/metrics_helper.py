# metrics_helper.py
# Helper metrics Python pour Education – exemple clé en main


def average(values):
    """
    Calcule la moyenne d'une liste de valeurs numériques
    """
    if not values:
        return 0
    return sum(values) / len(values)
