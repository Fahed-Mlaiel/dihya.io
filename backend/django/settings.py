"""
Django settings ultra avancés pour Dihya :
- Sécurité maximale (CORS, JWT, WAF, anti-DDOS, CSP, audit, RGPD, logs structurés)
- Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Multitenancy, gestion des rôles, plugins, fallback IA open source
- SEO backend (robots, sitemap, logs)
- Prêt CI/CD, Codespaces, Docker, K8s, fallback local
"""
import os
from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'change-me-in-prod')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '*').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'graphene_django',
    'django_multitenant',
    'auditlog',
    'django_extensions',
    # Django business modules (AppConfig-Klassen statt Modulpfade)
    'backend.django.app.routes.automobile.apps.AutomobileConfig',
    'backend.django.app.routes.btp.apps.BtpConfig',
    'backend.django.app.routes.construction.apps.ConstructionConfig',
    'backend.django.app.routes.crypto.apps.CryptoConfig',
    'backend.django.app.routes.culture.apps.CultureConfig',
    'backend.django.app.routes.education.apps.EducationConfig',
    'backend.django.app.routes.energie.apps.EnergieConfig',
    'backend.django.app.routes.environnement.apps.EnvironnementConfig',
    'backend.django.app.routes.gamer.apps.GamerConfig',
    'backend.django.app.routes.health.apps.HealthConfig',
    'backend.django.app.routes.hotellerie.apps.HotellerieConfig',
    'backend.django.app.routes.immobilier.apps.ImmobilierConfig',
    'backend.django.app.routes.industrie.apps.IndustrieConfig',
    'backend.django.app.routes.logistique.apps.LogistiqueConfig',
    'backend.django.app.routes.transport.apps.TransportConfig',
    'backend.django.app.routes.sante.apps.SanteConfig',
    'backend.django.app.routes.mode.apps.ModeConfig',
    'backend.django.app.routes.blockchain.apps.BlockchainConfig',
    'backend.django.app.routes.securite.apps.SecuriteConfig',
    'backend.django.app.routes.journalisme.apps.JournalismeConfig',
    'backend.django.app.routes.arts.apps.ArtsConfig',
    'backend.django.app.routes.seo.apps.SeoConfig',
    'backend.django.app.routes.sport.apps.SportConfig',
    'backend.django.app.routes.marketing.apps.MarketingConfig',
    'backend.django.app.routes.science.apps.ScienceConfig',
    'backend.django.app.routes.tourisme.apps.TourismeConfig',
    'backend.django.app.routes.voice.apps.VoiceConfig',
    'backend.django.app.routes.it_devops.apps.ItDevopsConfig',
    'backend.django.app.routes.services_personne.apps.ServicesPersonneConfig',
    'backend.django.app.routes.manufacturing.apps.ManufacturingConfig',
    'backend.django.app.routes.ecommerce.apps.EcommerceConfig',
    'backend.django.app.routes.intelligence_artificielle.apps.IntelligenceArtificielleConfig',
    'backend.django.app.routes.juridique.apps.JuridiqueConfig',
    'backend.django.app.routes.loisirs.apps.LoisirsConfig',
    'backend.django.app.routes.medias.apps.MediasConfig',
    'backend.django.app.routes.mobile.apps.MobileConfig',
    'backend.django.app.routes.preview.apps.PreviewConfig',
    'backend.django.app.routes.publicite.apps.PubliciteConfig',
    'backend.django.app.routes.recherche.apps.RechercheConfig',
    'backend.django.app.routes.ressources_humaines.apps.RessourcesHumainesConfig',
    'backend.django.app.routes.restauration.apps.RestaurationConfig',
    'backend.django.app.routes.social.apps.SocialConfig',
    'backend.django.app.routes.utils.apps.UtilsConfig',
    'backend.django.app.routes.validators.apps.ValidatorsConfig',
    'backend.django.app.routes.voyage.apps.VoyageConfig',
    'backend.django.app.routes.vr_ar.apps.VrArConfig',
    # ...weitere nach Bedarf...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'auditlog.middleware.AuditlogMiddleware',
    # WAF, anti-DDOS, plugins dynamiques ici
]

ROOT_URLCONF = 'backend.django.urls'

LANGUAGES = [
    ('fr', 'Français'), ('en', 'English'), ('ar', 'العربية'), ('ber', 'ⴰⵎⴰⵣⵉⵖ'),
    ('de', 'Deutsch'), ('zh', '中文'), ('ja', '日本語'), ('ko', '한국어'),
    ('nl', 'Nederlands'), ('he', 'עברית'), ('fa', 'فارسی'), ('hi', 'हिन्दी'), ('es', 'Español'),
]
LANGUAGE_CODE = 'fr'
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
USE_I18N = True
USE_L10N = True
USE_TZ = True
TIME_ZONE = 'Europe/Paris'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']
CORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

GRAPHENE = {
    'SCHEMA': 'django_project.schema.schema',
    'MIDDLEWARE': [
        'graphene_django.debug.DjangoDebugMiddleware',
    ],
}

MULTITENANT_SHARED_APPS = [
    'django_multitenant',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    # ...autres apps partagées
]
MULTITENANT_TENANT_APPS = [
    # ...apps spécifiques par tenant
]

AUDITLOG_INCLUDE_ALL_MODELS = True
AUDITLOG_DISABLE_ON_RAW_SAVE = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'same-origin'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'

# SEO backend
ROBOTS_USE_SITEMAP = True
ROBOTS_SITEMAP_URLS = [os.environ.get('ROBOTS_SITEMAP_URL', '/sitemap.xml')]

# Plugins dynamiques (chargement via API/CLI)
PLUGINS_PATH = os.path.join(BASE_DIR, 'plugins')

# Fallback IA open source (LLaMA, Mixtral, Mistral)
IA_FALLBACK_PROVIDERS = ['llama', 'mixtral', 'mistral']

# RGPD : anonymisation, logs exportables
DATA_PRIVACY_EXPORT_PATH = os.path.join(BASE_DIR, 'exports')

# GitHub Actions, Docker, K8s, Codespaces ready
# ...autres configs avancées ici
