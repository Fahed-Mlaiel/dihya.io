def ai_fallback(prompt):
    # Fallback IA minimal pour compatibilité, à surcharger par la logique métier avancée
    return {'status': 'fallback', 'result': f'Fallback IA: {prompt[:32]}...'}
