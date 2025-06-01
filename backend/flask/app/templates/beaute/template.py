"""
Routes métier Beauté pour Dihya Coding
RESTful + GraphQL, sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO.
"""

from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from typing import Any, Dict
from ...utils.i18n import get_locale, translate
from ...middleware.audit import audit_log
from ...utils.seo import seo_headers

bp_beaute = Blueprint('beaute', __name__, url_prefix='/api/beaute')

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

def register_beaute_routes(bp):
    @bp.route('/salons', methods=['GET'])
    @jwt_required()
    @require_role('admin', 'user')
    @audit_log
    @seo_headers
    def list_salons():
        """Liste des salons (Admin/User)"""
        return jsonify(salons), 200

    @bp.route('/salons', methods=['POST'])
    @jwt_required()
    @require_role('admin')
    @audit_log
    def create_salon():
        """Créer un salon (Admin)"""
        data = request.get_json()
        salon = {
            "id": len(salons) + 1,
            "nom": data.get("nom"),
            "adresse": data.get("adresse"),
            "equipe": data.get("equipe", []),
            "prestations": [],
            "planning": []
        }
        salons.append(salon)
        return jsonify({"message": "Salon créé", "salon": salon}), 201

    @bp.route('/prestations', methods=['GET'])
    def list_prestations():
        """Liste des prestations (Public)"""
        return jsonify(prestations), 200

    @bp.route('/prestations', methods=['POST'])
    @jwt_required()
    @require_role('admin')
    def add_prestation():
        """Ajouter une prestation (Admin)"""
        data = request.get_json()
        prestation = {
            "id": len(prestations) + 1,
            "nom": data.get("nom"),
            "tarif": data.get("tarif"),
            "duree": data.get("duree"),
            "description": data.get("description"),
            "disponibilite": data.get("disponibilite", True)
        }
        prestations.append(prestation)
        return jsonify({"message": "Prestation ajoutée", "prestation": prestation}), 201

    @bp.route('/rendezvous', methods=['GET'])
    @jwt_required()
    @require_role('salon', 'client')
    def list_rendezvous():
        """Liste des rendez-vous (Salon/Client)"""
        return jsonify(rendezvous), 200

    @bp.route('/rendezvous', methods=['POST'])
    @jwt_required()
    @require_role('client')
    def create_rendezvous():
        """Prendre rendez-vous (Client)"""
        data = request.get_json()
        rdv = {
            "id": len(rendezvous) + 1,
            "client": get_jwt_identity(),
            "salon": data.get("salon"),
            "prestation": data.get("prestation"),
            "date": data.get("date"),
            "statut": "confirmé"
        }
        rendezvous.append(rdv)
        return jsonify({"message": "Rendez-vous pris", "rendezvous": rdv}), 201

    @bp.route('/clients', methods=['GET'])
    @jwt_required()
    @require_role('admin', 'salon')
    def list_clients():
        """Liste des clients (Admin/Salon)"""
        return jsonify(clients), 200

    @bp.route('/clients', methods=['POST'])
    @jwt_required()
    @require_role('salon')
    def create_client():
        """Créer un client (Salon)"""
        data = request.get_json()
        client = {
            "id": len(clients) + 1,
            "nom": data.get("nom"),
            "email": data.get("email"),
            "historique": [],
            "fidelite": data.get("fidelite", 0)
        }
        clients.append(client)
        return jsonify({"message": "Client créé", "client": client}), 201

    @bp.route('/export/rendezvous', methods=['GET'])
    @jwt_required()
    @require_role('admin')
    def export_rendezvous():
        """Exporter les rendez-vous (CSV simulé)"""
        csv = "id,client,salon,prestation,date,statut\n"
        for r in rendezvous:
            csv += f'{r["id"]},{r["client"]},{r["salon"]},{r["prestation"]},{r["date"]},{r["statut"]}\n'
        return (csv, 200, {'Content-Type': 'text/csv'})

blueprint = bp_beaute

    # ... autres routes, GraphQL, plugins, audit, RGPD, SEO ...
