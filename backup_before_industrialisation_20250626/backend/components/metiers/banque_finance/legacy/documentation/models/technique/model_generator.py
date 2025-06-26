"""
Script Python pour générer un modèle de documentation legacy Banque_Finance.
Ultra avancé, conforme au cahier des charges.
"""


def generate_model(name, fields):
    print(f"# Modèle : {name}\n")
    for field in fields:
        print(f"- {field}")


if __name__ == "__main__":
    name = "Documentation technique"
    fields = [
        "Titre",
        "Résumé",
        "Architecture",
        "API",
        "Sécurité",
        "Déploiement",
        "Maintenance",
    ]
    generate_model(name, fields)
