# rgpd_sample.py – Exemple RGPD ultra avancé


def rgpd_sample(user):
    """Simule un export RGPD legacy administration_publique"""
    # ... logique RGPD avancée ...
    from datetime import datetime

    return {
        "user": user,
        "export": True,
        "date": datetime.utcnow().isoformat(),
    }
