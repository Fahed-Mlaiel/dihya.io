"""
Dihya – Modèle métier éducation ultra avancé
--------------------------------------------
Ce module définit la structure, la validation, la gestion multilingue et la sécurité des templates métiers pour l’éducation.
Prêt pour l’extension, la personnalisation, l’intégration IA, la souveraineté numérique et la compatibilité multi-stack.

🇫🇷 Modèle de template éducation (sécurité, extensibilité, multilingue, souveraineté numérique)
🇬🇧 Education template model (security, extensibility, multilingual, digital sovereignty)
🇦🇪 نموذج قالب التعليم (الأمان، التوسعة، متعدد اللغات، السيادة الرقمية)
ⵣ Template n tazrawt n tamedyazt (amatu, extensibility, multilingual, tasertit n digital)
"""

from typing import Dict, Any, Optional, List
import json
import yaml

SUPPORTED_LANGS = ["fr", "en", "ar", "tz"]

class EducationTemplate:
    """
    Classe de base pour un template éducation Dihya.
    Sécurisée, extensible, multilingue, compatible IA et plugins.
    """

    def __init__(
        self,
        template_type: str,
        lang: str,
        structure: List[Dict[str, Any]],
        meta: Optional[Dict[str, Any]] = None,
    ):
        if lang not in SUPPORTED_LANGS:
            raise ValueError(f"Langue non supportée: {lang}")
        self.template_type = template_type
        self.lang = lang
        self.structure = structure
        self.meta = meta or {}

    def to_dict(self) -> Dict[str, Any]:
        """Retourne le template sous forme de dictionnaire."""
        return {
            "type": self.template_type,
            "lang": self.lang,
            "structure": self.structure,
            "meta": self.meta,
        }

    def to_json(self, ensure_ascii=False, indent=2) -> str:
        """Sérialise le template en JSON."""
        return json.dumps(self.to_dict(), ensure_ascii=ensure_ascii, indent=indent)

    def to_yaml(self) -> str:
        """Sérialise le template en YAML."""
        return yaml.dump(self.to_dict(), allow_unicode=True, sort_keys=False)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "EducationTemplate":
        """Crée un template à partir d’un dictionnaire."""
        return EducationTemplate(
            template_type=data.get("type"),
            lang=data.get("lang"),
            structure=data.get("structure", []),
            meta=data.get("meta", {}),
        )

    @staticmethod
    def validate_structure(structure: List[Dict[str, Any]]) -> bool:
        """
        Valide la structure d’un template.
        - Chaque champ doit avoir au moins 'champ' et 'label'.
        """
        for field in structure:
            if "champ" not in field or "label" not in field:
                return False
        return True

    def is_valid(self) -> bool:
        """Valide le template complet."""
        return (
            self.template_type is not None
            and self.lang in SUPPORTED_LANGS
            and self.validate_structure(self.structure)
            and len(self.structure) > 0
        )

# Exemple d’utilisation/documentation multilingue
EXAMPLE_EDUCATION_TEMPLATE = EducationTemplate(
    template_type="examen",
    lang="fr",
    structure=[
        {"champ": "titre", "label": "Titre de l'examen"},
        {"champ": "date", "label": "Date"},
        {"champ": "note_max", "label": "Note maximale"},
    ],
    meta={
        "description": {
            "fr": "Template d'examen standard",
            "en": "Standard exam template",
            "ar": "قالب امتحان قياسي",
            "tz": "Template n tazrawt n examen"
        },
        "roles": ["admin", "enseignant", "élève"],
        "accessibility": {"aria-label": "Examen", "seo": True},
        "version": "1.0.0",
        "license": "AGPL-3.0-or-later"
    }
)

if __name__ == "__main__":
    # Affichage multiformat pour démo, doc, test
    print("# JSON\n", EXAMPLE_EDUCATION_TEMPLATE.to_json())
    print("# YAML\n", EXAMPLE_EDUCATION_TEMPLATE.to_yaml())
    print("# Valid?", EXAMPLE_EDUCATION_TEMPLATE.is_valid())

__all__ = ["EducationTemplate", "EXAMPLE_EDUCATION_TEMPLATE"]
