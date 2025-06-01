"""
Init du package de tests unitaires pour l’API plugins Dihya Coding.

Ce module permet de regrouper tous les tests liés à la gestion des plugins :
- Sécurité (authentification, rôle admin)
- Validation des payloads
- Ajout, suppression, activation/désactivation de plugins
- Robustesse et conformité métier

Bonnes pratiques :
- Isoler chaque test pour éviter les effets de bord.
- Utiliser des fixtures pour simuler les utilisateurs et l’état des plugins.
- Ne jamais inclure de secrets ou de données sensibles dans les tests.
"""