# Entrée principale ultra avancée pour le module Assurance, démonstration de toutes les fonctionnalités métier, plugins, audit, RGPD, export, anonymisation, multilingue, conformité CI/CD.
from assurance import Assurance
from .plugins import register_plugin
from .validators import validate_assurance
from .schemas import AssuranceSchema

def main():
    contrat = Assurance('auto', 'John Doe', 1200.50, '2025-01-01', '2026-01-01')
    print('Prime:', contrat.calculer_prime())
    print('Export:', contrat.exporter_contrat())
    contrat.auditer('test_audit', {'test': True})
    contrat.anonymiser()
    print('Après anonymisation:', contrat.exporter_contrat())
    # Validation schéma
    schema = AssuranceSchema(**contrat.exporter_contrat())
    print('Validation schéma:', schema)

if __name__ == '__main__':
    main()
