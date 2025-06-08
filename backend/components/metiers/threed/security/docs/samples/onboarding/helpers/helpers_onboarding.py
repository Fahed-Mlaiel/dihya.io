# helpers_onboarding.py
# Helpers avancés pour le parcours utilisateur, sécurité à l’entrée

from datetime import datetime

def start_onboarding(user):
    """Simule le début d'un onboarding sécurisé"""
    user = dict(user)
    user['onboardingStarted'] = True
    user['startedAt'] = datetime.utcnow().isoformat()
    return user

def complete_onboarding(user):
    """Simule la complétion d'un onboarding"""
    user = dict(user)
    user['onboardingCompleted'] = True
    user['completedAt'] = datetime.utcnow().isoformat()
    return user
