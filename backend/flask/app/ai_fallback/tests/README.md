# ai_fallback/tests — Tests unitaires des wrappers IA fallback Dihya Coding

Ce dossier contient les tests unitaires pour les wrappers IA fallback du backend Dihya Coding (Mixtral, LLaMA, Mistral, etc.).

## Objectif

- Vérifier la sélection dynamique du modèle IA selon la disponibilité et les quotas.
- Garantir la robustesse des réponses générées par chaque wrapper.
- Tester la gestion des quotas et le fallback automatique en cas de dépassement.
- Prévenir toute fuite de prompts ou de données sensibles dans les réponses.

## Bonnes pratiques

- Isoler chaque test pour éviter les effets de bord (utiliser des fixtures pour les prompts et les états de quota).
- Couvrir tous les cas critiques : sélection du modèle, quotas, erreurs, edge cases.
- Ne jamais inclure de secrets ou de données sensibles dans les tests ou les réponses.
- Documenter chaque test avec une docstring claire.
- Simuler différents scénarios de quota et de disponibilité des modèles.

## Exemple d’exécution

```bash
pytest app/ai_fallback/tests/