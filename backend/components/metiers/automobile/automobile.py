# Module principal automobile ultra avancé
class Automobile:
    def __init__(self, nom, statut, proprietaire=None, date_debut=None, date_fin=None):
        self.nom = nom
        self.statut = statut
        self.proprietaire = proprietaire
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.logs = []

    def auditer(self, action, details=None):
        self.logs.append({'action': action, 'details': details})

    def exporter_projet(self):
        return {
            'nom': self.nom,
            'statut': self.statut,
            'proprietaire': self.proprietaire,
            'date_debut': self.date_debut,
            'date_fin': self.date_fin
        }

    def anonymiser(self):
        self.proprietaire = 'ANONYMISED'

    def __repr__(self):
        return f"<Automobile nom={self.nom} statut={self.statut}>"
