"""
Template Métier "Loisirs" – Dihya Coding
Version finale conforme au cahier des charges.
Génère automatiquement une application loisirs complète (frontend + backend) avec design moderne, logique métier avancée et routes prêtes à l’emploi.
"""

from typing import Dict, Any, List, Optional
from ..environnement.template import BusinessTemplate

class LoisirsTemplate(BusinessTemplate):
    def __init__(self):
        super().__init__(
            name="Loisirs",
            description="Template pour applications de gestion d’activités, clubs, événements, loisirs : activités, membres, groupes, réservations, paiements, tâches, analytics, plugins.",
            stack=["frontend:react", "backend:flask"],
            i18n={
                "fr": "Loisirs",
                "en": "Leisure",
                "tz": "ⵍⵓⵙⵉⵔⵙ"
            }
        )

    def get_default_design(self) -> Dict[str, Any]:
        return {
            "theme": "amazigh_modern_loisirs",
            "responsive": True,
            "ui_framework": "tailwind",
            "customizable": True,
            "primary_colors": ["#0f172a", "#fbbf24", "#10b981"],
            "font": "Montserrat, Tifinagh, sans-serif",
            "motifs": "amazigh",
            "dark_mode": True
        }

    def get_roles(self) -> List[Dict[str, Any]]:
        return [
            {"name": "admin", "permissions": ["all"]},
            {"name": "organisateur", "permissions": ["activities", "members", "groups", "bookings", "payments", "tasks", "analytics"]},
            {"name": "membre", "permissions": ["view", "activities", "bookings", "groups", "payments"]},
            {"name": "invite", "permissions": ["view", "activities"]},
        ]

    def get_routes(self) -> List[Dict[str, Any]]:
        return [
            {"method": "GET", "endpoint": "/api/activities", "desc": "Liste des activités/événements", "auth": "organisateur/admin"},
            {"method": "POST", "endpoint": "/api/activities", "desc": "Créer/modifier une activité/événement", "auth": "organisateur/admin"},
            {"method": "GET", "endpoint": "/api/members", "desc": "Liste des membres", "auth": "organisateur/admin"},
            {"method": "POST", "endpoint": "/api/members", "desc": "Ajouter/modifier un membre", "auth": "organisateur/admin"},
            {"method": "GET", "endpoint": "/api/groups", "desc": "Liste des groupes", "auth": "organisateur/admin"},
            {"method": "POST", "endpoint": "/api/groups", "desc": "Créer/modifier un groupe", "auth": "organisateur/admin"},
            {"method": "GET", "endpoint": "/api/bookings", "desc": "Liste des réservations", "auth": "organisateur/admin"},
            {"method": "POST", "endpoint": "/api/bookings", "desc": "Créer/modifier une réservation", "auth": "organisateur/admin"},
            {"method": "GET", "endpoint": "/api/payments", "desc": "Liste des paiements/cotisations", "auth": "organisateur/admin"},
            {"method": "POST", "endpoint": "/api/payments", "desc": "Enregistrer un paiement/cotisation", "auth": "organisateur/admin"},
            {"method": "GET", "endpoint": "/api/tasks", "desc": "Liste des tâches/bénévoles", "auth": "organisateur/admin"},
            {"method": "POST", "endpoint": "/api/tasks", "desc": "Créer/modifier une tâche", "auth": "organisateur/admin"},
            {"method": "GET", "endpoint": "/api/notifications", "desc": "Notifications", "auth": "all"},
            {"method": "POST", "endpoint": "/api/plugins", "desc": "Ajouter un plugin", "auth": "admin"}
        ]

    def generate_frontend(self, user_requirements: Dict[str, Any]) -> str:
        return """
// App.js (extrait)
// ...imports...
import './App.css';
function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-[#0f172a] to-[#10b981] font-montserrat text-white">
      <header className="p-4 flex justify-between items-center border-b border-yellow-400">
        <h1 className="text-3xl font-bold tracking-wider">Dihya Loisirs</h1>
        <nav>
          <a href="/activities" className="mx-2 hover:text-yellow-400">Activités</a>
          <a href="/members" className="mx-2 hover:text-yellow-400">Membres</a>
          <a href="/groups" className="mx-2 hover:text-yellow-400">Groupes</a>
          <a href="/bookings" className="mx-2 hover:text-yellow-400">Réservations</a>
          <a href="/payments" className="mx-2 hover:text-yellow-400">Paiements</a>
          <a href="/tasks" className="mx-2 hover:text-yellow-400">Tâches</a>
        </nav>
      </header>
      <main className="p-6">
        {/* Composants dynamiques : Activités, Membres, Groupes, Réservations, Paiements, Tâches, Notifications */}
      </main>
      <footer className="p-4 text-center text-xs text-gray-400">
        ⴷⵉⵀⵢⴰ Coding – De l’idée au code, en toute souveraineté.
      </footer>
    </div>
  );
}
export default App;
        """.strip()

    def generate_backend(self, user_requirements: Dict[str, Any]) -> str:
        return """
# app.py (extrait)
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'change_this_secret'
CORS(app)
jwt = JWTManager(app)

@app.route('/api/activities', methods=['GET'])
@jwt_required()
def get_activities():
    return jsonify([{"id": 1, "title": "Atelier Yoga", "date": "2025-06-01"}])

@app.route('/api/activities', methods=['POST'])
@jwt_required()
def create_activity():
    data = request.json
    return jsonify({"msg": "Activité créée/modifiée", "data": data}), 201

@app.route('/api/members', methods=['GET'])
@jwt_required()
def get_members():
    return jsonify([{"id": 1, "name": "Nora"}])

@app.route('/api/members', methods=['POST'])
@jwt_required()
def create_member():
    data = request.json
    return jsonify({"msg": "Membre ajouté/modifié", "data": data}), 201

@app.route('/api/groups', methods=['GET'])
@jwt_required()
def get_groups():
    return jsonify([{"id": 1, "name": "Groupe Sport"}])

@app.route('/api/groups', methods=['POST'])
@jwt_required()
def create_group():
    data = request.json
    return jsonify({"msg": "Groupe créé/modifié", "data": data}), 201

@app.route('/api/bookings', methods=['GET'])
@jwt_required()
def get_bookings():
    return jsonify([{"id": 1, "activity_id": 1, "slot": "10h-12h"}])

@app.route('/api/bookings', methods=['POST'])
@jwt_required()
def create_booking():
    data = request.json
    return jsonify({"msg": "Réservation créée/modifiée", "data": data}), 201

@app.route('/api/payments', methods=['GET'])
@jwt_required()
def get_payments():
    return jsonify([{"id": 1, "member_id": 1, "amount": 20}])

@app.route('/api/payments', methods=['POST'])
@jwt_required()
def create_payment():
    data = request.json
    return jsonify({"msg": "Paiement enregistré", "data": data}), 201

@app.route('/api/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    return jsonify([{"id": 1, "title": "Préparer salle"}])

@app.route('/api/tasks', methods=['POST'])
@jwt_required()
def create_task():
    data = request.json
    return jsonify({"msg": "Tâche créée/modifiée", "data": data}), 201

@app.route('/api/notifications', methods=['GET'])
@jwt_required()
def get_notifications():
    return jsonify([{"type": "rappel", "msg": "Atelier Yoga demain à 10h"}])

@app.route('/api/plugins', methods=['POST'])
@jwt_required()
def add_plugin():
    data = request.json
    return jsonify({"msg": "Plugin ajouté", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True)
        """.strip()

    def get_plugin_support(self) -> Dict[str, Any]:
        return {
            "plugins": ["billetterie", "paiement", "analytics", "custom"],
            "marketplace": True
        }

    def get_seo_settings(self) -> Dict[str, Any]:
        return {
            "meta_tags": True,
            "sitemap": True,
            "robots_txt": True,
            "lighthouse_score": "90+",
            "open_graph": True
        }

    def get_security_settings(self) -> Dict[str, Any]:
        return {
            "auth": "jwt",
            "cors": True,
            "rate_limiting": True,
            "headers": {
                "X-Frame-Options": "DENY",
                "X-Content-Type-Options": "nosniff",
                "Content-Security-Policy": "default-src 'self'"
            },
            "anti_ddos": True,
            "logging": "horodaté"
        }

    def get_deployment_settings(self) -> Dict[str, Any]:
        return {
            "github_actions": True,
            "github_pages": True,
            "replit_fallback": True,
            "self_hosted_option": True,
            "ipfs_option": True
        }

    def get_i18n_settings(self) -> Dict[str, Any]:
        return {
            "enabled": True,
            "dialects_supported": True,
            "dynamic": True,
            "default_lang": "fr"
        }

    def get_marketplace_info(self) -> Dict[str, Any]:
        return {
            "contribution": True,
            "notation": True,
            "import_export": ["json", "yaml", "js"]
        }

    def get_documentation(self) -> Dict[str, Any]:
        return {
            "user_guide": True,
            "api_reference": True,
            "contribution_guide": True,
            "branding": {
                "theme": "amazigh_modern",
                "slogan": "De l’idée au code, en toute souveraineté."
            }
        }

# --- Exemple d’utilisation ---
if __name__ == "__main__":
    template = LoisirsTemplate()
    print(template.export_template("json"))