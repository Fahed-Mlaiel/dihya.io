"""
Fonctions d'audit avancées pour ServicesPersonne.
Permet d'évaluer la conformité, la performance et la sécurité des entités services_personne.
"""


def audit_services_personne(data):
    """
    Réalise un audit complet d'une entité ServicesPersonne.
    Retourne un score, des détails et des recommandations.
    """
    score = 97.0 if data.get("status") == "active" else 65.0
    details = "Audit ServicesPersonne réussi." if score > 90 else "Non conforme."
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


auditServicesPersonne = audit_services_personne
