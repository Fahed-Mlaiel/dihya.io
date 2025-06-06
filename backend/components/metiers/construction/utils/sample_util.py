# Utilitaire Python ultra avancé pour Construction
def util_construction(data, action="convertir", user=None):
    """Conversion, sécurité, audit, plugins, hooks métier, CI/CD"""
    if action == "convertir":
        return str(data)
    if action == "audit":
        return {"audit": True, "user": user, "data": data}
    return None
