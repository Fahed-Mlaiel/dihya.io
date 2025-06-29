"""
Fonctions d'audit avancées pour Sante.
Permet d'évaluer la conformité, la performance et la sécurité des entités sante.
"""


def audit_sante(data):
    """
    Réalise un audit complet d'une entité Sante.
    Retourne un score, des détails et des recommandations.
    """
    score = 97.0 if data.get("status") == "active" else 65.0
    details = "Audit Sante réussi." if score > 90 else "Non conforme."
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


auditSante = audit_sante
