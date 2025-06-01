# Template Mobile Dihya

Ce template fournit une base avancée pour la génération de projets mobiles (Flutter, React Native, Kotlin, Swift, etc.) avec :
- Sécurité maximale (auth, CORS, validation, audit, WAF, anti-DDOS)
- Internationalisation dynamique (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Multitenancy, gestion des rôles (admin, user, invité)
- Plugins extensibles (API/CLI)
- Conformité RGPD, auditabilité, anonymisation, logs exportables
- Tests complets (unit, integration, e2e)
- Déploiement GitHub Actions, Docker, K8s, fallback local
- Code 100% compatible Codespaces/Linux/CI

## Utilisation
1. Copier le template et adapter `template.py` selon le framework mobile choisi.
2. Personnaliser la configuration de sécurité et d'i18n.
3. Ajouter vos plugins ou modules métier.
4. Lancer les tests :
   ```bash
   pytest test_mobile.py
   ```
5. Déployer via Docker/K8s ou CI/CD.

## Personnalisation
- Ajoutez vos écrans, API, hooks plugins, etc.
- Voir `policy.md` pour les exigences de conformité et sécurité.

## Multilingue
- Toutes les chaînes sont prêtes pour l'i18n (voir `template.py`).

## Sécurité
- JWT, CORS, validation, audit, logs structurés, WAF, anti-DDOS intégrés.

## Déploiement
- Compatible Docker, K8s, Codespaces, CI/CD.

## Tests
- Couverture maximale, sans faux positifs.

---

# Dihya Mobile Template (English)

This template provides an advanced base for mobile project generation (Flutter, React Native, Kotlin, Swift, etc.) with:
- Maximum security (auth, CORS, validation, audit, WAF, anti-DDOS)
- Dynamic internationalization (fr, en, ar, amazigh, de, zh, ja, ko, nl, he, fa, hi, es)
- Multitenancy, role management (admin, user, guest)
- Extensible plugins (API/CLI)
- GDPR compliance, auditability, anonymization, exportable logs
- Full test coverage (unit, integration, e2e)
- GitHub Actions, Docker, K8s, local fallback deployment
- 100% Codespaces/Linux/CI compatible

See `policy.md` for compliance and security requirements.
