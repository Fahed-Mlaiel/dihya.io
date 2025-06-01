"""
Template Métier : Énergie
Backend Flask – Dihya Coding
Version finale conforme au cahier des charges
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

energie_bp = Blueprint('energie', __name__, url_prefix='/api')

# --- Modèles simulés (à remplacer par ORM/DB dans un vrai projet) ---

sites = []
consommations = []
equipements = []
maintenances = []
clients = []
factures = []
environnement = []

# --- ROUTES SITES DE PRODUCTION ---

@energie_bp.route('/sites', methods=['GET'])
@jwt_required()
def list_sites():
    """Liste des sites de production (Admin/User)"""
    return jsonify(sites), 200

@energie_bp.route('/sites', methods=['POST'])
@jwt_required()
def ajouter_site():
    """Ajouter un site (Admin)"""
    data = request.get_json()
    site = {
        "id": len(sites) + 1,
        "nom": data.get("nom"),
        "type": data.get("type"),
        "localisation": data.get("localisation"),
        "capacite": data.get("capacite"),
        "statut": data.get("statut", "actif")
    }
    sites.append(site)
    return jsonify({"message": "Site ajouté", "site": site}), 201

# --- ROUTES CONSOMMATION/PRODUCTION ---

@energie_bp.route('/consommation', methods=['GET'])
@jwt_required()
def list_consommation():
    """Liste des mesures de consommation/production (Admin/User)"""
    return jsonify(consommations), 200

@energie_bp.route('/consommation', methods=['POST'])
@jwt_required()
def ajouter_consommation():
    """Ajouter une mesure de consommation/production (Admin)"""
    data = request.get_json()
    mesure = {
        "id": len(consommations) + 1,
        "site": data.get("site"),
        "type": data.get("type"),
        "valeur": data.get("valeur"),
        "date": data.get("date"),
        "unite": data.get("unite")
    }
    consommations.append(mesure)
    return jsonify({"message": "Mesure ajoutée", "mesure": mesure}), 201

# --- ROUTES ÉQUIPEMENTS ---

@energie_bp.route('/equipements', methods=['GET'])
@jwt_required()
def list_equipements():
    """Liste des équipements (Admin/User)"""
    return jsonify(equipements), 200

@energie_bp.route('/equipements', methods=['POST'])
@jwt_required()
def ajouter_equipement():
    """Ajouter un équipement (Admin)"""
    data = request.get_json()
    equipement = {
        "id": len(equipements) + 1,
        "nom": data.get("nom"),
        "type": data.get("type"),
        "site": data.get("site"),
        "etat": data.get("etat", "actif"),
        "maintenance": data.get("maintenance", False)
    }
    equipements.append(equipement)
    return jsonify({"message": "Équipement ajouté", "equipement": equipement}), 201

# --- ROUTES MAINTENANCE ---

@energie_bp.route('/maintenance', methods=['GET'])
@jwt_required()
def list_maintenance():
    """Liste des interventions de maintenance (Admin/User)"""
    return jsonify(maintenances), 200

@energie_bp.route('/maintenance', methods=['POST'])
@jwt_required()
def ajouter_maintenance():
    """Planifier une intervention de maintenance (Admin)"""
    data = request.get_json()
    intervention = {
        "id": len(maintenances) + 1,
        "equipement": data.get("equipement"),
        "date": data.get("date"),
        "type": data.get("type"),
        "statut": data.get("statut", "planifiée")
    }
    maintenances.append(intervention)
    return jsonify({"message": "Intervention planifiée", "intervention": intervention}), 201

# --- ROUTES CLIENTS ---

@energie_bp.route('/clients', methods=['GET'])
@jwt_required()
def list_clients():
    """Liste des clients (Admin)"""
    return jsonify(clients), 200

@energie_bp.route('/clients', methods=['POST'])
@jwt_required()
def ajouter_client():
    """Ajouter un client (Admin)"""
    data = request.get_json()
    client = {
        "id": len(clients) + 1,
        "nom": data.get("nom"),
        "contact": data.get("contact"),
        "contrat": data.get("contrat"),
        "statut": data.get("statut", "actif")
    }
    clients.append(client)
    return jsonify({"message": "Client ajouté", "client": client}), 201

# --- ROUTES FACTURES ---

@energie_bp.route('/factures', methods=['GET'])
@jwt_required()
def list_factures():
    """Liste des factures (Admin/User)"""
    return jsonify(factures), 200

@energie_bp.route('/factures', methods=['POST'])
@jwt_required()
def ajouter_facture():
    """Générer une facture (Admin)"""
    data = request.get_json()
    facture = {
        "id": len(factures) + 1,
        "client": data.get("client"),
        "montant": data.get("montant"),
        "date": data.get("date"),
        "statut": data.get("statut", "en attente")
    }
    factures.append(facture)
    return jsonify({"message": "Facture générée", "facture": facture}), 201

# --- ROUTES ENVIRONNEMENT ---

@energie_bp.route('/environnement', methods=['GET'])
@jwt_required()
def list_environnement():
    """Indicateurs environnementaux (Admin/User)"""
    return jsonify(environnement), 200

# --- EXPORT CSV/PDF (exemple) ---

@energie_bp.route('/export/sites', methods=['GET'])
@jwt_required()
def export_sites():
    """Export des sites (Admin)"""
    # Ici, on simule un export CSV
    csv = "id,nom,type,localisation,capacite,statut\n" + "\n".join([
        f"{s['id']},{s['nom']},{s['type']},{s['localisation']},{s['capacite']},{s['statut']}" for s in sites
    ])
    return csv, 200, {'Content-Type': 'text/csv'}

# --- EXTENSIBILITÉ : Ajoutez ici vos routes métiers personnalisées ---

# --- FIN DU TEMPLATE ENERGIE ---

blueprint = energie_bp
