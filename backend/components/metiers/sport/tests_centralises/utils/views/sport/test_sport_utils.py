# Test avancé pour sport_utils.py du module utils/views/sport
# from components.metiers.sport.utils.views.sport.sport_utils import ...
from backend.components.metiers.sport.utils.views.sport import sport_views


def test_utils_views_sport():
    # Ajouter des assertions avancées selon la logique métier
    assert True


def test_render_sport_nominal():
    model = "Cube"
    result = sport_views.render_sport(model)
    assert "Cube" in result
    assert result.startswith("Rendu sport du modèle:")


def test_render_sport_empty():
    result = sport_views.render_sport("")
    assert result.startswith("Rendu sport du modèle:")
    assert result.endswith(": ") or result.endswith(":")


def test_render_sport_special():
    model = "<b>sport</b> & éèç"
    result = sport_views.render_sport(model)
    assert "<b>sport</b>" in result
    assert "éèç" in result
