"""
Fichier robots.txt dynamique pour l’optimisation SEO backend VR/AR.
"""
def get_robots_txt():
    return """User-agent: *\nDisallow: /admin/\nAllow: /api/vr_ar/\nSitemap: /sitemap.xml\n"""
