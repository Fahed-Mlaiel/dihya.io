"""
Fichier robots.txt dynamique pour l’optimisation SEO backend construction.
"""
def get_robots_txt():
    return """User-agent: *\nDisallow: /admin/\nAllow: /api/construction/\nSitemap: /sitemap.xml\n"""
