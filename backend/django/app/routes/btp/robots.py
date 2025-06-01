"""
Fichier robots.txt dynamique pour l’optimisation SEO backend BTP.
"""
def get_robots_txt():
    return """User-agent: *\nDisallow: /admin/\nAllow: /api/btp/\nSitemap: /sitemap.xml\n"""
