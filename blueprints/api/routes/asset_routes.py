"""
Blueprint routes API pour un asset métier (Flask)
Inclut : routes GET/POST, docstring, instructions d’extension
"""
from flask import Blueprint, jsonify, request

bp = Blueprint('assets', __name__)

@bp.route('/assets', methods=['GET'])
def list_assets():
    """Retourne la liste des assets."""
    return jsonify([{"id": 1, "name": "Asset 1", "owner": "Alice"}])

@bp.route('/assets', methods=['POST'])
def create_asset():
    """Crée un nouvel asset."""
    return jsonify({"message": "Asset créé", "data": request.json})

# Instructions :
# - Ajouter d’autres routes métier ici
# - Étendre avec middlewares, hooks, etc.
