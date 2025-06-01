# Dihya Coding – Guide de Déploiement

## Table des matières
- [Introduction](#introduction)
- [Prérequis](#prérequis)
- [Déploiement GitHub Actions](#déploiement-github-actions)
- [Déploiement Docker](#déploiement-docker)
- [Déploiement Kubernetes (K8s)](#déploiement-kubernetes-k8s)
- [Fallback local](#fallback-local)
- [Sécurité & RGPD](#sécurité--rgpd)
- [Internationalisation](#internationalisation)
- [Tests & Monitoring](#tests--monitoring)
- [SEO & Accessibilité](#seo--accessibilité)
- [Plugins & Extensibilité](#plugins--extensibilité)
- [FAQ Déploiement](#faq-déploiement)

---

## Introduction
Ce guide décrit comment déployer Dihya Coding en production, démo ou développement, avec sécurité maximale, conformité RGPD, accessibilité, SEO, plugins, i18n, audit, CI/CD, fallback IA open source.

## Prérequis
- Docker, Docker Compose, Python 3.11+, Node.js 20+, pip, npm, kubectl, helm
- Accès à un cluster K8s (optionnel)
- Accès à GitHub Actions (optionnel)
- Variables d’environnement sécurisées (voir `.env.example`)

## Déploiement GitHub Actions
- CI/CD automatisé (lint, tests, build, scan sécurité, déploiement)
- Secrets chiffrés dans GitHub
- Workflows pour Docker, K8s, fallback local
- Exemples : `.github/workflows/`

## Déploiement Docker
- `docker-compose up -d` pour un déploiement local ou cloud
- Images optimisées, sécurité renforcée (user non-root, CORS, WAF, audit)
- Volumes pour la persistance, logs structurés, backup automatisé

## Déploiement Kubernetes (K8s)
- Helm charts fournis (`/k8s/`)
- Sécurité : RBAC, NetworkPolicy, secrets, audit, monitoring Prometheus/Grafana
- Multi-tenant, plugins, i18n, fallback IA

## Fallback local
- `make run-local` ou `python manage.py runserver` (Django), `npm run dev` (Node)
- Sécurité, i18n, plugins, RGPD, auditabilité maintenus

## Sécurité & RGPD
- CORS, JWT, WAF, anti-DDOS, audit, anonymisation, logs structurés, export RGPD
- Conformité RGPD, auditabilité, accès exportable, suppression, consentement

## Internationalisation
- 13 langues supportées, détection automatique, fallback multilingue

## Tests & Monitoring
- `pytest`, `jest`, `docker-compose exec ... pytest`/`npm test`
- Monitoring Prometheus, Grafana, alertes, logs structurés

## SEO & Accessibilité
- robots.txt, sitemap.xml dynamique, headers SEO, tests accessibilité (axe, pa11y, lighthouse)

## Plugins & Extensibilité
- Ajout de plugins via API ou CLI, audit, sécurité, i18n

## FAQ Déploiement
- Voir [FAQ.md](FAQ.md) pour les questions fréquentes

---

## English version
See below for the English deployment guide (multilingual support, fallback, security, CI/CD, plugins, RGPD, SEO, accessibility, monitoring, tests, multi-stack).

...
