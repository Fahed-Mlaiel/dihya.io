"""
CI/CD DevOps threed (Python)
"""


def run_pipeline(env: str):
    print(f"Pipeline lancé pour l'environnement {env}")
    return True


def deploy_to_env(env: str):
    print(f"Déploiement sur {env} terminé.")
    return True
