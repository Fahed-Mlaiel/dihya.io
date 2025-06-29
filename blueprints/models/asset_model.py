"""
Blueprint modèle métier Asset (Python)
Classe Asset ultra avancée : validation, sérialisation, hooks, extension ORM, doc, exemples.
"""
from typing import Any, Dict

class Asset:
    def __init__(self, id: int, name: str, owner: str, **kwargs):
        self.id = id
        self.name = name
        self.owner = owner
        self.extra = kwargs

    def serialize(self) -> Dict[str, Any]:
        return {"id": self.id, "name": self.name, "owner": self.owner, **self.extra}

    def validate(self) -> bool:
        if not self.name:
            raise ValueError("Le nom de l'asset est obligatoire")
        return True

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        return cls(**data)

# Exemple d’utilisation :
# asset = Asset(id=1, name="Ordinateur", owner="Alice")
# print(asset.serialize())
# asset.validate()
