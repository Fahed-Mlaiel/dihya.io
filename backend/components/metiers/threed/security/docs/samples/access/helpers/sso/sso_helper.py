# sso_helper.py
# Helper avancé pour l’intégration SSO (Single Sign-On)

def initiate_sso_login(provider, callback_url):
    """Simule l’initiation d’un login SSO"""
    return {
        'url': f'https://sso.{provider}.com/login?redirect={callback_url}',
        'provider': provider,
        'initiatedAt': __import__('datetime').datetime.utcnow().isoformat()
    }
