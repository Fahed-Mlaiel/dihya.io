"""
Script Python pour générer automatiquement des checklists de documentation
legacy Seo.
Conforme au cahier des charges, extensible, prêt à l’emploi.
"""


def generate_checklist(items):
    print("Checklist générée :")
    for item in items:
        print(f"- [ ] {item}")


if __name__ == "__main__":
    items = [
        "Documentation technique complète",
        "Documentation fonctionnelle complète",
        "Modèles de guides prêts à l’emploi",
        "Changelog documenté",
        "Accessibilité et multilingue",
    ]
    generate_checklist(items)
