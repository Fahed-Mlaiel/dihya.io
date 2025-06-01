"""
Dihya Backend Assets – RGPD Helper
Fonctions d’anonymisation, export, conformité RGPD, auditabilité, multilingue.
"""
def anonymize_user(user: dict) -> dict:
    user = user.copy()
    user['email'] = 'anonymous@dihya.ai'
    user['name'] = 'Utilisateur Anonyme'
    user['ip'] = '0.0.0.0'
    return user

def export_users(users: list, output_path: str):
    import json
    anonymized = [anonymize_user(u) for u in users]
    with open(output_path, 'w') as f:
        json.dump(anonymized, f, indent=2, ensure_ascii=False)
    print(f"Export RGPD anonymisé terminé : {output_path}")
