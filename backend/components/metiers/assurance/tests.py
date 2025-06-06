# Tests principaux pour Assurance
def test_prime():
    from .assurance import Assurance
    contrat = Assurance('auto', 'John Doe', 1200.50, '2025-01-01', '2026-01-01')
    assert contrat.calculer_prime() == 1200.50

def test_export():
    from .assurance import Assurance
    contrat = Assurance('auto', 'John Doe', 1200.50, '2025-01-01', '2026-01-01')
    data = contrat.exporter_contrat()
    assert data['type_assurance'] == 'auto'
    assert data['client'] == 'John Doe'

def test_anonymisation():
    from .assurance import Assurance
    contrat = Assurance('auto', 'John Doe', 1200.50, '2025-01-01', '2026-01-01')
    contrat.anonymiser()
    assert contrat.client == 'ANONYMISED'
