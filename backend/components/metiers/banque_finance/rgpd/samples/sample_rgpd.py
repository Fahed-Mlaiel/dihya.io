# sample_rgpd.py – Exemple RGPD avancé (Python)
sample = {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "anonymized": False,
    "masked": False,
}

def anonymize_sample(sample):
    """Retourne une version anonymisée du sample RGPD pour les tests métier Banque_Finance."""
    anonymized = sample.copy()
    anonymized["email"] = None
    anonymized["anonymized"] = True
    return anonymized

# Convention : tout exemple RGPD doit être utilisé dans un test réel et documenté.
