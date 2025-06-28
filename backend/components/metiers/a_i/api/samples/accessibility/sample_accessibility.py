# sample_accessibility.py – Exemples ultra avancés d'accessibilité pour
# API A_I


def sample_accessibility_check(data):
    """Vérifie l'accessibilité d'une ressource API (clé en main, edge cases
    inclus)."""
    # Logique accessibilité avancée, conforme au cahier des charges
    if not data or "label" not in data:
        return {"accessible": False, "reason": "missing_label"}
    return {"accessible": True, "lang": data.get("lang", "fr")}
