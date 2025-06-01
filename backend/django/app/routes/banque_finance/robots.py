"""
Fichier robots.txt dynamique pour l’optimisation SEO backend banque/finance.
"""
def get_robots_txt():
    return """User-agent: *\nDisallow: /admin/\nAllow: /api/banque_finance/\nSitemap: /sitemap.xml\n"""
