# Guide Frontend – Dihya Coding

Ce guide explique comment développer, tester, sécuriser et déployer le frontend de Dihya Coding, en respectant l’accessibilité, la sécurité, l’internationalisation et la performance.

## Stack
- React (Next.js), TypeScript, TailwindCSS, i18next, Axios, ESLint, Prettier
- Compatible Linux, Codespaces, CI/CD, Docker

## Installation
```bash
cd frontend
npm install
npm run dev
```

## Sécurité
- CORS strict, CSP, XSS/CSRF protection, JWT, audit logging
- Respect des rôles (admin, user, invité)

## Internationalisation
- i18next, fichiers `/i18n/` (fr, en, ar, de, etc.)
- Changement dynamique de langue, fallback automatique

## Accessibilité
- Respect WCAG 2.1 AA, navigation clavier, ARIA, contrastes
- Audit via axe, Lighthouse, tests automatisés

## SEO
- balises meta dynamiques, sitemap, robots.txt, logs structurés

## Tests
- Unitaire : Jest, React Testing Library
- E2E : Cypress (voir `INTEGRATION_TESTS_GUIDE.md`)

## Déploiement
- Docker, GitHub Actions, Vercel, fallback local

## Bonnes pratiques
- Modularité, composants réutilisables, hooks custom
- Documentation (Storybook, docstring, types)
- Respect du style (`CODE_STYLE.md`)

---

Pour toute question, voir les guides d’intégration et contacter les mainteneurs.
