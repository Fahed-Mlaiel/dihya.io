"""
Routes d'authentification pour l'API Dihya Coding.
Inclut : inscription, connexion, refresh token, déconnexion.
Sécurité JWT, validation des entrées, bonnes pratiques.
"""

from flask import request, jsonify
from flask_jwt_extended import (
    create_access_token, create_refresh_token,
    jwt_required, get_jwt_identity, unset_jwt_cookies
)
from werkzeug.security import check_password_hash
from . import auth
from ..models.user import User  # À adapter selon ton ORM
from ..services.auth_service import register_user, authenticate_user
from ..utils.validators import validate_registration, validate_login

@auth.route('/api/auth/register', methods=['POST'])
def register():
    """
    Inscription d'un nouvel utilisateur.
    ---
    responses:
      201: Utilisateur créé
      400: Erreur de validation ou utilisateur existant
    """
    data = request.get_json()
    errors = validate_registration(data)
    if errors:
        return jsonify({"errors": errors}), 400

    user, err = register_user(data)
    if err:
        return jsonify({"error": err}), 400

    return jsonify({"message": "Utilisateur créé avec succès.", "user": user.to_dict()}), 201

@auth.route('/api/auth/login', methods=['POST'])
def login():
    """
    Connexion utilisateur, retourne un JWT access et refresh.
    ---
    responses:
      200: Connexion réussie
      401: Identifiants invalides
    """
    data = request.get_json()
    errors = validate_login(data)
    if errors:
        return jsonify({"errors": errors}), 400

    user = authenticate_user(data["email"], data["password"])
    if not user:
        return jsonify({"error": "Identifiants invalides."}), 401

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    return jsonify({
        "access_token": access_token,
        "refresh_token": refresh_token,
        "user": user.to_dict()
    }), 200

@auth.route('/api/auth/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    """
    Rafraîchit le token d'accès JWT.
    ---
    responses:
      200: Nouveau token d'accès
      401: Token refresh invalide
    """
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify({"access_token": access_token}), 200

@auth.route('/api/auth/logout', methods=['POST'])
@jwt_required()
def logout():
    """
    Déconnexion utilisateur (invalide les cookies JWT côté client).
    ---
    responses:
      200: Déconnexion réussie
    """
    response = jsonify({"message": "Déconnexion réussie."})
    unset_jwt_cookies(response)
    return response, 200