# rbac_sample.py – Exemple de RBAC ultra avancé


def rbac_sample(user, role):
    """Simule un contrôle RBAC legacy Culture"""
    # ... logique RBAC avancée ...
    return (
        f"{user} a tous les droits"
        if role == "admin"
        else f"{user} accès restreint"
    )
