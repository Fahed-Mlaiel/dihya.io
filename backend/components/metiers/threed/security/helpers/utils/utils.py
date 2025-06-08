# utils.py – Utilitaires sécurité

def mask_sensitive(data: str) -> str:
    # Masque les données sensibles pour les logs
    if len(data) <= 4:
        return '*' * len(data)
    return data[:2] + '*' * (len(data)-4) + data[-2:]
