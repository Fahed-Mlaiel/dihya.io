"""
partials_views.py – Helpers et fragments réutilisables (partials) pour le module hotellerie
- Widgets, composants, conformité RGPD, accessibilité, audit, i18n
"""


def render_widget(name, data):
    """Rendu d’un widget réutilisable (ex: bouton, carte, badge)."""
    return (
        f"<div class='widget widget-{name}'>"
        f"{data}</div>"
    )
