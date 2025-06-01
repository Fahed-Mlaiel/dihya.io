"""
Init du package de tests unitaires pour les wrappers IA fallback de Dihya Coding.

Ce module regroupe tous les tests liés aux modèles IA fallback :
- Sélection dynamique du modèle (Mixtral, LLaMA, Mistral, etc.)
- Gestion des quotas et fallback automatique
- Robustesse des réponses générées
- Sécurité (aucune fuite de prompts ou de données sensibles)

Bonnes pratiques :
- Isoler chaque test pour éviter les effets de bord.
- Utiliser des fixtures pour simuler les prompts et états de quota.
- Ne jamais inclure de secrets ou de données sensibles dans les tests ou les réponses.
- Documenter chaque test pour faciliter la maintenance et l’audit.
"""