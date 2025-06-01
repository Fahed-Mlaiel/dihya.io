# FAQ Développeur – Dihya Coding

## Général
**Q : Comment démarrer rapidement ?**
R : Suivez `DEV_ONBOARDING.md` et lancez `make dev` après installation des dépendances.

**Q : Quelles stacks sont supportées ?**
R : Linux, GitHub Codespaces, Docker, Python 3.11+, Node.js 20+, Bash.

## Sécurité
**Q : Comment fonctionne l’authentification ?**
R : JWT, CORS strict, WAF, anti-DDOS, audit logging, anonymisation RGPD.

**Q : Où trouver les politiques de sécurité ?**
R : Voir `docs/securite_GUIDE.md` et `docs/securite_POLICY.md`.

## Internationalisation
**Q : Comment ajouter une langue ?**
R : Ajoutez un fichier dans `/i18n/` et référencez-le dans la config.

## Plugins
**Q : Comment développer un plugin ?**
R : Suivez `PLUGINS_README.md` et testez avec les exemples fournis.

## Tests
**Q : Quelle est la couverture de tests ?**
R : 100% (unitaires, intégration, e2e, mocks, fixtures). Voir `TEST_STRATEGY.md`.

## RGPD & Audit
**Q : Comment exporter mes données ?**
R : Utilisez l’API `/users/me/export` (format JSON/CSV, anonymisation automatique).

## Déploiement
**Q : Comment déployer sur GitHub Actions/Docker/K8s ?**
R : Suivez `DEPLOYMENT.md` et les workflows CI/CD fournis.

---

Pour toute question non listée, ouvrez une issue ou contactez les mainteneurs (`docs/MAINTAINERS.md`).
