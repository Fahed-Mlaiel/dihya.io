"""
Sitemap dynamique pour l’optimisation SEO backend 3D, multilingue, multitenant, plugins, accessibilité, CI/CD-ready.
"""
def get_sitemap(lang: str = 'fr', tenant: str = 'default'):
    # SEO, multilingue, multitenant, plugins
    return [
        f'/api/3d/upload/?lang={lang}&tenant={tenant}',
        f'/api/3d/convert/?lang={lang}&tenant={tenant}',
        f'/api/3d/preview/?lang={lang}&tenant={tenant}',
        f'/api/3d/assets/?lang={lang}&tenant={tenant}',
    ]
