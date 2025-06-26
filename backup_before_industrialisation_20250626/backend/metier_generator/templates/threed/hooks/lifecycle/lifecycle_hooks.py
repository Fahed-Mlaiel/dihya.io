"""
Hooks lifecycle threed (Python)
"""


def before_lifecycle_event(event, data):
    # Logique avant événement de cycle de vie
    return {"event": event, "data": data}


def after_lifecycle_event(event, data):
    # Logique après événement de cycle de vie
    return {"event": event, "data": data}
