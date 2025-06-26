# fallback_service.py – Service fallback ultra avancé (clé en main)
def fallback_service(data):
    if not data:
        return {"fallback": True, "empty": True}
    result = data.copy() if isinstance(data, dict) else {"value": data}
    result["fallback"] = True
    result["status"] = "fallback"
    return result
