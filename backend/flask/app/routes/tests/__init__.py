"""
Init du package de tests unitaires pour les routes de génération Dihya Coding.

Ce module regroupe tous les tests liés à la route /api/generate :
- Validation des entrées (spécification, type de projet)
- Sécurité (authentification, rôles)
- Robustesse de la génération (succès, erreurs, edge cases)
- Conformité métier et non-fuite de données sensibles

Bonnes pratiques :
- Isoler chaque test pour éviter les effets de bord.
- Utiliser des fixtures pour simuler les utilisateurs et les payloads.
- Ne jamais inclure de secrets ou de données sensibles dans les tests ou les réponses.
- Documenter chaque test pour faciliter la maintenance et l’audit.
"""