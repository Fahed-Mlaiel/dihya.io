"""
Hooks custom event threed (Python)
"""


def before_custom_event(event, data):
    # Logique avant événement custom
    return {"event": event, "data": data}


def after_custom_event(event, data):
    # Logique après événement custom
    return {"event": event, "data": data}
