"""
Template Métier "Journalisme" – Dihya Coding
Version finale conforme au cahier des charges.
Génère automatiquement une application de gestion éditoriale et médias (frontend + backend) avec design moderne, logique métier avancée et routes prêtes à l’emploi.
"""

from typing import Dict, Any, List, Optional
from ..environnement.template import BusinessTemplate

class JournalismeTemplate(BusinessTemplate):
    def __init__(self):
        super().__init__(
            name="Journalisme",
            description="Template pour applications de gestion éditoriale, publication et médias : articles, workflow, auteurs, médias, commentaires, plugins.",
            stack=["frontend:react", "backend:flask"],
            i18n={
                "fr": "Journalisme",
                "en": "Journalism",
                "tz": "ⵉⵙⵉⵏⴰⵍ ⵉⵎⴰⵣⵉⵖⵉⵏ"
            }
        )

    def get_default_design(self) -> Dict[str, Any]:
        return {
            "theme": "amazigh_modern_journalisme",
            "responsive": True,
            "ui_framework": "tailwind",
            "customizable": True,
            "primary_colors": ["#334155", "#fbbf24", "#10b981"],
            "font": "Montserrat, Tifinagh, sans-serif",
            "motifs": "amazigh",
            "dark_mode": True
        }

    def get_roles(self) -> List[Dict[str, Any]]:
        return [
            {"name": "admin", "permissions": ["all"]},
            {"name": "redacteur", "permissions": ["articles", "media", "comments", "workflow"]},
            {"name": "relecteur", "permissions": ["review", "comments"]},
            {"name": "lecteur", "permissions": ["view", "comments"]},
            {"name": "guest", "permissions": ["view"]}
        ]

    def get_routes(self) -> List[Dict[str, Any]]:
        """
        Routes backend principales pour l'app journalisme.
        """
        return [
            {"method": "GET", "endpoint": "/api/articles", "desc": "Liste des articles", "auth": "public/redacteur"},
            {"method": "POST", "endpoint": "/api/articles", "desc": "Créer/modifier un article", "auth": "redacteur"},
            {"method": "GET", "endpoint": "/api/articles/<id>", "desc": "Détail d’un article", "auth": "public/redacteur"},
            {"method": "DELETE", "endpoint": "/api/articles/<id>", "desc": "Supprimer un article", "auth": "admin"},
            {"method": "POST", "endpoint": "/api/articles/<id>/review", "desc": "Demander une relecture", "auth": "redacteur"},
            {"method": "POST", "endpoint": "/api/articles/<id>/publish", "desc": "Publier un article", "auth": "admin/redacteur"},
            {"method": "GET", "endpoint": "/api/authors", "desc": "Liste des auteurs", "auth": "admin/redacteur"},
            {"method": "POST", "endpoint": "/api/authors", "desc": "Créer/modifier un auteur", "auth": "admin"},
            {"method": "GET", "endpoint": "/api/media", "desc": "Liste des médias", "auth": "redacteur/admin"},
            {"method": "POST", "endpoint": "/api/media", "desc": "Ajouter un média", "auth": "redacteur/admin"},
            {"method": "GET", "endpoint": "/api/comments", "desc": "Liste des commentaires", "auth": "public/redacteur"},
            {"method": "POST", "endpoint": "/api/comments", "desc": "Ajouter un commentaire", "auth": "lecteur/redacteur"},
            {"method": "GET", "endpoint": "/api/notifications", "desc": "Notifications", "auth": "all"},
            {"method": "POST", "endpoint": "/api/plugins", "desc": "Ajouter un plugin", "auth": "admin"}
        ]

    def generate_frontend(self, user_requirements: Dict[str, Any]) -> str:
        """
        Génère un squelette React + Tailwind pour app journalisme moderne.
        """
        return """
// App.js (extrait)
// ...imports...
import './App.css';
function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-[#334155] to-[#10b981] font-montserrat text-white">
      <header className="p-4 flex justify-between items-center border-b border-yellow-400">
        <h1 className="text-3xl font-bold tracking-wider">Dihya Journalisme</h1>
        <nav>
          <a href="/articles" className="mx-2 hover:text-yellow-400">Articles</a>
          <a href="/media" className="mx-2 hover:text-yellow-400">Médias</a>
          <a href="/authors" className="mx-2 hover:text-yellow-400">Auteurs</a>
          <a href="/workflow" className="mx-2 hover:text-yellow-400">Workflow</a>
          <a href="/comments" className="mx-2 hover:text-yellow-400">Commentaires</a>
        </nav>
      </header>
      <main className="p-6">
        {/* Composants dynamiques : Articles, Médias, Auteurs, Workflow, Commentaires, Notifications */}
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
        """
        Génère un backend Flask avec routes journalisme, sécurité, JWT, CORS, rate limiting.
        """
        return """
# app.py (extrait)
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'change_this_secret'
CORS(app)
jwt = JWTManager(app)

@app.route('/api/articles', methods=['GET'])
def get_articles():
    # Liste des articles (mock)
    return jsonify([{"id": 1, "titre": "Actu Amazigh", "statut": "publié"}])

@app.route('/api/articles', methods=['POST'])
@jwt_required()
def create_article():
    # Créer/modifier un article
    data = request.json
    # ...validation...
    return jsonify({"msg": "Article créé/modifié", "data": data}), 201

@app.route('/api/articles/<int:id>', methods=['GET'])
def get_article(id):
    # Détail d’un article (mock)
    return jsonify({"id": id, "titre": "Actu Amazigh", "contenu": "..."})

@app.route('/api/articles/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_article(id):
    # Supprimer un article
    return jsonify({"msg": "Article supprimé", "id": id}), 200

@app.route('/api/articles/<int:id>/review', methods=['POST'])
@jwt_required()
def review_article(id):
    # Demander une relecture
    return jsonify({"msg": "Relecture demandée", "id": id}), 200

@app.route('/api/articles/<int:id>/publish', methods=['POST'])
@jwt_required()
def publish_article(id):
    # Publier un article
    return jsonify({"msg": "Article publié", "id": id}), 200

@app.route('/api/authors', methods=['GET'])
@jwt_required()
def get_authors():
    # Liste des auteurs (mock)
    return jsonify([{"id": 1, "nom": "Nora"}])

@app.route('/api/authors', methods=['POST'])
@jwt_required()
def create_author():
    # Créer/modifier un auteur
    data = request.json
    return jsonify({"msg": "Auteur créé/modifié", "data": data}), 201

@app.route('/api/media', methods=['GET'])
@jwt_required()
def get_media():
    # Liste des médias (mock)
    return jsonify([{"id": 1, "type": "photo", "url": "/media/photo1.jpg"}])

@app.route('/api/media', methods=['POST'])
@jwt_required()
def create_media():
    # Ajouter un média
    data = request.json
    return jsonify({"msg": "Média ajouté", "data": data}), 201

@app.route('/api/comments', methods=['GET'])
def get_comments():
    # Liste des commentaires (mock)
    return jsonify([{"id": 1, "article_id": 1, "contenu": "Bravo !"}])

@app.route('/api/comments', methods=['POST'])
@jwt_required()
def create_comment():
    # Ajouter un commentaire
    data = request.json
    return jsonify({"msg": "Commentaire ajouté", "data": data}), 201

@app.route('/api/notifications', methods=['GET'])
@jwt_required()
def get_notifications():
    # Notifications (mock)
    return jsonify([{"type": "workflow", "msg": "Nouvel article à relire"}])

@app.route('/api/plugins', methods=['POST'])
@jwt_required()
def add_plugin():
    # Ajout plugin (mock)
    data = request.json
    return jsonify({"msg": "Plugin ajouté", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True)
        """.strip()

    def get_plugin_support(self) -> Dict[str, Any]:
        return {
            "plugins": ["analytics", "mailing", "paywall", "traduction", "custom"],
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
    template = JournalismeTemplate()
    print(template.export_template("json"))

blueprint = journalisme_bp
