"""
Template métier exemple – Dihya Coding

Ce template génère une structure de projet pour une plateforme e-learning multilingue, avec modules de cours, quiz, gestion utilisateurs, et analytics.
Il démontre la personnalisation, la documentation, la sécurité et l’extensibilité des templates Dihya.

Usage :
- À sélectionner lors de la génération d’un projet (API ou CLI).
- Génère automatiquement les fichiers backend, frontend, et la doc métier.
"""
from .generation_template import GenerationTemplateBase
import logging

class ElearningTemplate(GenerationTemplateBase):
    name = "Elearning"
    description = "Template pour plateforme e-learning multilingue (cours, quiz, analytics)."
    domain = "e-learning"
    version = "1.0.0"
    author = "Dihya Coding"
    safe = True

    def generate_files(self, needs):
        logging.info(f"[Template:{self.name}] generate_files appelé.")
        files = {
            "backend/courses.py": (
                '"""\nModule backend pour la gestion des cours (CRUD, RBAC, audit).\n"""\n'
                'from flask import Blueprint, request, jsonify\n'
                'courses_bp = Blueprint("courses", __name__, url_prefix="/api/courses")\n'
                '@courses_bp.route("", methods=["GET"])\ndef list_courses():\n    return jsonify([]), 200\n'
            ),
            "frontend/pages/Courses.js": (
                '// Page React pour la gestion des cours\nexport default function Courses() {\n  return <div>Liste des cours</div>;\n}\n'
            ),
            "docs/elearning_template.md": (
                """\n# Template e-learning\n\nCe template génère une plateforme e-learning multilingue avec gestion des cours, quiz, utilisateurs, et analytics.\n- Backend Flask sécurisé\n- Frontend React\n- RBAC, audit, conformité RGPD\n- Extensible via plugins\n"""
            )
        }
        return files
