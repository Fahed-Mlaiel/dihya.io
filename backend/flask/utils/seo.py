"""
SEO backend : robots, sitemap, logs structurés, accessibilité
"""

def set_robots_headers(response):
    """
    Ajoute l'en-tête X-Robots-Tag pour le SEO backend (conformité SEO, accessibilité, audit)
    :param response: objet Flask Response
    :return: objet Flask Response modifié
    """
    response.headers['X-Robots-Tag'] = 'all'
    return response

def set_sitemap_headers(response):
    """
    Ajoute l'en-tête X-Sitemap pour le SEO backend (sitemap dynamique, conformité SEO)
    :param response: objet Flask Response
    :return: objet Flask Response modifié
    """
    response.headers['X-Sitemap'] = '/sitemap.xml'
    return response
