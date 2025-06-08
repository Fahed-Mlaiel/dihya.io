# views.py - Exemple métier principal views
def render_view(view_name, context):
    return f"<div>{view_name}: {context}</div>"
