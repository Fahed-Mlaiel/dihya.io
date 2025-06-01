"""
utils.py - Fonctions utilitaires avancées pour routes Flask Dihya
Sécurité, i18n, audit, plugins, fallback IA, RGPD, anonymisation, export, logging structuré
"""
from typing import Any, Dict
from flask import request
from flask_babel import gettext as _

def validate_project_ia(data: Dict, locale: str) -> (bool, Dict):
    """Validation stricte d’un projet IA (exemple)."""
    errors = {}
    if not data.get('name'):
        errors['name'] = _('Nom requis')
    if not data.get('description'):
        errors['description'] = _('Description requise')
    return (len(errors) == 0, errors)

def audit_log(user: str, action: str, tenant: str, locale: str, details: Any = None) -> None:
    """Audit log structuré (RGPD, exportable, anonymisable)."""
    # Exemple : log dans un fichier ou base RGPD-compliant
    pass

def get_tenant(user: str) -> str:
    """Récupérer le tenant de l’utilisateur (multi-tenant)."""
    return user.split('@')[-1] if '@' in user else 'default'

def get_locale(req: Any) -> str:
    """Détecter la langue de la requête (i18n dynamique)."""
    return req.headers.get('Accept-Language', 'fr')

def get_plugins(tenant: str) -> Dict:
    """Charger dynamiquement les plugins actifs pour un tenant."""
    return {'tools': ['diagnostic', 'export'], 'ai': ['llama', 'mixtral', 'mistral']}

def fallback_ia(tenant: str, plugins: Dict, locale: str, data: Any = None) -> Any:
    """Fallback IA open source (LLaMA, Mixtral, Mistral, mock)."""
    # Exemple : renvoyer un projet IA mocké
    return [{'id': 1, 'name': _('Projet IA démo'), 'locale': locale, 'tenant': tenant}]

def anonymize_data(data: Any, user: str) -> Any:
    """Anonymisation RGPD des données (exemple)."""
    # Exemple : supprimer les emails, IP, etc.
    return data

def export_projects(projects: Any, format: str = 'json') -> Any:
    """Export des projets (CSV, JSON, etc.)."""
    # Exemple : export JSON
    from flask import Response
    import json
    return Response(json.dumps(projects), mimetype='application/json')

def export_diagnostics(diagnostics: Any, format: str = 'json') -> Any:
    """Export des diagnostics (CSV, JSON, etc.)."""
    from flask import Response
    import json
    return Response(json.dumps(diagnostics), mimetype='application/json')

def get_i18n_headers(lang="fr"):
    """Gibt Header für die gewünschte Sprache zurück."""
    return {"Accept-Language": lang}

def get_admin_token():
    """Gibt einen Dummy-Admin-Token zurück (für Tests)."""
    return "dummy-admin-token"

def get_tenant_headers(tenant="default"):
    """Gibt Header für den gewünschten Tenant zurück."""
    return {"X-Tenant": tenant}

def validate_input(data, schema):
    """Valide les données selon un schéma simple."""
    for key, typ in schema.items():
        if key not in data or not isinstance(data[key], typ):
            raise ValueError(f"Champ {key} invalide")
    return True

def plugin_manager(name, params):
    """Mock plugin manager."""
    return {'status': 'success', 'plugin': name, 'params': params}

def rgpd_anonymize(data):
    """Mock RGPD anonymizer."""
    return {k: f'anonymized_{k}' for k in data}
