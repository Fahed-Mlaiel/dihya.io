"""
Template Métier : Blockchain
Backend Flask – Dihya Coding
Version finale conforme au cahier des charges
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

blockchain_bp = Blueprint('blockchain', __name__, url_prefix='/api')

# --- Modèles simulés (à remplacer par ORM/DB ou intégration web3) ---

contracts = []
wallets = []
transactions = []
tokens = []
notifications = []

# --- ROUTES SMART CONTRACTS ---

@blockchain_bp.route('/contracts', methods=['GET'])
@jwt_required()
def list_contracts():
    """Liste des smart contracts (Admin/User)"""
    return jsonify(contracts), 200

@blockchain_bp.route('/contracts', methods=['POST'])
@jwt_required()
def deploy_contract():
    """Déployer un smart contract (Admin)"""
    data = request.get_json()
    contract = {
        "id": len(contracts) + 1,
        "nom": data.get("nom"),
        "code_source": data.get("code_source"),
        "adresse": data.get("adresse", ""),
        "createur": get_jwt_identity(),
        "date": data.get("date"),
        "statut": "déployé",
        "logs": []
    }
    contracts.append(contract)
    return jsonify({"message": "Smart contract déployé", "contract": contract}), 201

# --- ROUTES PORTEFEUILLES ---

@blockchain_bp.route('/wallets', methods=['GET'])
@jwt_required()
def list_wallets():
    """Liste des portefeuilles (User)"""
    user_id = get_jwt_identity()
    user_wallets = [w for w in wallets if w["utilisateur"] == user_id]
    return jsonify(user_wallets), 200

@blockchain_bp.route('/wallets', methods=['POST'])
@jwt_required()
def create_wallet():
    """Créer un portefeuille (User)"""
    data = request.get_json()
    wallet = {
        "id": len(wallets) + 1,
        "utilisateur": get_jwt_identity(),
        "adresse": data.get("adresse"),
        "solde": data.get("solde", 0.0),
        "blockchain": data.get("blockchain", "Ethereum"),
        "historique": []
    }
    wallets.append(wallet)
    return jsonify({"message": "Portefeuille créé", "wallet": wallet}), 201

# --- ROUTES TRANSACTIONS ---

@blockchain_bp.route('/transactions', methods=['GET'])
@jwt_required()
def list_transactions():
    """Liste des transactions (User)"""
    user_id = get_jwt_identity()
    user_transactions = [t for t in transactions if t["portefeuille_utilisateur"] == user_id]
    return jsonify(user_transactions), 200

@blockchain_bp.route('/transactions', methods=['POST'])
@jwt_required()
def send_transaction():
    """Envoyer une transaction (User)"""
    data = request.get_json()
    transaction = {
        "id": len(transactions) + 1,
        "portefeuille_utilisateur": get_jwt_identity(),
        "type": data.get("type"),
        "montant": data.get("montant"),
        "date": data.get("date"),
        "statut": "envoyée",
        "hash": data.get("hash", "")
    }
    transactions.append(transaction)
    return jsonify({"message": "Transaction envoyée", "transaction": transaction}), 201

# --- ROUTES TOKENS & NFT ---

@blockchain_bp.route('/tokens', methods=['GET'])
@jwt_required()
def list_tokens():
    """Liste des tokens/NFT (User)"""
    return jsonify(tokens), 200

@blockchain_bp.route('/tokens', methods=['POST'])
@jwt_required()
def create_token():
    """Créer un token ou NFT (Admin)"""
    data = request.get_json()
    token = {
        "id": len(tokens) + 1,
        "nom": data.get("nom"),
        "type": data.get("type"),
        "proprietaire": data.get("proprietaire"),
        "metadonnees": data.get("metadonnees", {}),
        "statut": "émis"
    }
    tokens.append(token)
    return jsonify({"message": "Token/NFT créé", "token": token}), 201

# --- EXPORT TRANSACTIONS (CSV simulé) ---

@blockchain_bp.route('/export/transactions', methods=['GET'])
@jwt_required()
def export_transactions():
    """Exporter les transactions (CSV simulé)"""
    csv = "id,utilisateur,type,montant,date,statut,hash\n"
    for t in transactions:
        csv += f'{t["id"]},{t["portefeuille_utilisateur"]},{t["type"]},{t["montant"]},{t["date"]},{t["statut"]},{t["hash"]}\n'
    return (csv, 200, {'Content-Type': 'text/csv'})

# --- EXTENSIBILITÉ : Ajoutez ici vos routes métiers personnalisées ---

# --- FIN DU TEMPLATE BLOCKCHAIN ---

blueprint = blockchain_bp
