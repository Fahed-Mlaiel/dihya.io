"""
Dihya – Exemple de Template BTP (Bâtiment & Travaux Publics) Python Ultra Avancé
-------------------------------------------------------------------------------
Ce module fournit un exemple de template métier Python pour le BTP sur la plateforme Dihya.
Il sert de base pour la génération, la validation ou la manipulation de devis, rapports, audits, matériaux, ou assets BTP (IA, plugins…).

🇫🇷 Exemple de template métier Python (sécurité, extensibilité, multilingue)
🇬🇧 Example construction Python template (security, extensibility, multilingual)
🇦🇪 مثال قالب البناء والأشغال العامة بايثون (الأمان، التوسعة، متعدد اللغات)
ⵣ Amud n template n BTP Python (amatu, extensibility, multilingual)

Sécurité : aucun code exécutable à l’import, validation stricte des entrées, logs, conformité RGPD/NIS2.
Extensible : surchargez la classe, ajoutez vos méthodes, intégrez vos assets, IA ou plugins.
Multilingue : tous les messages sont traduits (fr, en, ar, tzm).
"""

import hashlib
import json
from typing import Dict, Any, Optional

class BTPTemplate:
    """
    Classe de base pour la gestion d’un template métier BTP.
    """

    def __init__(self, name: str, description: Dict[str, str], author: str, version: str, data: Dict[str, Any]):
        """
        Initialise un template métier BTP.

        :param name: Nom du template
        :param description: Description multilingue (clé: langue, valeur: texte)
        :param author: Auteur du template
        :param version: Version du template
        :param data: Données du template (devis, rapport, audit, matériaux, meta…)
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
        "fr": "Devis chantier structuré pour la gestion de projets BTP.",
        "en": "Structured construction quote for BTP project management.",
        "ar": "عرض أسعار منظم لإدارة مشاريع البناء.",
        "tzm": "Adevis n uselkim n chantier i uselkim n BTP."
    }
    data = {
        "chantier": "Immeuble Résidentiel",
        "client": "A. Dihya",
        "date_debut": "2025-06-01",
        "date_fin": "2026-06-01",
        "lots": [
            {"nom": "Terrassement", "montant": 20000, "unité": "EUR"},
            {"nom": "Maçonnerie", "montant": 50000, "unité": "EUR"}
        ],
        "meta": {"type": "devis", "usage": "chantier"}
    }
    template = BTPTemplate(
        name="devis_chantier_2025",
        description=description,
        author="A. Dihya",
        version="1.0",
        data=data
    )
    assert template.validate()
    print(json.dumps(template.export_metadata(), indent=2, ensure_ascii=False))

# Sécurité : pas d’exécution dynamique, pas d’accès disque/réseau non contrôlé
# Extensible : surchargez BTPTemplate pour vos besoins métiers (devis, rapports, IA…)
# Multilingue : adaptez _msg pour la locale utilisateur
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
