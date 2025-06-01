"""
Template Métier : E-commerce
Backend Flask – Dihya Coding
Version finale conforme au cahier des charges
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

ecommerce_bp = Blueprint('ecommerce', __name__, url_prefix='/api')

# --- Modèles simulés (à remplacer par ORM/DB dans un vrai projet) ---

produits = []
categories = []
clients = []
commandes = []
promotions = []

# --- ROUTES PRODUITS ---

@ecommerce_bp.route('/produits', methods=['GET'])
def list_produits():
    """Liste des produits (Public)"""
    return jsonify(produits), 200

@ecommerce_bp.route('/produits', methods=['POST'])
@jwt_required()
def ajouter_produit():
    """Ajouter un produit (Admin)"""
    data = request.get_json()
    produit = {
        "id": len(produits) + 1,
        "nom": data.get("nom"),
        "description": data.get("description"),
        "prix": data.get("prix"),
        "stock": data.get("stock", 0),
        "images": data.get("images", []),
        "categorie": data.get("categorie"),
        "variantes": data.get("variantes", [])
    }
    produits.append(produit)
    return jsonify({"message": "Produit ajouté", "produit": produit}), 201

# --- ROUTES CATÉGORIES ---

@ecommerce_bp.route('/categories', methods=['GET'])
def list_categories():
    """Liste des catégories (Public)"""
    return jsonify(categories), 200

@ecommerce_bp.route('/categories', methods=['POST'])
@jwt_required()
def ajouter_categorie():
    """Ajouter une catégorie (Admin)"""
    data = request.get_json()
    categorie = {
        "id": len(categories) + 1,
        "nom": data.get("nom"),
        "parent": data.get("parent"),
        "description": data.get("description"),
        "seo": data.get("seo", {})
    }
    categories.append(categorie)
    return jsonify({"message": "Catégorie ajoutée", "categorie": categorie}), 201

# --- ROUTES CLIENTS ---

@ecommerce_bp.route('/clients', methods=['GET'])
@jwt_required()
def list_clients():
    """Liste des clients (Admin)"""
    return jsonify(clients), 200

@ecommerce_bp.route('/clients', methods=['POST'])
def creer_client():
    """Créer un client (Public)"""
    data = request.get_json()
    client = {
        "id": len(clients) + 1,
        "nom": data.get("nom"),
        "email": data.get("email"),
        "adresse": data.get("adresse"),
        "historique": [],
        "fidelite": data.get("fidelite", 0)
    }
    clients.append(client)
    return jsonify({"message": "Client créé", "client": client}), 201

# --- ROUTES COMMANDES ---

@ecommerce_bp.route('/commandes', methods=['GET'])
@jwt_required()
def list_commandes():
    """Liste des commandes (Admin/User)"""
    user_id = get_jwt_identity()
    if user_id:
        user_commandes = [c for c in commandes if c["client"] == user_id]
        return jsonify(user_commandes), 200
    return jsonify(commandes), 200

@ecommerce_bp.route('/commandes', methods=['POST'])
@jwt_required()
def passer_commande():
    """Passer une commande (User)"""
    data = request.get_json()
    commande = {
        "id": len(commandes) + 1,
        "client": get_jwt_identity(),
        "produits": data.get("produits", []),
        "montant": data.get("montant"),
        "statut": "en attente",
        "date": data.get("date"),
        "livraison": data.get("livraison", {}),
        "paiement": data.get("paiement", {}),
        "historique": []
    }
    commandes.append(commande)
    return jsonify({"message": "Commande passée", "commande": commande}), 201

# --- ROUTES PROMOTIONS ---

@ecommerce_bp.route('/promotions', methods=['GET'])
def list_promotions():
    """Liste des promotions (Public)"""
    return jsonify(promotions), 200

@ecommerce_bp.route('/promotions', methods=['POST'])
@jwt_required()
def ajouter_promotion():
    """Ajouter une promotion (Admin)"""
    data = request.get_json()
    promotion = {
        "id": len(promotions) + 1,
        "code": data.get("code"),
        "type": data.get("type"),
        "valeur": data.get("valeur"),
        "date_debut": data.get("date_debut"),
        "date_fin": data.get("date_fin"),
        "statut": data.get("statut", "actif")
    }
    promotions.append(promotion)
    return jsonify({"message": "Promotion ajoutée", "promotion": promotion}), 201

# --- EXPORT COMMANDES (CSV simulé) ---

@ecommerce_bp.route('/export/commandes', methods=['GET'])
@jwt_required()
def export_commandes():
    """Exporter les commandes (CSV simulé)"""
    csv = "id,client,produits,montant,statut,date\n"
    for c in commandes:
        csv += f'{c["id"]},{c["client"]},{c["produits"]},{c["montant"]},{c["statut"]},{c["date"]}\n'
    return (csv, 200, {'Content-Type': 'text/csv'})

# --- EXTENSIBILITÉ : Ajoutez ici vos routes métiers personnalisées ---

# --- FIN DU TEMPLATE E-COMMERCE ---

blueprint = ecommerce_bp
