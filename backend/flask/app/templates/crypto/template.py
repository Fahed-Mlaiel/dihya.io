"""
Template Métier : Crypto
Backend Flask – Dihya Coding
Version finale conforme au cahier des charges
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

crypto_bp = Blueprint('crypto', __name__, url_prefix='/api')

# --- Modèles simulés (à remplacer par ORM/DB ou intégration web3/crypto API) ---

wallets = []
transactions = []
tokens = []
alerts = []

# --- ROUTES PORTEFEUILLES ---

@crypto_bp.route('/wallets', methods=['GET'])
@jwt_required()
def list_wallets():
    """Liste des portefeuilles (User)"""
    user_id = get_jwt_identity()
    user_wallets = [w for w in wallets if w["utilisateur"] == user_id]
    return jsonify(user_wallets), 200

@crypto_bp.route('/wallets', methods=['POST'])
@jwt_required()
def create_wallet():
    """Créer un portefeuille (User)"""
    data = request.get_json()
    wallet = {
        "id": len(wallets) + 1,
        "utilisateur": get_jwt_identity(),
        "adresse": data.get("adresse"),
        "solde": data.get("solde", 0.0),
        "blockchain": data.get("blockchain", "Bitcoin"),
        "historique": []
    }
    wallets.append(wallet)
    return jsonify({"message": "Portefeuille créé", "wallet": wallet}), 201

# --- ROUTES TRANSACTIONS ---

@crypto_bp.route('/transactions', methods=['GET'])
@jwt_required()
def list_transactions():
    """Liste des transactions (User)"""
    user_id = get_jwt_identity()
    user_transactions = [t for t in transactions if t["wallet_user"] == user_id]
    return jsonify(user_transactions), 200

@crypto_bp.route('/transactions', methods=['POST'])
@jwt_required()
def send_transaction():
    """Envoyer une transaction (User)"""
    data = request.get_json()
    transaction = {
        "id": len(transactions) + 1,
        "wallet_user": get_jwt_identity(),
        "type": data.get("type"),
        "montant": data.get("montant"),
        "date": data.get("date"),
        "statut": "envoyée",
        "hash": data.get("hash", ""),
        "frais": data.get("frais", 0.0)
    }
    transactions.append(transaction)
    return jsonify({"message": "Transaction envoyée", "transaction": transaction}), 201

# --- ROUTES TOKENS & NFT ---

@crypto_bp.route('/tokens', methods=['GET'])
@jwt_required()
def list_tokens():
    """Liste des tokens/NFT (User)"""
    return jsonify(tokens), 200

@crypto_bp.route('/tokens', methods=['POST'])
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

# --- ROUTES SUIVI DE MARCHÉ (SIMULÉ) ---

@crypto_bp.route('/market', methods=['GET'])
def get_market():
    """Prix du marché en temps réel (Public, simulé)"""
    # Exemple statique, à remplacer par appel API réelle
    market = [
        {"symbol": "BTC", "price": 65000, "change_24h": 2.1},
        {"symbol": "ETH", "price": 3200, "change_24h": -1.2},
        {"symbol": "SOL", "price": 150, "change_24h": 0.5}
    ]
    return jsonify(market), 200

# --- EXPORT TRANSACTIONS (CSV simulé) ---

@crypto_bp.route('/export/transactions', methods=['GET'])
@jwt_required()
def export_transactions():
    """Exporter les transactions (CSV simulé)"""
    csv = "id,utilisateur,type,montant,date,statut,hash,frais\n"
    for t in transactions:
        csv += f'{t["id"]},{t["wallet_user"]},{t["type"]},{t["montant"]},{t["date"]},{t["statut"]},{t["hash"]},{t["frais"]}\n'
    return (csv, 200, {'Content-Type': 'text/csv'})

# --- EXTENSIBILITÉ : Ajoutez ici vos routes métiers personnalisées ---

# --- FIN DU TEMPLATE CRYPTO ---