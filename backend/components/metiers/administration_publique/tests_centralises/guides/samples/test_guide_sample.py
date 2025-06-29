# test___init__.py – Tests guides samples (Python)
def test___init___content():
    assert "sample" in "guide sample python – métier administration_publique".lower()

def test_print_guide_output(capsys):
    from backend.components.metiers.administration_publique.guides.samples import guide_sample
    guide_sample.print_guide()
    captured = capsys.readouterr()
    assert "Guide sample Python" in captured.out
