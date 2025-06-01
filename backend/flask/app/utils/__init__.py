"""
Initialisation des utilitaires pour l'application Dihya Coding.
Ce module permet d'organiser et d'importer les utilitaires communs :
- Sécurité (hash, JWT, rate limiting)
- Validation des données
- Mailing
- Internationalisation (i18n)
- SEO

À compléter si de nouveaux utilitaires sont ajoutés.
"""

from .securite import hash_password, verify_password, require_json, set_default_security_headers, rate_limited
from .securite import sanitize_input
from .validators import validate_email, validate_registration, validate_login, validate_user_update
from .mailing import send_email
from .i18n import get_locale, translate
from .seo import set_robots_headers, set_sitemap_headers, generate_meta_tags, generate_robots_txt, generate_sitemap

# Kompatibilität: Alias für security
from .securite import *

# Ajouter ici d'autres imports utilitaires si besoin.
