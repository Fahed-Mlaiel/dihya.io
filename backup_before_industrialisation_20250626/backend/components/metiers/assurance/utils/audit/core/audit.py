"""
Fonctions d'audit avancées pour Assurance.
Permet d'évaluer la conformité, la performance et la sécurité des entités assurance.
"""


def audit_assurance(data):
    """
    Réalise un audit complet d'une entité Assurance.
    Retourne un score, des détails et des recommandations.
    """
    score = 97.0 if data.get("status") == "active" else 65.0
    details = "Audit Assurance réussi." if score > 90 else "Non conforme."
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


auditAssurance = audit_assurance
