# Dihya Coding — Frontend

Ce dossier contient le frontend de la plateforme Dihya Coding : interface moderne, générateur de projets, UI/UX responsive, SEO, sécurité, conformité RGPD, extensibilité et documentation claire.

---

## Objectifs

- Offrir une interface utilisateur intelligente, accessible et multilingue (support dialectes).
- Permettre la génération automatique de projets (web, mobile, IA, DevOps, blockchain) à partir d’un cahier des charges écrit ou vocal.
- Garantir un design moderne, responsive, inspiré de la culture amazigh et personnalisable.
- Assurer la sécurité, la conformité RGPD, l’auditabilité et la souveraineté des données.
- Faciliter l’extensibilité via plugins, templates, thèmes et architecture modulaire.

---

## Bonnes pratiques

- **Design moderne** : React, Tailwind CSS, composants réutilisables, responsive, thèmes personnalisés.
- **SEO** : balises meta dynamiques, sitemap, robots.txt, manifest, composant SEO dédié.
- **Sécurité** : validation/sanitation côté client, gestion JWT/OAuth, anti-XSS, CORS, gestion des rôles.
- **RGPD** : consentement cookies, anonymisation, export/purge des données utilisateur, documentation claire.
- **Extensibilité** : architecture ouverte pour plugins, templates, thèmes, multilingue.
- **Auditabilité** : logs front (actions critiques), traçabilité des générations, monitoring UX.
- **Documentation** : chaque composant, hook, feature et page doit être documenté (docstring, README, guides).

---

## Structure recommandée
frontend/
├── public/ 
│   ├── SEO, manifest, favicon, robots.txt, sitemap.xml
frontend/ ├── public/ # Référencement (SEO), manifeste, favicon, robots.txt, sitemap.xml ├── src/ │ ├── assets/ # Images, icônes, illustrations │ ├── components/ # Composants réutilisables (Navbar, Footer, Référencement, etc.) │ ├── layout/ # Dispositions globales (MainLayout, etc.) │ ├── pages/ # Pages principales (Accueil, Génération, Aperçu, Authentification, etc.) │ ├── styles/ # Configuration Tailwind, CSS global │ ├── features/ # Logique métier (génération, authentification, IA, plugins) │ ├── contexts/ # Contextes React (authentification, langue, thème) │ ├── hooks/ # Hooks personnalisés (useAuth, useAI, useTheme) │ ├── utils/ # Fonctions utilitaires (API, validation, sécurité) │ ├── api/ # Appels API (génération, authentification, etc.) │ ├── i18n/ # Multilingue (locales, gestion dynamique) │ └── tests/ # Tests unitaires et end-to-end └── docs/ # Documentation utilisateur et développeur
│   ├── assets/ 
│   │   ├── Images, icônes, illustrations
│   ├── components/ 
│   │   ├── UI réutilisable (Navbar, Footer, SEO, etc.)
│   ├── layout/ 
│   │   ├── Layouts globaux (MainLayout, etc.)
│   ├── pages/ 
│   │   ├── Pages principales (Home, Generate, Preview, Auth, etc.)
│   ├── styles/ 
│   │   ├── Tailwind config, CSS global
│   ├── features/ 
│   │   ├── Logique métier (génération, auth, IA, plugins)
│   ├── contexts/ 
│   │   ├── Contextes React (auth, langue, thème)
│   ├── hooks/ 
│   │   ├── Hooks personnalisés (useAuth, useAI, useTheme)
│   ├── utils/ 
│   │   ├── Fonctions utilitaires (API, validation, sécurité)
│   ├── api/ 
│   │   ├── Appels API (génération, auth, etc.)
│   ├── i18n/ 
│   │   ├── Multilingue (locales, gestion dynamique)
│   └── tests/ 
│       ├── Tests unitaires et e2e
└── docs/ 
	├── Documentation utilisateur et dev
Voici une structure recommandée pour organiser le frontend du projet.


## Fonctionnalités principales

- **Génération de projet** : page Generate (texte libre, vocal, options stack), assistant IA, preview live, partage.
- **Authentification & rôles** : JWT/OAuth, gestion des rôles (admin, user, invité), pages Login/Register/Profile.
- **Multilingue** : gestion dynamique des langues, support dialectes, LanguageSwitcher.
- **Plugins & templates** : ajout facile de plugins (analytics, CMS, Stripe…), templates UI par domaine.
- **SEO & accessibilité** : composant SEO, fichiers SEO, respect des standards WCAG.
- **Sécurité & RGPD** : validation/sanitation, consentement cookies, export/purge, logs anonymisés.
- **Extensibilité** : architecture modulaire, hooks, contextes, thèmes personnalisés.
- **Tests & auditabilité** : tests unitaires/e2e, logs front, monitoring UX.

---

## Documentation

- **/docs/dev_guide.md** : guide développeur (architecture, bonnes pratiques, sécurité, RGPD, extensibilité)
- **/docs/user_guide.md** : guide utilisateur (parcours, génération, preview, export)
- **/docs/architecture.md** : architecture détaillée du frontend
- Chaque composant, page, feature : docstring et commentaires explicatifs

---

## Contribution

- Respecter la charte Dihya Coding : sécurité, souveraineté, conformité RGPD, extensibilité, documentation.
- Documenter chaque évolution, nouvelle feature, plugin ou template.
- Ajouter des tests pour chaque ajout critique (sécurité, génération, auth, plugins).
- Vérifier la conformité SEO, accessibilité, RGPD à chaque évolution.

---

**Pour toute évolution, respecter la sécurité, la souveraineté, la conformité RGPD et la philosophie Dihya Coding.**