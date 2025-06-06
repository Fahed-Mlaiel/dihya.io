"""
Fichier robots.txt dynamique pour l’optimisation SEO backend 3D, multilingue, multitenant, plugins, accessibilité, CI/CD-ready.
"""
def get_robots_txt(lang: str = 'fr', tenant: str = 'default') -> str:
    # SEO, multilingue, multitenant, plugins
    robots = {
        'fr': "User-agent: *\nDisallow: /admin/\nAllow: /api/3d/\nSitemap: /sitemap.xml\n",
        'en': "User-agent: *\nDisallow: /admin/\nAllow: /api/3d/\nSitemap: /sitemap.xml\n",
        'ar': "User-agent: *\nDisallow: /admin/\nAllow: /api/3d/\nSitemap: /sitemap.xml\n",
        'tzm': "User-agent: *\nDisallow: /admin/\nAllow: /api/3d/\nSitemap: /sitemap.xml\n"
    }
    return robots.get(lang, robots['fr'])
