# ai_fallback/ — Fallback IA open source Backend Dihya Coding

Ce dossier permet d’intégrer des modèles d’intelligence artificielle open source (ex : Mixtral, LLaMA, Mistral) pour servir de solution de repli (fallback) locale lorsque les APIs propriétaires (GPT, etc.) sont inaccessibles ou limitées.

---

## Objectif

- Garantir la souveraineté numérique et la continuité de service même en cas de coupure ou de blocage des APIs externes.
- Permettre l’utilisation de modèles IA open source compatibles avec le cahier des charges Dihya Coding.
- Assurer la conformité RGPD (logs anonymisés, purge possible).

---

## Bonnes pratiques

- **Documenter chaque intégration de modèle IA** (licence, version, dépendances, limitations).
- **Sécuriser les échanges** avec les modèles (pas de fuite de données sensibles, prompts jamais loggés).
- **Logger chaque appel** à un fallback IA (horodatage, utilisateur, modèle, statut, jamais de prompt).
- **Prévoir un mécanisme de sélection automatique** du backend IA selon la disponibilité (fallback transparent et priorisé).
- **Respecter les licences open source** des modèles utilisés.
- **Tester la robustesse et la performance** de chaque fallback.
- **Permettre la purge et l’export des logs** (conformité RGPD).

---

## Fonctionnalités

- Orchestration automatique entre plusieurs modèles fallback (Mixtral, LLaMA, Mistral…)
- Validation stricte des prompts et des sorties
- Logging structuré et anonymisé de chaque appel (voir `models.py`)
- Modularité : chaque modèle est un wrapper indépendant, facile à mettre à jour ou remplacer
- Extensibilité : ajout de nouveaux modèles ou backends possible sans casser l’existant

---

## Exemple d’utilisation

```python
from app.ai_fallback.models import generate_with_fallback

code, preview_url = generate_with_fallback(
    prompt="Explique le concept de souveraineté numérique.",
    project_type="webapp",
    stack="flask",
    user="user_123"
)
````

# Fallback IA Backend – Dihya Coding

Ce dossier gère les mécanismes de fallback IA : sécurité, RGPD, accessibilité, audit, CI/CD, multilingue, documentation, plugins.

## Bonnes pratiques
- Sécurité, validation, audit, logs, documentation, accessibilité, RGPD, CI/CD
- Exemples d’utilisation, guides intégrés, multilingue, plugins

---
Production-ready, sécurisé, conforme, extensible, documenté, multilingue, CI/CD, RGPD, accessibilité.
