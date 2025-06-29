# helper_accessibility.py – Helpers d’accessibilité (Python)
def is_accessible(element):
    """Vérifie l’accessibilité d’un élément."""
    return hasattr(element, "aria_label")
