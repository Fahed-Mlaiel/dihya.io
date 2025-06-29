# test___init__.py – Tests guides intégration (Python)
def test___init___content():
    assert "intégration" in "guide intégration avancé – Métier administration_publique".lower()

def test_print_guide_output(capsys):
    from backend.components.metiers.administration_publique.guides.integration import guide_integration
    guide_integration.print_guide()
    captured = capsys.readouterr()
    assert "Guide intégration avancé" in captured.out
