# monitoring_sample.py – Exemple de monitoring ultra avancé


def monitoring_sample(metric, value):
    """Simule une alerte monitoring legacy Industrie"""
    # ... logique de monitoring avancée ...
    return (
        f"ALERT: {metric} dépasse le seuil!"
        if value > 100
        else f"OK: {metric}"
    )
