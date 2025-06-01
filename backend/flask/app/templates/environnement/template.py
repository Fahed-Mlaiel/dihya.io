"""
Template Métier Dihya Coding – Environnement
Ce fichier définit la structure de base pour un template métier extensible et personnalisable.
Chaque template métier doit hériter de cette classe et implémenter les méthodes nécessaires.
"""

from typing import Dict, Any, List, Optional

class BusinessTemplate:
    """
    Classe de base pour un template métier.
    À étendre pour chaque secteur (santé, juridique, etc.).
    """

    def __init__(self, name: str, description: str, stack: List[str], i18n: Optional[Dict[str, str]] = None):
        self.name = name
        self.description = description
        self.stack = stack  # Ex: ["frontend:react", "backend:flask"]
        self.i18n = i18n or {}

    def get_metadata(self) -> Dict[str, Any]:
        """
        Retourne les métadonnées du template.
        """
        return {
            "name": self.name,
            "description": self.description,
            "stack": self.stack,
            "i18n": self.i18n
        }

    def generate_frontend(self, user_requirements: Dict[str, Any]) -> str:
        """
        Génère le code frontend selon les besoins utilisateur.
        À surcharger dans les sous-classes.
        """
        raise NotImplementedError("La génération frontend doit être implémentée dans le template métier.")

    def generate_backend(self, user_requirements: Dict[str, Any]) -> str:
        """
        Génère le code backend selon les besoins utilisateur.
        À surcharger dans les sous-classes.
        """
        raise NotImplementedError("La génération backend doit être implémentée dans le template métier.")

    def get_default_design(self) -> Dict[str, Any]:
        """
        Retourne les paramètres de design par défaut (UI/UX, thèmes, responsive, etc.).
        """
        return {
            "theme": "amazigh_modern_environnement",
            "responsive": True,
            "ui_framework": "tailwind",
            "customizable": True,
            "primary_colors": ["#16a34a", "#fbbf24", "#10b981"],
            "font": "Montserrat, Tifinagh, sans-serif",
            "motifs": "amazigh",
            "dark_mode": True
        }

    def get_roles(self) -> List[Dict[str, Any]]:
        """
        Définit les rôles utilisateurs par défaut.
        """
        return [
            {"name": "admin", "permissions": ["all"]},
            {"name": "user", "permissions": ["read", "write"]},
            {"name": "guest", "permissions": ["read"]}
        ]

    def get_security_settings(self) -> Dict[str, Any]:
        """
        Paramètres de sécurité par défaut.
        """
        return {
            "auth": "jwt",
            "cors": True,
            "rate_limiting": True,
            "headers": {
                "X-Frame-Options": "DENY",
                "X-Content-Type-Options": "nosniff"
            }
        }

    def get_seo_settings(self) -> Dict[str, Any]:
        """
        Paramètres SEO par défaut.
        """
        return {
            "meta_tags": True,
            "sitemap": True,
            "robots_txt": True,
            "lighthouse_score": "90+"
        }

    def get_deployment_settings(self) -> Dict[str, Any]:
        """
        Paramètres de déploiement automatique.
        """
        return {
            "github_actions": True,
            "github_pages": True,
            "replit_fallback": True,
            "self_hosted_option": True
        }

    def get_i18n_settings(self) -> Dict[str, Any]:
        """
        Paramètres de traduction automatique.
        """
        return {
            "enabled": True,
            "dialects_supported": True,
            "dynamic": True
        }

    def get_plugin_support(self) -> Dict[str, Any]:
        """
        Support des plugins et extensions.
        """
        return {
            "plugins": ["analytics", "cms", "stripe", "custom"],
            "marketplace": True
        }

    def export_template(self, format: str = "json") -> Any:
        """
        Export du template métier (JSON, YAML, etc.).
        """
        import json, yaml
        data = self.get_metadata()
        if format == "json":
            return json.dumps(data, indent=2)
        elif format == "yaml":
            return yaml.dump(data)
        else:
            raise ValueError("Format d'export non supporté.")

# Exemple d’implémentation d’un template métier pour la santé
class HealthTemplate(BusinessTemplate):
    def __init__(self):
        super().__init__(
            name="Santé",
            description="Template pour applications médicales (gestion patients, RDV, dossiers, etc.)",
            stack=["frontend:react", "backend:flask"]
        )

    def generate_frontend(self, user_requirements: Dict[str, Any]) -> str:
        # Génération d’un squelette React avec Material UI/Tailwind
        return "// Code React généré dynamiquement selon user_requirements"

    def generate_backend(self, user_requirements: Dict[str, Any]) -> str:
        # Génération d’une API Flask sécurisée
        return "# Code Flask généré dynamiquement selon user_requirements"

# Pour ajouter un nouveau métier, il suffit d’étendre BusinessTemplate et d’implémenter les méthodes.
# Les templates peuvent être importés/exportés via la marketplace ou l’API.

# --- Exemple d’utilisation ---
if __name__ == "__main__":
    template = HealthTemplate()
    print(template.export_template("json"))
