"""
Dihya – Flask Backend Config (Python)
Multilingue, sécurisé, modulaire, souverain, documenté
Compatible multi-environnements, CI/CD, tests, souveraineté
"""
import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    ENV = os.getenv('FLASK_ENV', 'development')
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-me')
    ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*').split(',')
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', './logs/app.log')
    LANGUAGES = ['fr', 'en', 'ar', 'tzr']
    DEFAULT_LANGUAGE = 'fr'
    CSRF_ENABLED = True
    XSS_PROTECTION = True
    CONTENT_SECURITY_POLICY = True
    TESTING = os.getenv('TESTS_ENABLE', 'false').lower() == 'true'
