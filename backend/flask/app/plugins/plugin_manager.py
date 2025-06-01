# plugin_manager.py – Plugin-Manager-Stub für Kompatibilität

class Plugin:
    def __init__(self, name):
        self.name = name
    def run_analysis(self, data):
        return {"score": 100, "data": data}

def get_plugin(name):
    # Gibt einen generischen Plugin-Stub zurück
    return Plugin(name)
