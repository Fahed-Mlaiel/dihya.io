"""
templates_views.py – Helpers et templates (HTML, Jinja, etc.) pour le module threed
- Rendu, conformité RGPD, accessibilité, audit, i18n
"""
def render_template(name, context):
    """Rendu d’un template HTML simple (ex: page, composant, email)."""
    return f"<div class='template template-{name}'>{context}</div>"
