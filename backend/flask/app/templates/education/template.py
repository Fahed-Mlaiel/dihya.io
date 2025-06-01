"""
Template Métier : Éducation
Backend Flask – Dihya Coding
Version finale conforme au cahier des charges
"""

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

education_bp = Blueprint('education', __name__, url_prefix='/api')

# --- Modèles simulés (à remplacer par ORM/DB dans un vrai projet) ---

cours = []
utilisateurs = []
classes = []
devoirs = []
notes = []
ressources = []

# --- ROUTES COURS ---

@education_bp.route('/cours', methods=['GET'])
def list_cours():
    """Liste des cours (Public)"""
    return jsonify(cours), 200

@education_bp.route('/cours', methods=['POST'])
@jwt_required()
def ajouter_cours():
    """Ajouter un cours (Admin/Professeur)"""
    data = request.get_json()
    cours_obj = {
        "id": len(cours) + 1,
        "titre": data.get("titre"),
        "description": data.get("description"),
        "professeur": data.get("professeur"),
        "classe": data.get("classe"),
        "ressources": data.get("ressources", [])
    }
    cours.append(cours_obj)
    return jsonify({"message": "Cours ajouté", "cours": cours_obj}), 201

# --- ROUTES UTILISATEURS (ÉLÈVES/PROFESSEURS) ---

@education_bp.route('/utilisateurs', methods=['GET'])
@jwt_required()
def list_utilisateurs():
    """Liste des utilisateurs (Admin)"""
    return jsonify(utilisateurs), 200

@education_bp.route('/utilisateurs', methods=['POST'])
def creer_utilisateur():
    """Créer un utilisateur (Public)"""
    data = request.get_json()
    utilisateur = {
        "id": len(utilisateurs) + 1,
        "nom": data.get("nom"),
        "email": data.get("email"),
        "role": data.get("role", "eleve"),
        "classe": data.get("classe"),
        "profil": data.get("profil", {})
    }
    utilisateurs.append(utilisateur)
    return jsonify({"message": "Utilisateur créé", "utilisateur": utilisateur}), 201

# --- ROUTES CLASSES ---

@education_bp.route('/classes', methods=['GET'])
def list_classes():
    """Liste des classes (Public)"""
    return jsonify(classes), 200

@education_bp.route('/classes', methods=['POST'])
@jwt_required()
def ajouter_classe():
    """Ajouter une classe (Admin)"""
    data = request.get_json()
    classe = {
        "id": len(classes) + 1,
        "nom": data.get("nom"),
        "niveau": data.get("niveau"),
        "annee": data.get("annee"),
        "eleves": data.get("eleves", [])
    }
    classes.append(classe)
    return jsonify({"message": "Classe ajoutée", "classe": classe}), 201

# --- ROUTES DEVOIRS ---

@education_bp.route('/devoirs', methods=['GET'])
@jwt_required()
def list_devoirs():
    """Liste des devoirs (Professeur/Élève)"""
    return jsonify(devoirs), 200

@education_bp.route('/devoirs', methods=['POST'])
@jwt_required()
def ajouter_devoir():
    """Ajouter un devoir (Professeur)"""
    data = request.get_json()
    devoir = {
        "id": len(devoirs) + 1,
        "titre": data.get("titre"),
        "description": data.get("description"),
        "classe": data.get("classe"),
        "date_limite": data.get("date_limite"),
        "ressources": data.get("ressources", [])
    }
    devoirs.append(devoir)
    return jsonify({"message": "Devoir ajouté", "devoir": devoir}), 201

# --- ROUTES NOTES ---

@education_bp.route('/notes', methods=['GET'])
@jwt_required()
def list_notes():
    """Liste des notes (Professeur/Élève)"""
    return jsonify(notes), 200

@education_bp.route('/notes', methods=['POST'])
@jwt_required()
def ajouter_note():
    """Ajouter une note (Professeur)"""
    data = request.get_json()
    note = {
        "id": len(notes) + 1,
        "eleve": data.get("eleve"),
        "devoir": data.get("devoir"),
        "valeur": data.get("valeur"),
        "commentaire": data.get("commentaire", "")
    }
    notes.append(note)
    return jsonify({"message": "Note ajoutée", "note": note}), 201

# --- ROUTES RESSOURCES ---

@education_bp.route('/ressources', methods=['GET'])
def list_ressources():
    """Liste des ressources pédagogiques (Public)"""
    return jsonify(ressources), 200

@education_bp.route('/ressources', methods=['POST'])
@jwt_required()
def ajouter_ressource():
    """Ajouter une ressource (Professeur/Admin)"""
    data = request.get_json()
    ressource = {
        "id": len(ressources) + 1,
        "titre": data.get("titre"),
        "type": data.get("type"),
        "url": data.get("url"),
        "cours": data.get("cours")
    }
    ressources.append(ressource)
    return jsonify({"message": "Ressource ajoutée", "ressource": ressource}), 201

# --- EXPORT COURS (CSV simulé) ---

@education_bp.route('/export/cours', methods=['GET'])
@jwt_required()
def export_cours():
    """Exporter les cours (CSV simulé)"""
    csv = "id,titre,description,professeur,classe\n"
    for c in cours:
        csv += f'{c["id"]},{c["titre"]},{c["description"]},{c["professeur"]},{c["classe"]}\n'
    return (csv, 200, {'Content-Type': 'text/csv'})

# --- EXTENSIBILITÉ : Ajoutez ici vos routes métiers personnalisées ---

# --- FIN DU TEMPLATE EDUCATION ---

blueprint = education_bp
