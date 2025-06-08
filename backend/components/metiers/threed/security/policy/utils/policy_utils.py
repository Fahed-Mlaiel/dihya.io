# policy_utils.py – Utilitaires pour politiques sécurité

def describe_policy(model):
    return f"Politique: {model['name']} (v{model['version']}) – Règles: {', '.join(model['rules'])}"
