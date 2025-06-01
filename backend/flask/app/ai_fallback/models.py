"""
Gestion des modèles IA open source de fallback pour Dihya Coding.

Ce module permet d’intégrer et d’orchestrer des modèles open source (Mixtral, LLaMA, Mistral, etc.)
en cas de quota dépassé ou d’indisponibilité des API propriétaires (OpenAI, etc.).

Bonnes pratiques :
- Ne jamais exposer de prompts ou de données sensibles dans les logs ou erreurs.
- Logger chaque appel à un modèle fallback avec horodatage, utilisateur, type de génération et statut.
- Prévoir une validation stricte des entrées et sorties.
- Modulariser chaque wrapper de modèle pour faciliter l’ajout ou la mise à jour.
- Documenter chaque modèle supporté et ses limitations.
- Respecter la conformité RGPD (logs anonymisés, purge possible).
"""

import os
from datetime import datetime
from typing import Tuple, Optional

FALLBACK_LOG_FILE = os.path.join(
    os.path.dirname(__file__), "../../logs/ai_fallback.log"
)

def log_fallback_call(user: Optional[str], model: str, status: str, details: str = ""):
    """
    Logge chaque appel à un modèle IA fallback.

    Args:
        user (str): ID utilisateur ou 'anonymous'.
        model (str): Nom du modèle utilisé.
        status (str): "SUCCESS" ou "FAIL".
        details (str): Détails additionnels (jamais de prompt ni de données sensibles).
    """
    entry = (
        f"{datetime.utcnow().isoformat()} | user={user or 'anonymous'} | "
        f"model={model} | status={status} | {details}"
    )
    try:
        with open(FALLBACK_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    except Exception:
        pass  # Ne jamais faire échouer la génération pour un problème de log

def validate_prompt(prompt: str) -> bool:
    """
    Valide le prompt utilisateur (sécurité, longueur, contenu).

    Args:
        prompt (str): Prompt utilisateur.

    Returns:
        bool: True si valide, False sinon.
    """
    if not prompt or len(prompt) < 10 or len(prompt) > 2000:
        return False
    # Ajouter ici d'autres règles de validation si besoin
    return True

def generate_with_mixtral(prompt: str, project_type: str, stack: str) -> Tuple[str, str]:
    """
    Génère du code avec Mixtral (exemple fictif).

    Args:
        prompt (str): Prompt utilisateur validé.
        project_type (str): Type de projet (webapp, mobile, etc.).
        stack (str): Stack technique demandée.

    Returns:
        tuple: (code généré, url de preview)
    """
    # TODO: Intégrer l’appel réel au modèle Mixtral local ou API
    code = f"# Code généré par Mixtral pour {project_type} ({stack})\n# Prompt: {prompt}"
    preview_url = "https://preview.dihya.dev/mixtral_demo"
    return code, preview_url

def generate_with_llama(prompt: str, project_type: str, stack: str) -> Tuple[str, str]:
    """
    Génère du code avec LLaMA (exemple fictif).

    Args:
        prompt (str): Prompt utilisateur validé.
        project_type (str): Type de projet.
        stack (str): Stack technique.

    Returns:
        tuple: (code généré, url de preview)
    """
    # TODO: Intégrer l’appel réel au modèle LLaMA local ou API
    code = f"# Code généré par LLaMA pour {project_type} ({stack})\n# Prompt: {prompt}"
    preview_url = "https://preview.dihya.dev/llama_demo"
    return code, preview_url

def generate_with_mistral(prompt: str, project_type: str, stack: str) -> Tuple[str, str]:
    """
    Génère du code avec Mistral (exemple fictif).

    Args:
        prompt (str): Prompt utilisateur validé.
        project_type (str): Type de projet.
        stack (str): Stack technique.

    Returns:
        tuple: (code généré, url de preview)
    """
    # TODO: Intégrer l’appel réel au modèle Mistral local ou API
    code = f"# Code généré par Mistral pour {project_type} ({stack})\n# Prompt: {prompt}"
    preview_url = "https://preview.dihya.dev/mistral_demo"
    return code, preview_url

def generate_with_mlx(prompt: str, project_type: str, stack: str) -> Tuple[str, str]:
    """
    Génère du code avec MLX (exemple fictif, wrapper extensible Apple Silicon/CPU).

    Args:
        prompt (str): Prompt utilisateur validé.
        project_type (str): Type de projet.
        stack (str): Stack technique.

    Returns:
        tuple: (code généré, url de preview)
    """
    # TODO: Intégrer l’appel réel au modèle MLX local ou API (Apple Silicon, CPU, etc.)
    code = f"# Code généré par MLX pour {project_type} ({stack})\n# Prompt: {prompt}"
    preview_url = "https://preview.dihya.dev/mlx_demo"
    return code, preview_url

def generate_with_fallback(
    prompt: str, project_type: str, stack: str, user: Optional[str] = "anonymous"
) -> Tuple[str, str]:
    """
    Orchestration : tente chaque modèle open source jusqu’à succès.

    Args:
        prompt (str): Prompt utilisateur (sera validé).
        project_type (str): Type de projet.
        stack (str): Stack technique.
        user (str, optional): ID utilisateur pour la traçabilité.

    Returns:
        tuple: (code généré, url de preview)
    """
    if not validate_prompt(prompt):
        log_fallback_call(user, "N/A", "FAIL", "Prompt invalide")
        return "# Erreur : prompt invalide ou trop court.", ""

    for model_func, model_name in [
        (generate_with_mixtral, "Mixtral"),
        (generate_with_llama, "LLaMA"),
        (generate_with_mistral, "Mistral"),
        (generate_with_mlx, "MLX"),
    ]:
        try:
            code, preview_url = model_func(prompt, project_type, stack)
            log_fallback_call(user, model_name, "SUCCESS")
            return code, preview_url
        except Exception as e:
            log_fallback_call(user, model_name, "FAIL", str(e))
    # Si aucun modèle ne fonctionne
    log_fallback_call(user, "ALL", "FAIL", "Aucun modèle fallback disponible")
    return "# Erreur : aucun modèle fallback disponible.", ""
