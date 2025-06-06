# Sample util Education

def generer_email_utilisateur(utilisateur):
    """Génère un email personnalisé pour un utilisateur Education."""
    return f"Bonjour {utilisateur.prenom} {utilisateur.nom}, bienvenue sur la plateforme Education."

def generer_rapport_evaluation(evaluation):
    """Génère un rapport structuré pour une évaluation."""
    return f"Rapport: {evaluation.utilisateur_id} a obtenu {evaluation.note}/20 le {evaluation.date}"

def anonymiser_utilisateur(utilisateur):
    """Anonymise les données utilisateur pour RGPD."""
    return {
        **utilisateur.dict(),
        'email': 'anonymized@domain.tld',
        'nom': 'Anonyme',
        'prenom': 'Anonyme'
    }

def log_structured(event, data):
    """Log structuré pour audit et conformité."""
    import json
    import datetime
    print(json.dumps({"event": event, "data": data, "date": datetime.datetime.now().isoformat()}))
