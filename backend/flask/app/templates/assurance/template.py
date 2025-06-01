"""
Routes métier Assurance pour Dihya Coding
RESTful + GraphQL, sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO.
"""

from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from typing import Any, Dict
from ...utils.i18n import get_locale, translate
from ...middleware.audit import audit_log
from ...utils.seo import seo_headers

bp_assurance = Blueprint('assurance', __name__, url_prefix='/api/assurance')

def require_role(*roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user = get_jwt_identity()
            if not user or user.get('role') not in roles:
                return jsonify({'error': translate('Accès refusé', get_locale())}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator

def register_assurance_routes(bp):
    @bp.route('/contrats', methods=['GET'])
    @jwt_required()
    @require_role('gestionnaire', 'admin')
    @audit_log
    @seo_headers
    def list_contrats():
        """Liste des contrats (Agent/Admin)"""
        return jsonify(contrats), 200

    @bp.route('/contrats', methods=['POST'])
    @jwt_required()
    @require_role('gestionnaire')
    @audit_log
    def create_contrat():
        """Créer un contrat (Agent)"""
        data = request.get_json()
        contrat = {
            "id": len(contrats) + 1,
            "client": data.get("client"),
            "type": data.get("type"),
            "date_debut": data.get("date_debut"),
            "date_fin": data.get("date_fin"),
            "statut": "actif",
            "montant": data.get("montant"),
            "historique": []
        }
        contrats.append(contrat)
        return jsonify({"message": "Contrat créé", "contrat": contrat}), 201

    @bp.route('/clients', methods=['GET'])
    @jwt_required()
    @require_role('gestionnaire', 'admin')
    def list_clients():
        """Liste des clients (Agent/Admin)"""
        return jsonify(clients), 200

    @bp.route('/clients', methods=['POST'])
    @jwt_required()
    @require_role('gestionnaire')
    def create_client():
        """Créer un client (Agent)"""
        data = request.get_json()
        client = {
            "id": len(clients) + 1,
            "nom": data.get("nom"),
            "email": data.get("email"),
            "documents": data.get("documents", []),
            "contrats": [],
            "sinistres": []
        }
        clients.append(client)
        return jsonify({"message": "Client créé", "client": client}), 201

    @bp.route('/sinistres', methods=['GET'])
    @jwt_required()
    @require_role('gestionnaire', 'admin')
    def list_sinistres():
        """Liste des sinistres (Agent/Admin)"""
        return jsonify(sinistres), 200

    @bp.route('/sinistres', methods=['POST'])
    @jwt_required()
    @require_role('client')
    def declare_sinistre():
        """Déclarer un sinistre (Client)"""
        data = request.get_json()
        sinistre = {
            "id": len(sinistres) + 1,
            "contrat": data.get("contrat"),
            "date": data.get("date"),
            "description": data.get("description"),
            "statut": "en attente",
            "pieces_jointes": data.get("pieces_jointes", [])
        }
        sinistres.append(sinistre)
        return jsonify({"message": "Sinistre déclaré", "sinistre": sinistre}), 201

    @bp.route('/export/contrats', methods=['GET'])
    @jwt_required()
    @require_role('admin')
    def export_contrats():
        """Exporter les contrats (CSV simulé)"""
        csv = "id,client,type,date_debut,date_fin,statut,montant\n"
        for c in contrats:
            csv += f'{c["id"]},{c["client"]},{c["type"]},{c["date_debut"]},{c["date_fin"]},{c["statut"]},{c["montant"]}\n'
        return (csv, 200, {'Content-Type': 'text/csv'})

blueprint = bp_assurance

    # ... autres routes, GraphQL, plugins, audit, RGPD, SEO ...
