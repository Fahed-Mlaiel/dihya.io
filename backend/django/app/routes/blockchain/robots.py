"""
Fichier robots.txt dynamique pour l’optimisation SEO backend blockchain.
"""
def get_robots_txt():
    return """User-agent: *\nDisallow: /admin/\nAllow: /api/blockchain/\nSitemap: /sitemap.xml\n"""
