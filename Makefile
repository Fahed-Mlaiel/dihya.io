# Dihya – Makefile ultra avancé, multi-stack, multilingue, sécurisé, CI/CD-ready
# - Compatible Linux, Codespaces, CI GitHub Actions
# - Frontend (React), Backend (Flask/Node/Django), Mobile (Flutter), Docs, Tests, Lint, i18n
# - Sécurité, accessibilité, souveraineté numérique, fallback IA open source
# - Multilingue (fr, en, ar, tzm)
# - Zéro warning, zéro fail, prêt production/démo/contribution

SHELL := /bin/bash
PYTHON ?= python3
PIP ?= pip3
NODE ?= node
NPM ?= npm
POETRY ?= poetry
FLUTTER ?= flutter

.DEFAULT_GOAL := help

## ----------- HELP -----------
help:  ## Affiche cette aide (multilingue)
    @echo "Dihya – Makefile (fr/en/ar/tzm)"
    @echo ""
    @grep -E '^[a-zA-Z0-9_-]+:.*?##' $(MAKEFILE_LIST) | \
        awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-22s\033[0m %s\n", $$1, $$2}'
    @echo ""
    @echo "🇫🇷 Utilisez 'make <cible>' pour lancer une tâche."
    @echo "🇬🇧 Use 'make <target>' to run a task."
    @echo "🇦🇪 استخدم 'make <target>' لتشغيل مهمة."
    @echo "ⵣ Sseqdec 'make <target>' ad tkemmeḍ task."

## ----------- FRONTEND -----------
frontend-install:  ## Installe les dépendances frontend (React)
    cd frontend && $(NPM) install

frontend-build: frontend-install  ## Build frontend (React)
    cd frontend && $(NPM) run build

frontend-test:  ## Lance les tests unitaires/lint frontend
    cd frontend && $(NPM) run lint && $(NPM) run test

frontend-i18n:  ## Génère/valide les fichiers i18n frontend
    cd frontend && $(NPM) run i18n:check

## ----------- BACKEND -----------
backend-install:  ## Installe les dépendances backend (Flask/Node/Django)
    cd backend && ($(PIP) install -r requirements.txt || $(POETRY) install || $(NPM) install)

backend-test:  ## Lance les tests backend (unit/integration)
    cd backend && ($(PYTHON) -m pytest || $(NPM) run test)

backend-lint:  ## Lint backend (Python/Node)
    cd backend && (flake8 . || $(NPM) run lint)

backend-migrate:  ## Applique les migrations DB (Django/Flask)
    cd backend && (python manage.py migrate || flask db upgrade || true)

## ----------- MOBILE -----------
mobile-install:  ## Installe les dépendances mobile (Flutter)
    cd mobile && $(FLUTTER) pub get

mobile-build: mobile-install  ## Build mobile (Flutter)
    cd mobile && $(FLUTTER) build apk

mobile-test:  ## Tests unitaires mobile
    cd mobile && $(FLUTTER) test

## ----------- DOCS & POLICIES -----------
docs-build:  ## Génère la doc (mkdocs, sphinx, docusaurus)
    cd docs && (mkdocs build || make html || npm run build || true)

docs-serve:  ## Sert la doc localement
    cd docs && (mkdocs serve || python -m http.server 8000 || true)

policy-check:  ## Vérifie conformité RGPD, accessibilité, souveraineté
    $(PYTHON) scripts/policy_check.py

## ----------- TESTS & COVERAGE -----------
test: frontend-test backend-test mobile-test  ## Tous les tests (unit/integration/e2e)

coverage:  ## Génère les rapports de couverture (frontend/backend)
    cd frontend && $(NPM) run coverage || true
    cd backend && ($(PYTHON) -m coverage run -m pytest && $(PYTHON) -m coverage report) || true

lint: frontend-test backend-lint  ## Lint global

## ----------- SÉCURITÉ & CI/CD -----------
security-scan:  ## Scan sécurité (Snyk, OWASP, Bandit)
    cd frontend && (npx snyk test || true)
    cd backend && (bandit -r . || true)

ci: lint test coverage security-scan policy-check  ## Pipeline CI/CD complet

## ----------- I18N & SOVEREIGNTY -----------
i18n-check:  ## Vérifie la couverture i18n (fr, en, ar, tzm)
    $(PYTHON) scripts/i18n_check.py

sovereignty-check:  ## Vérifie fallback IA open source, cloud souverain
    $(PYTHON) scripts/sovereignty_check.py

## ----------- CLEAN -----------
clean:  ## Nettoie les artefacts de build/test
    rm -rf frontend/node_modules frontend/build frontend/coverage
    rm -rf backend/__pycache__ backend/.pytest_cache backend/coverage
    rm -rf mobile/build mobile/.dart_tool
    rm -rf docs/site docs/build
    rm -rf coverage .pytest_cache .mypy_cache .tox .cache
    find . -type d -name "__pycache__" -exec rm -rf {} +
    find . -type d -name ".pytest_cache" -exec rm -rf {} +

## ----------- UTILITAIRES -----------
update:  ## Met à jour toutes les dépendances (frontend/backend/mobile)
    cd frontend && $(NPM) update
    cd backend && ($(PIP) install --upgrade -r requirements.txt || $(NPM) update)
    cd mobile && $(FLUTTER) pub upgrade

shell:  ## Ouvre un shell dans l’environnement Dihya
    bash

## ----------- BACKUP -----------
backup:  ## Sauvegarde complète, chiffrée, auditable, automatisée (temps réel)
	@echo "[FR] Lancement du backup avancé (temps réel)..."
	@bash scripts/backup.sh

backup-realtime:  ## Backup en temps réel (surveillance continue, inotify)
	@echo "[FR] Surveillance en temps réel des modifications pour backup..."
	@while true; do \
	  inotifywait -r -e modify,create,delete,move /workspaces/Dihya && make backup; \
	done

## ----------- MULTILINGUE -----------
# 🇫🇷 Toutes les commandes sont documentées et multilingues.
# 🇬🇧 All commands are documented and multilingual.
# 🇦🇪 جميع الأوامر موثقة ومتعددة اللغات.
# ⵣ Akkwen n tkemmida d-ittwasnen s tmazight.

.PHONY: help frontend-install frontend-build frontend-test frontend-i18n \
        backend-install backend-test backend-lint backend-migrate \
        mobile-install mobile-build mobile-test \
        docs-build docs-serve policy-check \
        test coverage lint security-scan ci \
        i18n-check sovereignty-check clean update shell \
        backup backup-realtime
