"""
Blueprint documentation Integration Guide (Python)
Génération de guides d’intégration dynamiques, exemples d’appel API, doc front-end/back-end, instructions d’extension.
"""
def generate_integration_guide(api_url: str, examples: dict) -> str:
    """
    Génère un guide d’intégration complet avec exemples d’appel API (curl, Python, JS).
    """
    guide = f"""
# Guide d’intégration API

Base URL : {api_url}

## Exemples d’appel

### curl
curl -X GET {api_url}/assets

### Python
import requests
resp = requests.get('{api_url}/assets')
print(resp.json())

### JavaScript
fetch('{api_url}/assets').then(r => r.json()).then(console.log)

"""
    for k, v in examples.items():
        guide += f"\n## {k}\n{v}\n"
    return guide

# Exemple d'utilisation :
# print(generate_integration_guide("https://api.exemple.com", {}))
