"""
Template Métier : Culture
Backend Flask – Dihya Coding
Version finale conforme au cahier des charges
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

culture_bp = Blueprint('culture', __name__, url_prefix='/api')

# --- Modèles simulés (à remplacer par ORM/DB dans un vrai projet) ---

evenements = []
artistes = []
lieux = []
oeuvres = []
billets = []

# --- ROUTES EVENEMENTS ---

@culture_bp.route('/evenements', methods=['GET'])
def list_evenements():
    """Liste des événements (Public)"""
    return jsonify(evenements), 200

@culture_bp.route('/evenements', methods=['POST'])
@jwt_required()
def creer_evenement():
    """Créer un événement (Admin)"""
    data = request.get_json()
    evenement = {
        "id": len(evenements) + 1,
        "nom": data.get("nom"),
        "date": data.get("date"),
        "lieu": data.get("lieu"),
        "artistes": data.get("artistes", []),
        "description": data.get("description"),
        "billets": []
    }
    evenements.append(evenement)
    return jsonify({"message": "Événement créé", "evenement": evenement}), 201

# --- ROUTES ARTISTES ---

@culture_bp.route('/artistes', methods=['GET'])
def list_artistes():
    """Liste des artistes (Public)"""
    return jsonify(artistes), 200

@culture_bp.route('/artistes', methods=['POST'])
@jwt_required()
def ajouter_artiste():
    """Ajouter un artiste (Admin)"""
    data = request.get_json()
    artiste = {
        "id": len(artistes) + 1,
        "nom": data.get("nom"),
        "bio": data.get("bio"),
        "oeuvres": data.get("oeuvres", []),
        "photo": data.get("photo", "")
    }
    artistes.append(artiste)
    return jsonify({"message": "Artiste ajouté", "artiste": artiste}), 201

# --- ROUTES LIEUX ---

@culture_bp.route('/lieux', methods=['GET'])
def list_lieux():
    """Liste des lieux (Public)"""
    return jsonify(lieux), 200

@culture_bp.route('/lieux', methods=['POST'])
@jwt_required()
def ajouter_lieu():
    """Ajouter un lieu (Admin)"""
    data = request.get_json()
    lieu = {
        "id": len(lieux) + 1,
        "nom": data.get("nom"),
        "adresse": data.get("adresse"),
        "capacite": data.get("capacite"),
        "type": data.get("type")
    }
    lieux.append(lieu)
    return jsonify({"message": "Lieu ajouté", "lieu": lieu}), 201

# --- ROUTES OEUVRES ---

@culture_bp.route('/oeuvres', methods=['GET'])
def list_oeuvres():
    """Liste des œuvres (Public)"""
    return jsonify(oeuvres), 200

@culture_bp.route('/oeuvres', methods=['POST'])
@jwt_required()
def ajouter_oeuvre():
    """Ajouter une œuvre (Admin)"""
    data = request.get_json()
    oeuvre = {
        "id": len(oeuvres) + 1,
        "titre": data.get("titre"),
        "artiste": data.get("artiste"),
        "type": data.get("type"),
        "description": data.get("description"),
        "medias": data.get("medias", [])
    }
    oeuvres.append(oeuvre)
    return jsonify({"message": "Œuvre ajoutée", "oeuvre": oeuvre}), 201

# --- ROUTES BILLETS ---

@culture_bp.route('/billets', methods=['GET'])
@jwt_required()
def list_billets():
    """Liste des billets (User/Admin)"""
    user_id = get_jwt_identity()
    user_billets = [b for b in billets if b["utilisateur"] == user_id]
    return jsonify(user_billets), 200

@culture_bp.route('/billets', methods=['POST'])
@jwt_required()
def reserver_billet():
    """Réserver/acheter un billet (User)"""
    data = request.get_json()
    billet = {
        "id": len(billets) + 1,
        "evenement": data.get("evenement"),
        "utilisateur": get_jwt_identity(),
        "statut": "réservé",
        "qr_code": "QR-" + str(len(billets) + 1)
    }
    billets.append(billet)
    return jsonify({"message": "Billet réservé", "billet": billet}), 201

# --- EXPORT EVENEMENTS (CSV simulé) ---

@culture_bp.route('/export/evenements', methods=['GET'])
@jwt_required()
def export_evenements():
    """Exporter les événements (CSV simulé)"""
    csv = "id,nom,date,lieu,description\n"
    for e in evenements:
        csv += f'{e["id"]},{e["nom"]},{e["date"]},{e["lieu"]},{e["description"]}\n'
    return (csv, 200, {'Content-Type': 'text/csv'})

# --- EXTENSIBILITÉ : Ajoutez ici vos routes métiers personnalisées ---

blueprint = culture_bp

# --- FIN DU TEMPLATE CULTURE ---
