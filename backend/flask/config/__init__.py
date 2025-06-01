"""
Configuration centralisée de l'application Flask pour Dihya Coding.

Inclut tous les paramètres critiques :
- Sécurité (CORS, JWT, OAuth, rate limiting, headers)
- Mailing (SMTP, API)
- Internationalisation (Babel, langues/dialectes)
- SEO (balises, sitemap, robots.txt)
- DevOps (monitoring, logs, backups)
- Plugins & templates métiers
- RGPD & conformité (logs, anonymisation)
- Extensibilité (plugins, IA fallback, marketplace)
- Branding (thème, assets)
"""

import os

class Config:
    """Configuration de base pour Dihya Coding (No-Code souverain)."""
    # Sécurité générale
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    DEBUG = os.environ.get("DEBUG", "False") == "True"
    TESTING = os.environ.get("TESTING", "False") == "True"

    # Mailing (SMTP ou API)
    MAIL_SERVER = os.environ.get("MAIL_SERVER", "smtp.example.com")
    MAIL_PORT = int(os.environ.get("MAIL_PORT", 587))
    MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS", "True") == "True"
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME", "")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD", "")
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_DEFAULT_SENDER", "noreply@dihya.coding")

    # JWT / Auth
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "jwt-secret-key")
    JWT_ACCESS_TOKEN_EXPIRES = int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRES", 3600))  # 1h
    JWT_REFRESH_TOKEN_EXPIRES = int(os.environ.get("JWT_REFRESH_TOKEN_EXPIRES", 86400))  # 24h
    OAUTH_CLIENT_ID = os.environ.get("OAUTH_CLIENT_ID", "")
    OAUTH_CLIENT_SECRET = os.environ.get("OAUTH_CLIENT_SECRET", "")

    # CORS & Sécurité API
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")
    RATE_LIMIT = os.environ.get("RATE_LIMIT", "100/minute")
    SECURE_HEADERS = {
        "Strict-Transport-Security": "max-age=63072000; includeSubDomains",
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "X-XSS-Protection": "1; mode=block"
    }

    # Internationalisation (i18n)
    LANGUAGES = ["fr", "en", "ar", "ber", "tzm"]
    BABEL_DEFAULT_LOCALE = os.environ.get("BABEL_DEFAULT_LOCALE", "fr")
    BABEL_DEFAULT_TIMEZONE = os.environ.get("BABEL_DEFAULT_TIMEZONE", "Europe/Paris")

    # SEO & Branding
    BASE_URL = os.environ.get("BASE_URL", "http://localhost:5000")
    SITE_NAME = os.environ.get("SITE_NAME", "Dihya Coding")
    SITE_DESCRIPTION = os.environ.get("SITE_DESCRIPTION", "Plateforme No-Code souveraine, multilingue, extensible.")
    SITE_THEME = os.environ.get("SITE_THEME", "amazigh-modern")

    # DevOps & Monitoring
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    ENABLE_MONITORING = os.environ.get("ENABLE_MONITORING", "True") == "True"
    BACKUP_ENABLED = os.environ.get("BACKUP_ENABLED", "True") == "True"

    # Plugins & Templates métiers
    ENABLE_MARKETPLACE = os.environ.get("ENABLE_MARKETPLACE", "True") == "True"
    PLUGINS_PATH = os.environ.get("PLUGINS_PATH", "./marketplace/plugins")
    TEMPLATES_PATH = os.environ.get("TEMPLATES_PATH", "./marketplace/templates")

    # RGPD & conformité
    ENABLE_RGPD = os.environ.get("ENABLE_RGPD", "True") == "True"
    AUDIT_LOG_PATH = os.environ.get("AUDIT_LOG_PATH", "./audit/logs")
    ANONYMIZE_LOGS = os.environ.get("ANONYMIZE_LOGS", "True") == "True"

    # IA & fallback souverain
    ENABLE_IA_FALLBACK = os.environ.get("ENABLE_IA_FALLBACK", "True") == "True"
    IA_FALLBACK_MODELS = os.environ.get("IA_FALLBACK_MODELS", "Mixtral,LLaMA,Mistral").split(",")

    # Cookies & sessions
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = "Lax"

    # Extensibilité
    ALLOWED_EXTENSIONS = ["json", "yaml", "yml", "js", "py"]

    # Pour d'autres environnements, héritez de Config (ex: ProductionConfig, TestingConfig)
    # et surchargez les paramètres sensibles.

# Exemple d’extension :
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    BASE_URL = os.environ.get("BASE_URL", "https://dihya.coding")
    LOG_LEVEL = "WARNING"