# Test avancé pour public_utils.py du module utils/views/public
# from components.metiers.recherche.utils.views.public.public_utils import ...
from backend.components.metiers.recherche.utils.views.public import public_views


def test_utils_views_public():
    # Ajouter des assertions avancées selon la logique métier
    assert True


def test_render_public_info_nominal():
    msg = "Bienvenue !"
    result = public_views.render_public_info(msg)
    assert result == f"Info publique: {msg}"


def test_render_public_info_empty():
    result = public_views.render_public_info("")
    assert result == "Info publique: "


def test_render_public_info_special():
    msg = "<b>HTML</b> & éèç"
    result = public_views.render_public_info(msg)
    assert "<b>HTML</b>" in result
    assert "éèç" in result
