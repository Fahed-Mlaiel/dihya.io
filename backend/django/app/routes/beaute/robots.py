"""
Fichier robots.txt dynamique pour l’optimisation SEO backend beauté.
"""
def get_robots_txt():
    return """User-agent: *\nDisallow: /admin/\nAllow: /api/beaute/\nSitemap: /sitemap.xml\n"""
