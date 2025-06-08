# api_samples.py – Exemples d’intégration API (Python)
def sample_api_request():
    return {
        'method': 'POST',
        'url': '/api/secure-endpoint',
        'headers': {'Authorization': 'Bearer <token>'},
        'body': {'data': 'example'}
    }
