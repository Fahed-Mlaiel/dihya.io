# 📊 Analytics – Dihya Coding

Ce module gère l’intégration, la collecte et l’analyse des données d’usage de la plateforme Dihya Coding, dans le respect des meilleures pratiques de sécurité, de conformité RGPD, d’auditabilité et d’extensibilité.

---

## 🚀 Objectifs

- Suivi de l’utilisation des fonctionnalités clés (génération, preview, plugins…)
- Analyse de la performance et de l’engagement utilisateur
- Support multi-plugins (Matomo, Plausible, etc.), 100% open-source
- Respect strict de la vie privée (pas de données personnelles sans consentement)
- Auditabilité et logs horodatés pour la transparence

---

## 🛡️ Sécurité & RGPD

- **Consentement explicite** requis avant tout tracking
- **Anonymisation** des IP et des identifiants
- **Opt-out** accessible à tout moment
- **Aucune donnée sensible** collectée sans justification métier
- **Logs d’accès** et d’événements pour audit
- **Suppression/export** des données sur demande utilisateur

---

## ⚙️ Architecture & Extensibilité

- Intégration facile de nouveaux outils analytics via plugins
- Configuration centralisée (`analytics.config.js`)
- Support des événements personnalisés (ex : génération, export, login)
- Documentation claire pour chaque intégration

---

## 📈 Bonnes pratiques

- Ne jamais tracker les pages sensibles (admin, API, données privées)
- Prioriser l’analytics côté serveur pour la robustesse
- Documenter chaque événement suivi (nom, description, finalité)
- Vérifier la conformité RGPD à chaque évolution

---

## 📚 Documentation

- [Exemple d’intégration Matomo](./matomo.md)
- [Exemple d’intégration Plausible](./plausible.md)
- [Configuration analytics](./analytics.config.js)
- [Politique de confidentialité](../../public/privacy.md)

---

> **Transparence et souveraineté : l’analytics au service de l’utilisateur, jamais à son détriment.**