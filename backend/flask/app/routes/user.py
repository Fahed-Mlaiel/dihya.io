"""
Routes de gestion des utilisateurs pour l'API Dihya Coding.
Inclut : CRUD utilisateur, gestion des rôles, profil, sécurité, validation.
"""

from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import user
from ..models.user import User
from ..services.user_service import (
    get_user_by_id, get_all_users, update_user, delete_user
)
from ..utils.validators import validate_user_update

@user.route('/api/users', methods=['GET'])
@jwt_required()
def list_users():
    """
    Liste tous les utilisateurs (admin uniquement).
    ---
    responses:
      200: Liste des utilisateurs
      403: Accès refusé
    """
    current_user_id = get_jwt_identity()
    current_user = get_user_by_id(current_user_id)
    if not current_user or not current_user.is_admin:
        return jsonify({"error": "Accès refusé"}), 403
    users = get_all_users()
    return jsonify([u.to_dict() for u in users]), 200

@user.route('/api/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    """
    Récupère les informations d'un utilisateur par ID.
    ---
    responses:
      200: Utilisateur trouvé
      404: Utilisateur non trouvé
    """
    u = get_user_by_id(user_id)
    if not u:
        return jsonify({"error": "Utilisateur non trouvé"}), 404
    return jsonify(u.to_dict()), 200

@user.route('/api/users/me', methods=['GET'])
@jwt_required()
def get_profile():
    """
    Récupère le profil de l'utilisateur connecté.
    ---
    responses:
      200: Profil utilisateur
    """
    current_user_id = get_jwt_identity()
    u = get_user_by_id(current_user_id)
    if not u:
        return jsonify({"error": "Utilisateur non trouvé"}), 404
    return jsonify(u.to_dict()), 200

@user.route('/api/users/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user_route(user_id):
    """
    Met à jour les informations d'un utilisateur (admin ou soi-même).
    ---
    responses:
      200: Utilisateur mis à jour
      400: Erreur de validation
      403: Accès refusé
      404: Utilisateur non trouvé
    """
    current_user_id = get_jwt_identity()
    current_user = get_user_by_id(current_user_id)
    if not current_user or (current_user.id != user_id and not current_user.is_admin):
        return jsonify({"error": "Accès refusé"}), 403

    data = request.get_json()
    errors = validate_user_update(data)
    if errors:
        return jsonify({"errors": errors}), 400

    updated, err = update_user(user_id, data)
    if err:
        return jsonify({"error": err}), 400
    return jsonify(updated.to_dict()), 200

@user.route('/api/users/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user_route(user_id):
    """
    Supprime un utilisateur (admin uniquement).
    ---
    responses:
      204: Utilisateur supprimé
      403: Accès refusé
      404: Utilisateur non trouvé
    """
    current_user_id = get_jwt_identity()
    current_user = get_user_by_id(current_user_id)
    if not current_user or not current_user.is_admin:
        return jsonify({"error": "Accès refusé"}), 403

    deleted, err = delete_user(user_id)
    if err:
        return jsonify({"error": err}), 404
    return '', 204