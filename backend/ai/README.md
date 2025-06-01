# README – Dihya Backend AI

Ce dossier contient tous les modules backend IA de Dihya : génération automatique, NLP, ML, fallback open source, intégration LLM, sécurité, audit, tests, plugins, multilingue, RGPD.

## 🌍 Multilingue & Souveraineté
- API et logs multilingues (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Fallback IA open source (Ollama, Mixtral, LLaMA, Mistral)
- Prêt pour cloud souverain, Codespaces, Linux, CI/CD

## 🔒 Sécurité & RGPD
- CORS, JWT, validation, audit, WAF, anti-DDOS, RBAC, logs structurés
- Conformité RGPD/NIS2, anonymisation, exportabilité, auditabilité

## 🧩 Modularité & Extensibilité
- Plugins dynamiques (API/CLI), multitenancy, gestion des rôles (admin, user, invité)
- REST & GraphQL-ready, endpoints testés, documentation intégrée

## 📦 Structure du dossier
- `__init__.py` : initialisation du module IA backend
- `ai.py` : moteur IA principal (Flask, fallback open source, sécurité, audit, multilingue)
- `main.py` : entrypoint Flask, prêt CI/CD, Codespaces, production
- `views.py` : vues avancées, REST/GraphQL-ready, sécurité, plugins
- `schemas.py` : schémas Pydantic/GraphQL, typés, multilingues, RGPD-ready
- `urls.py` : définition des routes API (Flask/Django/GraphQL)
- `tests.py` : tests unitaires, intégration, e2e, audit, sécurité, multilingue
- `plugins.py` : système de plugins IA backend, extensible, RGPD
- `audit.py` : audit structuré, logs, export, anonymisation, conformité
- `i18n.py` : internationalisation dynamique, 13 langues supportées

## 🚀 Exemples d’intégration
- Flask : `from Dihya.backend.ai import ai_bp`
- Django : `urlpatterns = [path('api/ai/', include('Dihya.backend.ai.urls'))]`
- GraphQL : brancher le schéma sur `/api/ai/graphql`

## 🧪 Tests & Qualité
- Couverture maximale (unit, integration, e2e, audit, RGPD, accessibilité)
- Aucun warning, fail CI, fail lint, fail test, fail build, fail doc, fail accessibilité, fail sécurité, fail SEO

## 📚 Documentation
- Voir `/docs/API_REFERENCE_*.md`, `/docs/ARCHITECTURE_DIAGRAM.png`, `/docs/LEGAL_COMPLIANCE.md`
- Pour contribuer, voir `/CONTRIBUTING.md` et `/PLUGINS_GUIDE.md`

---

🇫🇷, 🇬🇧, 🇦🇪, ⵣ – Documentation multilingue, accessible, souveraine, production-ready.
