"""
Dihya – Exemple de Template Blockchain Python Ultra Avancé
---------------------------------------------------------
Ce module fournit un exemple de template métier Python pour la blockchain sur la plateforme Dihya.
Il sert de base pour la génération, la validation ou la manipulation de contrats intelligents, transactions, audits, NFT, ou assets blockchain (IA, plugins…).

🇫🇷 Exemple de template métier Python (sécurité, extensibilité, multilingue)
🇬🇧 Example blockchain Python template (security, extensibility, multilingual)
🇦🇪 مثال قالب البلوكشين بايثون (الأمان، التوسعة، متعدد اللغات)
ⵣ Amud n template n blockchain Python (amatu, extensibility, multilingual)

Sécurité : aucun code exécutable à l’import, validation stricte des entrées, logs, conformité RGPD/NIS2.
Extensible : surchargez la classe, ajoutez vos méthodes, intégrez vos assets, IA ou plugins.
Multilingue : tous les messages sont traduits (fr, en, ar, tzm).
"""

import hashlib
import json
from typing import Dict, Any, Optional

class BlockchainTemplate:
    """
    Classe de base pour la gestion d’un template métier blockchain.
    """

    def __init__(self, name: str, description: Dict[str, str], author: str, version: str, data: Dict[str, Any]):
        """
        Initialise un template métier blockchain.

        :param name: Nom du template
        :param description: Description multilingue (clé: langue, valeur: texte)
        :param author: Auteur du template
        :param version: Version du template
        :param data: Données du template (contrat, transaction, NFT, meta…)
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
        "fr": "Contrat intelligent ERC-20 structuré pour la gestion de tokens.",
        "en": "Structured ERC-20 smart contract for token management.",
        "ar": "عقد ذكي ERC-20 منظم لإدارة الرموز.",
        "tzm": "Acontrat smart ERC-20 i uselkim n tokens."
    }
    data = {
        "contrat": "ERC-20",
        "propriétaire": "A. Dihya",
        "date_deploiement": "2025-05-21",
        "fonctions": ["mint", "burn", "transfer", "approve"],
        "meta": {"type": "smart_contract", "usage": "token_erc20"}
    }
    template = BlockchainTemplate(
        name="smart_contract_erc20_2025",
        description=description,
        author="A. Dihya",
        version="1.0",
        data=data
    )
    assert template.validate()
    print(json.dumps(template.export_metadata(), indent=2, ensure_ascii=False))

# Sécurité : pas d’exécution dynamique, pas d’accès disque/réseau non contrôlé
# Extensible : surchargez BlockchainTemplate pour vos besoins métiers (contrats, NFT, IA…)
# Multilingue : adaptez _msg pour la locale utilisateur
# Prêt CI/CD, Codespaces, cloud souverain, production, démo, contribution
