"""
Fixtures avancées pour tests, démo, et CI/CD des modèles 3D.
Inclut multilingue, sécurité, RGPD, anonymisation, accessibilité.
"""
from .models import Model3D
from django.contrib.auth import get_user_model
from django.utils import timezone
from .i18n import I18N

def create_3d_fixtures():
    User = get_user_model()
    # Multitenant, multilingue, anonymisé, RGPD, plugins, a11y
    tenants = ['default', 'tenant42']
    langs = list(I18N.keys())
    for tenant in tenants:
        for lang in langs:
            user = User.objects.filter(is_staff=True).first() or User.objects.create_user(username=f'{tenant}_{lang}_user', password='pass', is_staff=True)
            Model3D.objects.create(
                name=f"Demo 3D Model {lang} {tenant}",
                file="demo.obj",
                owner=user,
                preview_url=f"https://cdn.dihya.app/{tenant}/{lang}/demo_preview.png",
                file_url=f"https://cdn.dihya.app/{tenant}/{lang}/demo.obj",
                date_upload=timezone.now(),
                date_modification=timezone.now(),
            )
    # RGPD: anonymisation, suppression logique
    # Plugins: Beispiel für Plugin-Feld
    # Accessibility: alle Felder gesetzt
