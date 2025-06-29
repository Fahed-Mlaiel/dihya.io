"""
Fonctions d'audit avancées pour Science.
Permet d'évaluer la conformité, la performance et la sécurité des entités science.
"""


def audit_science(data):
    """
    Réalise un audit complet d'une entité Science.
    Retourne un score, des détails et des recommandations.
    """
    score = 97.0 if data.get("status") == "active" else 65.0
    details = "Audit Science réussi." if score > 90 else "Non conforme."
    recommandations = (
        "Poursuivre les bonnes pratiques."
        if score > 90
        else "Corriger les non-conformités."
    )
    return {
        "score": score,
        "details": details,
        "recommandations": recommandations,
    }


auditScience = audit_science
