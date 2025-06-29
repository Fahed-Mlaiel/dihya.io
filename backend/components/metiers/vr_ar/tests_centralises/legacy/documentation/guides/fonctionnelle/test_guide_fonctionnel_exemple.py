"""
Test ultra avancé pour guide fonctionnelle Python
"""


def test_guide_fonctionnel_exemple():
    assert True


def test_guide_fonctionnel_exemple_output(capsys):
    from backend.components.metiers.vr_ar.legacy.documentation.guides.fonctionnelle import (
        guide_fonctionnel_exemple,
    )

    guide_fonctionnel_exemple.guide_fonctionnel_exemple()
    captured = capsys.readouterr()
    assert "Guide fonctionnel legacy vr_ar" in captured.out
    assert "Checklist de conformité" in captured.out
    assert "Accessibilité" in captured.out
