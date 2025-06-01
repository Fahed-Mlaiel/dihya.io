"""
Initialisation des blueprints de routes pour l'application Dihya Coding.
Chaque module de routes (main, auth, user, etc.) est importé ici pour
être enregistré dans l'application principale.
"""

from flask import Blueprint

# Blueprint principal (routes publiques, healthcheck, accueil, info, echo, SEO)
main = Blueprint('main', __name__)

# Blueprint Auth (authentification, inscription, refresh, logout)
auth = Blueprint('auth', __name__)

# Blueprint User (gestion des utilisateurs, rôles, profil, CRUD)
user = Blueprint('user', __name__)

from .generate import generate_bp
from .ai import ai_blueprint

__all__ = [
    "main",
    "auth",
    "user",
    "generate_bp",
    "ai_blueprint"
]

# À compléter si de nouveaux modules de routes sont ajoutés (ex: admin, plugins, etc.)

# Les fichiers main.py, auth.py, user.py doivent définir les routes
# et attacher les fonctions à ces blueprints respectifs.
# Chaque blueprint doit être importé dans app/__init__.py pour l'enregistrement.

# Stubs für Kompatibilität mit Tests (Blueprints aus Templates)
try:
    from ..templates.administration_publique import blueprint as administration_publique_blueprint
except ImportError:
    administration_publique_blueprint = None
try:
    from ..templates.agriculture import blueprint as agriculture_blueprint
except ImportError:
    agriculture_blueprint = None
try:
    from ..templates.assurance import blueprint as assurance_blueprint
except ImportError:
    assurance_blueprint = None

__all__ += [
    "administration_publique_blueprint",
    "agriculture_blueprint",
    "assurance_blueprint"
]
