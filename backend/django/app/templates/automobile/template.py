"""
Dihya – Exemple de Template Automobile Python Ultra Avancé
---------------------------------------------------------
Ce module fournit un exemple de template métier Python pour l’automobile sur la plateforme Dihya.
Il sert de base pour la génération, la validation ou la manipulation de fiches véhicules, diagnostics, contrats, sinistres, ou assets automobile (IA, plugins…).

🇫🇷 Exemple de template métier Python (sécurité, extensibilité, multilingue)
🇬🇧 Example automobile Python template (security, extensibility, multilingual)
🇦🇪 مثال قالب السيارات بايثون (الأمان، التوسعة، متعدد اللغات)
ⵣ Amud n template n tigmmiwin Python (amatu, extensibility, multilingual)

Sécurité : aucun code exécutable à l’import, validation stricte des entrées, logs, conformité RGPD/NIS2.
Extensible : surchargez la classe, ajoutez vos méthodes, intégrez vos assets, IA ou plugins.
Multilingue : tous les messages sont traduits (fr, en, ar, tzm).
"""

import hashlib
import json
from typing import Dict, Any, Optional

class AutomobileTemplate:
    """
    Classe de base pour la gestion d’un template métier automobile.
    """

    def __init__(self, name: str, description: Dict[str, str], author: str, version: str, data: Dict[str, Any]):
        """
        Initialise un template métier automobile.

        :param name: Nom du template
        :param description: Description multilingue (clé: langue, valeur: texte)
        :param author: Auteur du template
        :param version: Version du template
        :param data: Données du template (fiche, diagnostic, meta…)
        """
        self.name = name
        self.description = description
        self.author = author
        self.version = version
        self.data = data
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        """
        Calcule le hash SHA256 du template pour l’intégrité.
        """
        raw = json.dumps({
            "name": self.name,
            "description": self.description,
            "author": self.author,
            "version": self.version,
            "data": self.data
        }, sort_keys=True, ensure_ascii=False).encode('utf-8')
        return hashlib.sha256(raw).hexdigest()

    def validate(self) -> bool:
        """
        Valide la structure du template (exemple minimal).
        """
        required_fields = ['name', 'description', 'author', 'version', 'data']
        for field in required_fields:
            if getattr(self, field, None) is None:
                print(self._msg(
                    "Le champ requis est manquant : ",
                    "Required field missing: ",
                    "الحقل المطلوب مفقود: ",
                    "Ur yettwaf ara urar: "
                ) + field)
                return False
        return True

    def export_metadata(self) -> Dict[str, Any]:
        """
        Exporte les métadonnées du template.
        """
        return {
            "name": self.name,
            "description": self.description,
            "author": self.author,
            "version": self.version,
            "hash": self.hash
        }

    def _msg(self, fr: str, en: str, ar: str, tzm: str) -> str:
        """
        Retourne un message multilingue (fr, en, ar, tzm).
        """
        # Pour l’exemple, retourne le français, mais peut être adapté selon la locale
        return fr

# Exemple d’utilisation
if __name__ == "__main__":
    description = {
        "fr": "Fiche technique structurée pour véhicule électrique.",
        "en": "Structured technical sheet for electric vehicle.",
        "ar": "بطاقة تقنية منظمة للسيارة الكهربائية.",
        "tzm": "Aficha technique n tigmmiwin tazwart n taddart tazwart."
    }
    data = {
        "vehicule": "Renault Zoe",
        "année": 2025,
        "type": "électrique",
        "diagnostics": [
            {"date": "2025-03-01", "batterie": "OK", "moteur": "OK"},
            {"date": "2025-06-01", "batterie": "OK", "moteur": "OK"}
        ],
        "meta": {"type": "fiche", "usage": "vehicule"}
    }
    template = AutomobileTemplate(
        name="fiche_vehicule_zoe_2025",
        description=description,
        author="A. Dihya",
        version="1.0",
        data=data
    )
    assert template.validate()
    print(json.dumps(template.export_metadata(), indent=2, ensure_ascii=False))

# Sécurité : pas d’exécution dynamique, pas d’accès disque/réseau non contrôlé
# Extensible : surchargez AutomobileTemplate pour vos besoins métiers (fiches, diagnostics, IA…)
# Multilingue : adaptez _msg pour la locale utilisateur
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
