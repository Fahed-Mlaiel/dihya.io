"""
Routes métier Banque & Finance pour Dihya Coding
RESTful + GraphQL, sécurité, i18n, multitenancy, plugins, audit, RGPD, SEO.
"""

from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from typing import Any, Dict
from ...utils.i18n import get_locale, translate
from ...middleware.audit import audit_log
from ...utils.seo import seo_headers

bp_banque_finance = Blueprint('banque_finance', __name__, url_prefix='/api/banque_finance')

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

def register_banque_finance_routes(bp):
    @bp.route('/comptes', methods=['GET'])
    @jwt_required()
    @require_role('conseiller', 'admin')
    @audit_log
    @seo_headers
    def list_comptes():
        """Liste des comptes (Conseiller/Admin)"""
        return jsonify(comptes), 200

    @bp.route('/comptes', methods=['POST'])
    @jwt_required()
    @require_role('conseiller')
    @audit_log
    def create_compte():
        """Créer un compte bancaire (Conseiller)"""
        data = request.get_json()
        compte = {
            "id": len(comptes) + 1,
            "client": data.get("client"),
            "type": data.get("type"),
            "solde": data.get("solde", 0.0),
            "historique": [],
            "statut": "actif"
        }
        comptes.append(compte)
        return jsonify({"message": "Compte créé", "compte": compte}), 201

    @bp.route('/clients', methods=['GET'])
    @jwt_required()
    @require_role('conseiller', 'admin')
    def list_clients():
        """Liste des clients (Conseiller/Admin)"""
        return jsonify(clients), 200

    @bp.route('/clients', methods=['POST'])
    @jwt_required()
    @require_role('conseiller')
    def create_client():
        """Créer un client (Conseiller)"""
        data = request.get_json()
        client = {
            "id": len(clients) + 1,
            "nom": data.get("nom"),
            "email": data.get("email"),
            "documents": data.get("documents", []),
            "comptes": [],
            "scoring": data.get("scoring", None)
        }
        clients.append(client)
        return jsonify({"message": "Client créé", "client": client}), 201

    @bp.route('/operations', methods=['GET'])
    @jwt_required()
    @require_role('client', 'admin')
    def list_operations():
        """Liste des opérations (Client/Admin)"""
        return jsonify(operations), 200

    @bp.route('/operations', methods=['POST'])
    @jwt_required()
    @require_role('client')
    def create_operation():
        """Effectuer une opération bancaire (Client)"""
        data = request.get_json()
        operation = {
            "id": len(operations) + 1,
            "compte": data.get("compte"),
            "type": data.get("type"),
            "montant": data.get("montant"),
            "date": data.get("date"),
            "statut": "effectuée"
        }
        operations.append(operation)
        # Logique de débit/crédit simulée
        for c in comptes:
            if c["id"] == data.get("compte"):
                if data.get("type") == "debit":
                    c["solde"] -= data.get("montant")
                elif data.get("type") == "credit":
                    c["solde"] += data.get("montant")
                c["historique"].append(operation)
        return jsonify({"message": "Opération effectuée", "operation": operation}), 201

    @bp.route('/credits', methods=['GET'])
    @jwt_required()
    @require_role('client', 'admin')
    def list_credits():
        """Liste des crédits (Client/Admin)"""
        return jsonify(credits), 200

    @bp.route('/credits', methods=['POST'])
    @jwt_required()
    @require_role('client')
    def demande_credit():
        """Demander un crédit (Client)"""
        data = request.get_json()
        credit = {
            "id": len(credits) + 1,
            "client": get_jwt_identity(),
            "montant": data.get("montant"),
            "taux": data.get("taux"),
            "duree": data.get("duree"),
            "statut": "en attente",
            "echeances": []
        }
        credits.append(credit)
        return jsonify({"message": "Crédit demandé", "credit": credit}), 201

    @bp.route('/export/comptes', methods=['GET'])
    @jwt_required()
    @require_role('admin')
    def export_comptes():
        """Exporter les comptes (CSV simulé)"""
        csv = "id,client,type,solde,statut\n"
        for c in comptes:
            csv += f'{c["id"]},{c["client"]},{c["type"]},{c["solde"]},{c["statut"]}\n'
        return (csv, 200, {'Content-Type': 'text/csv'})

blueprint = bp_banque_finance

    # ... autres routes, GraphQL, plugins, audit, RGPD, SEO ...
