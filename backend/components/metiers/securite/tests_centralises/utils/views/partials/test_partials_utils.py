# Test avancé pour partials_utils.py du module utils/views/partials
# from components.metiers.securite.utils.views.partials.partials_utils import ...
from backend.components.metiers.securite.utils.views.partials import partials_views


def test_utils_views_partials():
    # Ajouter des assertions avancées selon la logique métier
    assert True


def test_render_widget_nominal():
    html = partials_views.render_widget("badge", "OK")
    assert "widget-badge" in html
    assert ">OK<" in html
    assert html.startswith("<div") and html.endswith("</div>")


def test_render_widget_edge_cases():
    html = partials_views.render_widget("", "vide")
    assert "widget-" in html
    html2 = partials_views.render_widget("special-ç", "<b>bold</b>")
    assert "special-ç" in html2
    assert "<b>bold</b>" in html2
