"""
Fichier robots.txt dynamique pour l’optimisation SEO backend agriculture.
"""
def get_robots_txt():
    return """User-agent: *\nDisallow: /admin/\nAllow: /api/agriculture/\nSitemap: /sitemap.xml\n"""
