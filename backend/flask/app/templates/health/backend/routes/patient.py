"""
Route API patient – Template Santé Dihya
CRUD patient, sécurité, RGPD, audit, multilingue
"""
from flask import Blueprint, request, jsonify

bp = Blueprint("patient", __name__)

@bp.route("/api/health/patients", methods=["GET"])
def list_patients():
    # Exemple : retourne une liste fictive
    return jsonify([
        {"id": 1, "name": "Alice", "dob": "1990-01-01", "lang": "fr"},
        {"id": 2, "name": "Youssef", "dob": "1985-05-12", "lang": "ar"}
    ])

@bp.route("/api/health/patients", methods=["POST"])
def create_patient():
    data = request.get_json()
    # Validation, RGPD, audit à implémenter
    return jsonify({"message": "Patient créé", "patient": data}), 201
