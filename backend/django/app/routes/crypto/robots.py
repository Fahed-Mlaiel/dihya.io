"""
Fichier robots.txt dynamique pour l’optimisation SEO backend crypto.
"""
def get_robots_txt():
    return """User-agent: *\nDisallow: /admin/\nAllow: /api/crypto/\nSitemap: /sitemap.xml\n"""
