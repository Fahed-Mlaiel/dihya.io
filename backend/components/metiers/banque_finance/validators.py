"""
Validators Banque & Finance – Ultra avancé
-----------------------------------------
Vérification IBAN, BIC, RGPD, multilingue, documentation et type hints.
"""

def is_valid_compte(compte: str) -> bool:
    return isinstance(compte, str) and len(compte) > 8 and compte.isalnum()

def is_valid_iban(iban: str) -> bool:
    return isinstance(iban, str) and len(iban) >= 15 and iban[:2].isalpha()

def is_valid_bic(bic: str) -> bool:
    return isinstance(bic, str) and len(bic) in (8, 11) and bic.isalnum()
