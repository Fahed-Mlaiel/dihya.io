# Entrée principale ultra avancée pour le module Automobile, démonstration de toutes les fonctionnalités métier, plugins, audit, RGPD, export, anonymisation, multilingue, conformité CI/CD.
from .automobile import Automobile
from .plugins import PluginAuto, plugin_manager_auto
from .validators import validate_automobile
from .schemas import AutomobileSchema

def main():
    projet = Automobile('Voiture électrique', 'actif', 'Alice', '2025-01-01', '2026-01-01')
    print('Projet:', projet)
    print('Export:', projet.exporter_projet())
    projet.auditer('test_audit', {'test': True})
    projet.anonymiser()
    print('Après anonymisation:', projet.exporter_projet())
    # Validation schéma
    schema = AutomobileSchema(**projet.exporter_projet())
    print('Validation schéma:', schema)
    # Plugins
    plugin = PluginAuto()
    plugin_manager_auto.register(plugin)
    data = plugin_manager_auto.process_all(projet.exporter_projet())
    print('Données après plugins:', data)

if __name__ == '__main__':
    main()
