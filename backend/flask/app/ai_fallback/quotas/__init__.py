"""
Module de gestion des quotas API et de la redirection fallback IA pour Dihya Coding.

Ce package permet de surveiller l’utilisation des APIs propriétaires (GPT, etc.),
de détecter les dépassements de quotas et de rediriger automatiquement les requêtes
vers les modèles IA open source (Mixtral, LLaMA, etc.) en fallback.

Bonnes pratiques :
- Journaliser chaque dépassement de quota et chaque bascule en fallback.
- Ne jamais exposer de données sensibles lors de la gestion des quotas.
- Prévoir une configuration souple des seuils de quotas et des priorités de fallback.
- Tester la robustesse du mécanisme de redirection.

Exemple d’utilisation :
    from backend.flask.app.ai_fallback.quotas import check_and_route

    response = check_and_route(prompt, lang="fr")

"""

import os
from datetime import datetime

# Exemple de seuils de quotas (à adapter selon l’API)
QUOTA_LIMIT = int(os.getenv("GPT_API_QUOTA_LIMIT", "1000"))
QUOTA_USED = 0  # À remplacer par une persistance réelle

def check_and_route(prompt, lang="fr"):
    """
    Vérifie le quota restant et route la requête vers l’API propriétaire ou le fallback IA.
    :param prompt: Texte à traiter
    :param lang: Langue cible
    :return: Réponse IA (propriétaire ou fallback)
    """
    global QUOTA_USED
    if QUOTA_USED >= QUOTA_LIMIT:
        log_quota_event("fallback", prompt)
        from backend.flask.app.ai_fallback import get_fallback_response
        return get_fallback_response(prompt, lang=lang)
    else:
        QUOTA_USED += 1
        log_quota_event("proprietary", prompt)
        # TODO: Appeler ici l’API propriétaire (ex: GPT)
        return f"[Réponse API propriétaire simulée pour : {prompt}]"

def log_quota_event(route_type, prompt):
    """
    Journalise chaque utilisation ou fallback pour audit.
    """
    log_entry = f"{datetime.utcnow().isoformat()} | {route_type.upper()} | {prompt[:50]}"
    log_file = os.getenv("QUOTA_LOG_FILE", "logs/quotas.log")
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_entry + "\n")

def check_quota(user):
    """
    Simule la vérification du quota IA pour un utilisateur.
    Retourne True si quota disponible, False sinon.
    """
    # TODO: Logik anpassen, hier immer True für Demo
    return True

def use_fallback_ai(spec, project_type, stack):
    """
    Simule le fallback IA open source.
    Retourne (code, preview_url)
    """
    return {"main.py": "# code demo"}, "https://dihya.ai/preview/demo"
