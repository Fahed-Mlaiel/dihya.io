# test___init__.py – Tests guides samples (Python)
def test___init___content():
    assert "sample" in "guide sample python – métier vr_ar".lower()

def test_print_guide_output(capsys):
    from backend.components.metiers.vr_ar.guides.samples import guide_sample
    guide_sample.print_guide()
    captured = capsys.readouterr()
    assert "Guide sample Python" in captured.out
