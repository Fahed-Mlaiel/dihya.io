"""
Gestion avancée des plugins BTP (ajout, suppression, audit, sécurité, i18n).
"""
from typing import List, Dict, Any
import logging

class BTPPluginManager:
    def __init__(self):
        self.plugins: List[Dict[str, Any]] = []
        self.audit_logger = logging.getLogger("dihya.btp.plugins")

    def register_plugin(self, plugin: Dict[str, Any]) -> None:
        plugin['anonymized'] = True
        self.plugins.append(plugin)
        self.audit_logger.info(f"[PLUGIN][REGISTER] {plugin.get('name')} {plugin.get('version')}")

    def remove_plugin(self, name: str) -> None:
        self.plugins = [p for p in self.plugins if p.get('name') != name]
        self.audit_logger.info(f"[PLUGIN][REMOVE] {name}")

    def list_plugins(self, lang: str = 'fr') -> List[Dict[str, Any]]:
        for p in self.plugins:
            if 'description' in p and isinstance(p['description'], dict):
                p['description_localized'] = p['description'].get(lang, p['description'].get('en', ''))
        return self.plugins

    def audit_plugins(self):
        for p in self.plugins:
            self.audit_logger.info(f"[PLUGIN][AUDIT] {p.get('name')} {p.get('version')}")

    def fallback_plugin(self, name: str):
        return {'name': name, 'status': 'fallback', 'message': 'Plugin non disponible'}

plugin_manager = BTPPluginManager()
plugin_manager.register_plugin({
    'name': 'gestion_chantiers',
    'version': '1.0',
    'description': {
        'fr': 'Gestion intelligente des chantiers',
        'en': 'Smart site management',
        'ar': 'إدارة ذكية للمشاريع',
        'tzm': 'Asefru n chantier',
    },
    'author': 'Dihya',
    'license': 'AGPL',
    'multitenant': True,
    'accessibility': True,
    'rgpd_ready': True,
    'ci_cd_ready': True,
})
