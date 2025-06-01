"""
SEO backend : robots, sitemap, logs structurés, accessibilité
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

# SEO avancé : génération de meta tags, robots.txt, sitemap.xml, X-Robots-Tag, X-Sitemap, accessibilité, audit, RGPD, multitenancy

def generate_meta_tags(title, description, keywords=None, canonical_url=None, og_image=None):
    tags = [
        f'<title>{title}</title>',
        f'<meta name="description" content="{description}">',
    ]
    if keywords:
        tags.append(f'<meta name="keywords" content="{keywords}">')
    if canonical_url:
        tags.append(f'<link rel="canonical" href="{canonical_url}">')
    if og_image:
        tags.append(f'<meta property="og:image" content="{og_image}">')
    return '\n'.join(tags)

def generate_robots_txt(disallow_api=True):
    lines = ["User-agent: *"]
    if disallow_api:
        lines.append("Disallow: /api/")
    return '\n'.join(lines)

def generate_sitemap(urls, base_url):
    from xml.etree.ElementTree import Element, SubElement, tostring
    urlset = Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for url in urls:
        url_el = SubElement(urlset, 'url')
        loc = SubElement(url_el, 'loc')
        loc.text = f"{base_url}{url}"
    return tostring(urlset, encoding='utf-8', method='xml').decode('utf-8')

def seo_headers(f):
    """
    Flask-Response-Dekorator für SEO-Header (kompatibel mit @seo_headers auf Routen).
    """
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        response = f(*args, **kwargs)
        # Falls die Route ein dict oder keine Response zurückgibt, nicht modifizieren
        try:
            response.headers['X-Robots-Tag'] = 'all'
            response.headers['X-Sitemap'] = '/sitemap.xml'
        except Exception:
            pass
        return response
    return decorated_function
