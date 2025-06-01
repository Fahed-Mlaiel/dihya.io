"""
Template Métier : Construction
Backend Flask – Dihya Coding
Version finale conforme au cahier des charges
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

construction_bp = Blueprint('construction', __name__, url_prefix='/api')

# --- Modèles simulés (à remplacer par ORM/DB dans un vrai projet) ---

projets = []
chantiers = []
equipes = []
materiels = []
fournisseurs = []
finances = []

# --- ROUTES PROJETS ---

@construction_bp.route('/projets', methods=['GET'])
@jwt_required()
def list_projets():
    """Liste des projets (Admin/User)"""
    return jsonify(projets), 200

@construction_bp.route('/projets', methods=['POST'])
@jwt_required()
def creer_projet():
    """Créer un projet (Admin)"""
    data = request.get_json()
    projet = {
        "id": len(projets) + 1,
        "nom": data.get("nom"),
        "localisation": data.get("localisation"),
        "date_debut": data.get("date_debut"),
        "date_fin": data.get("date_fin"),
        "statut": data.get("statut", "en cours"),
        "equipes": data.get("equipes", []),
        "budget": data.get("budget"),
        "documents": data.get("documents", [])
    }
    projets.append(projet)
    return jsonify({"message": "Projet créé", "projet": projet}), 201

# --- ROUTES CHANTIERS ---

@construction_bp.route('/chantiers', methods=['GET'])
@jwt_required()
def list_chantiers():
    """Liste des chantiers (Admin/User)"""
    return jsonify(chantiers), 200

@construction_bp.route('/chantiers', methods=['POST'])
@jwt_required()
def creer_chantier():
    """Créer un chantier (Admin)"""
    data = request.get_json()
    chantier = {
        "id": len(chantiers) + 1,
        "projet": data.get("projet"),
        "localisation": data.get("localisation"),
        "date_debut": data.get("date_debut"),
        "date_fin": data.get("date_fin"),
        "statut": data.get("statut", "en cours"),
        "equipes": data.get("equipes", []),
        "budget": data.get("budget"),
        "documents": data.get("documents", [])
    }
    chantiers.append(chantier)
    return jsonify({"message": "Chantier créé", "chantier": chantier}), 201

# --- ROUTES ÉQUIPES ---

@construction_bp.route('/equipes', methods=['GET'])
@jwt_required()
def list_equipes():
    """Liste des équipes (Admin/User)"""
    return jsonify(equipes), 200

@construction_bp.route('/equipes', methods=['POST'])
@jwt_required()
def creer_equipe():
    """Créer une équipe (Admin)"""
    data = request.get_json()
    equipe = {
        "id": len(equipes) + 1,
        "nom": data.get("nom"),
        "membres": data.get("membres", []),
        "chef": data.get("chef"),
        "chantiers": data.get("chantiers", [])
    }
    equipes.append(equipe)
    return jsonify({"message": "Équipe créée", "equipe": equipe}), 201

# --- ROUTES MATÉRIELS ---

@construction_bp.route('/materiels', methods=['GET'])
@jwt_required()
def list_materiels():
    """Liste du matériel (Admin/User)"""
    return jsonify(materiels), 200

@construction_bp.route('/materiels', methods=['POST'])
@jwt_required()
def ajouter_materiel():
    """Ajouter du matériel (Admin)"""
    data = request.get_json()
    materiel = {
        "id": len(materiels) + 1,
        "nom": data.get("nom"),
        "type": data.get("type"),
        "etat": data.get("etat", "disponible"),
        "disponibilite": data.get("disponibilite", True),
        "historique": data.get("historique", [])
    }
    materiels.append(materiel)
    return jsonify({"message": "Matériel ajouté", "materiel": materiel}), 201

# --- ROUTES FOURNISSEURS ---

@construction_bp.route('/fournisseurs', methods=['GET'])
@jwt_required()
def list_fournisseurs():
    """Liste des fournisseurs (Admin)"""
    return jsonify(fournisseurs), 200

@construction_bp.route('/fournisseurs', methods=['POST'])
@jwt_required()
def ajouter_fournisseur():
    """Ajouter un fournisseur (Admin)"""
    data = request.get_json()
    fournisseur = {
        "id": len(fournisseurs) + 1,
        "nom": data.get("nom"),
        "contact": data.get("contact"),
        "specialite": data.get("specialite"),
        "contrats": data.get("contrats", [])
    }
    fournisseurs.append(fournisseur)
    return jsonify({"message": "Fournisseur ajouté", "fournisseur": fournisseur}), 201

# --- ROUTES FINANCES ---

@construction_bp.route('/finances', methods=['GET'])
@jwt_required()
def list_finances():
    """Suivi financier (Admin)"""
    return jsonify(finances), 200

@construction_bp.route('/finances', methods=['POST'])
@jwt_required()
def ajouter_finance():
    """Ajouter une ligne financière (Admin)"""
    data = request.get_json()
    finance = {
        "id": len(finances) + 1,
        "projet": data.get("projet"),
        "budget": data.get("budget"),
        "depenses": data.get("depenses", []),
        "factures": data.get("factures", []),
        "statut": data.get("statut", "en cours")
    }
    finances.append(finance)
    return jsonify({"message": "Ligne financière ajoutée", "finance": finance}), 201

# --- EXPORT PROJETS (CSV simulé) ---

@construction_bp.route('/export/projets', methods=['GET'])
@jwt_required()
def export_projets():
    """Exporter les projets (CSV simulé)"""
    csv = "id,nom,localisation,date_debut,date_fin,statut,budget\n"
    for p in projets:
        csv += f'{p["id"]},{p["nom"]},{p["localisation"]},{p["date_debut"]},{p["date_fin"]},{p["statut"]},{p["budget"]}\n'
    return (csv, 200, {'Content-Type': 'text/csv'})

# --- EXTENSIBILITÉ : Ajoutez ici vos routes métiers personnalisées ---

# --- FIN DU TEMPLATE CONSTRUCTION ---

blueprint = construction_bp
