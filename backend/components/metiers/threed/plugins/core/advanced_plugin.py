# advanced_plugin.py – Plugin avancé Python (exemple clé en main)
class AdvancedPlugin:
    def __init__(self):
        self.activated = False
        self.audit_trail = []
    def activate(self, ctx):
        self.activated = True
        self.audit_trail.append({'event': 'activate', 'ctx': ctx})
    def run(self, data):
        if not self.activated:
            raise Exception('Plugin non activé')
        self.audit_trail.append({'event': 'run', 'data': data})
        result = data.copy() if isinstance(data, dict) else {'value': data}
        result['plugin'] = 'advanced'
        result['status'] = 'ok'
        return result
    def get_audit_trail(self):
        return self.audit_trail
