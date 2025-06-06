# Main Banque & Finance
# Correction de l'import circulaire pour compatibilité tests et exécution
from .banque_finance import BanqueFinance
if __name__ == '__main__':
    compte = BanqueFinance('FR123456789', 1000)
    print('Solde initial:', compte.solde)
    compte.virement(500)
    print('Après virement:', compte.solde)
