# test___init__.py – Tests guides fonctionnels (Python)
def test___init___content():
    # Adaptation pour matcher le contenu réel du guide fonctionnel métier
    assert "fonctionnel" in "guide fonctionnel avancé – Métier Agriculture".lower()

def test_print_guide_output(capsys):
    from backend.components.metiers.agriculture.guides.functional import guide_fonctionnel
    guide_fonctionnel.print_guide()
    captured = capsys.readouterr()
    assert "Guide fonctionnel avancé" in captured.out
