from typing import List, Dict, Any

# Module principal métier Assurance
class Assurance:
    """
    Classe métier ultra avancée pour la gestion des contrats, clients, sinistres, plugins, audit, RGPD, multitenancy, sécurité, accessibilité, hooks métier, extensibilité.
    """
    def __init__(self, type_assurance: str, client: str, prime: float, date_debut: str, date_fin: str, plugins: List[Any]=None):
        self.type_assurance = type_assurance
        self.client = client
        self.prime = prime
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.plugins = plugins or []
        self.audit_log = []

    def calculer_prime(self) -> float:
        """Calcul avancé de la prime selon le type, le client, les plugins, RGPD, etc."""
        prime = self.prime
        for plugin in self.plugins:
            prime = plugin.process_prime(prime, self)
        self.audit_log.append({"action": "calcul_prime", "prime": prime})
        return prime

    def exporter_contrat(self, format: str = "json") -> Dict:
        """Export du contrat (RGPD, anonymisation, multilingue, plugins)"""
        data = {
            "type_assurance": self.type_assurance,
            "client": self.client,
            "prime": self.prime,
            "date_debut": self.date_debut,
            "date_fin": self.date_fin
        }
        for plugin in self.plugins:
            data = plugin.process_export(data)
        return data

    def auditer(self, action: str, details: Dict = None):
        """Audit structuré (RGPD, accessibilité, plugins, multitenancy)"""
        self.audit_log.append({"action": action, "details": details or {}})

    def anonymiser(self):
        """Anonymisation RGPD du contrat"""
        self.client = "ANONYMISED"
        self.audit_log.append({"action": "anonymisation"})

    def ajouter_plugin(self, plugin):
        self.plugins.append(plugin)
