"""
Fichier robots.txt dynamique pour l’optimisation SEO backend arts.
"""
def get_robots_txt():
    return """User-agent: *\nDisallow: /admin/\nAllow: /api/arts/\nSitemap: /sitemap.xml\n"""
