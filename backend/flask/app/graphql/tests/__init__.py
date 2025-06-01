"""
Init du package de tests unitaires pour les resolvers GraphQL de Dihya Coding.

Ce module regroupe tous les tests liés aux resolvers GraphQL :
- Validation des arguments et des schémas
- Sécurité des accès (rôles, permissions)
- Conformité des réponses (pas de fuite de données sensibles)
- Robustesse face aux erreurs et cas limites

Bonnes pratiques :
- Isoler chaque test pour éviter les effets de bord.
- Utiliser des fixtures pour simuler le contexte utilisateur.
- Ne jamais inclure de secrets ou de données sensibles dans les tests.
- Documenter chaque test pour faciliter la maintenance et l’audit.
"""

# Dieses __init__.py stellt sicher, dass das Verzeichnis als Python-Paket erkannt wird.
