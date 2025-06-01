"""
Init du package de tests unitaires pour les services métiers Dihya Coding.

Ce module regroupe tous les tests liés aux services métiers :
- Authentification (auth_service)
- Utilisateurs (user_service)
- Mailing (mail)
- Notifications (notifications)
- OAuth2 (oauth2)
- Templates métiers dynamiques

Bonnes pratiques :
- Isoler chaque test pour éviter les effets de bord.
- Utiliser des fixtures pour simuler les entrées et états critiques.
- Ne jamais inclure de secrets ou de données sensibles dans les tests.
- Documenter chaque test pour faciliter la maintenance et l’audit.
"""