# fallback.py
# Fallback d'export Python pour A_I – exemple clé en main
from datetime import datetime

fallback_exports = []


def export_fallback(data=None):
    """
    Fallback minimal : export en mémoire si la persistance échoue
    """
    if data is None:
        data = {}
    export_obj = {"timestamp": datetime.utcnow().isoformat() + "Z", **data}
    fallback_exports.append(export_obj)
    return export_obj
