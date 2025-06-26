# Test avancé pour tourisme_utils.py du module utils/views/tourisme
# from components.metiers.tourisme.utils.views.tourisme.tourisme_utils import ...
from backend.components.metiers.tourisme.views.core import views as tourisme_views


def test_utils_views_tourisme():
    # Test basique de présence de fonction
    assert hasattr(tourisme_views, "render_home")
    assert hasattr(tourisme_views, "render_model")


def test_render_tourisme_nominal():
    model = {"name": "Cube"}
    result = tourisme_views.render_model(model)
    assert "Cube" in result
    assert result.startswith("<div>Modèle:")


def test_render_tourisme_empty():
    result = tourisme_views.render_model({"name": ""})
    assert result.startswith("<div>Modèle:")
    assert result.endswith("</div>")


def test_render_tourisme_special():
    model = {"name": "<b>tourisme</b> & éèç"}
    result = tourisme_views.render_model(model)
    assert "<b>tourisme</b>" in result
    assert "éèç" in result
