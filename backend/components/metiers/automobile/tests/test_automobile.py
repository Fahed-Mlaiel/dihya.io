# Test principal automobile ultra avancé
from ..automobile import Automobile
from ..plugins import PluginAuto, plugin_manager_auto
from ..schemas import AutomobileSchema

def test_automobile_creation():
    auto = Automobile('Test', 'actif', 'Bob', '2025-01-01', '2026-01-01')
    assert auto.nom == 'Test'
    assert auto.statut == 'actif'
    assert auto.proprietaire == 'Bob'
    auto.auditer('creation', {'user': 'Bob'})
    assert len(auto.logs) == 1
    auto.anonymiser()
    assert auto.proprietaire == 'ANONYMISED'
    # Validation schéma
    schema = AutomobileSchema(**auto.exporter_projet())
    assert schema.nom == 'Test'
    # Plugins
    plugin = PluginAuto()
    plugin_manager_auto.register(plugin)
    data = plugin_manager_auto.process_all(auto.exporter_projet())
    assert data['nom'] == 'Test'
