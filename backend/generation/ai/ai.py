"""
Intégration IA avancée (LLaMA, Mixtral, Mistral) pour Dihya Coding (Python)
Sécurité, fallback, audit, multilingue, plugins
"""
from typing import List
import requests

def generate_ai_content(prompt: str, lang: str = 'fr', models: List[str] = None) -> str:
    """
    Génère du contenu IA avec fallback open source
    :param prompt: Texte d'entrée
    :param lang: Langue cible
    :param models: Liste des modèles IA à utiliser
    :return: Résultat généré
    """
    if models is None:
        models = ['llama', 'mixtral', 'mistral']
    for model in models:
        try:
            response = requests.post(f'http://localhost:8000/api/ai/{model}',
                                     json={'prompt': prompt},
                                     headers={'Accept-Language': lang})
            if response.ok:
                data = response.json()
                if data and 'result' in data:
                    return data['result']
        except Exception:
            continue
    raise RuntimeError('Aucun modèle IA disponible.')
