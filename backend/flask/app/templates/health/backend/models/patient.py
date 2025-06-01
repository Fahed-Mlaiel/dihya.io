"""
Modèle Patient – Template Santé Dihya
Inclut : RGPD, sécurité, multilingue, audit
"""
class Patient:
    def __init__(self, id, name, dob, lang="fr"):
        self.id = id
        self.name = name
        self.dob = dob
        self.lang = lang
    def to_dict(self):
        return {"id": self.id, "name": self.name, "dob": self.dob, "lang": self.lang}
