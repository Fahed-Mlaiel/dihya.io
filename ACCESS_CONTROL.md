# 🔐 Politique de contrôle d’accès – Dihya Coding

Ce document définit la politique de contrôle d’accès (RBAC/ABAC), la gestion des rôles, permissions, sécurité, auditabilité et souveraineté numérique pour tous les modules du projet Dihya.

---

## 🛡️ Principes fondamentaux | Core Principles

- **Séparation stricte des rôles** : admin, user, invité, plugin, service, superadmin, auditeur, etc.
- **Gestion dynamique des permissions** : chaque action est contrôlée par des règles explicites (RBAC/ABAC).
- **Auditabilité** : chaque accès critique est logué, anonymisé, traçable et effaçable (RGPD).
- **Souveraineté** : aucune délégation à des services tiers sans fallback open source.
- **Multilingue & accessibilité** : interfaces et messages d’erreur traduits (fr, en, ar, amazigh), accessibles à tous.

---

## 🧑‍💼 Rôles & permissions | Roles & Permissions

| Rôle         | Description (fr)                                 | Description (en)                                 | Description (ar)                                   | Description (tzr)                       |
|--------------|--------------------------------------------------|--------------------------------------------------|----------------------------------------------------|------------------------------------------|
| superadmin   | Accès total, gestion sécurité, audit, RGPD       | Full access, security, audit, GDPR               | وصول كامل، إدارة الأمان، التدقيق، RGPD             | ⴰⴷⴷⵔⴰⵏ ⴰⵎⴰⵣⵉⵖ ⴷ ⴰⵙⵉⵏⴰⵡ, RGPD         |
| admin        | Gestion utilisateurs, plugins, logs, configs     | Manage users, plugins, logs, configs             | إدارة المستخدمين، الإضافات، السجلات، الإعدادات      | ⴰⴷⴷⵔⴰⵏ ⴷ ⵉⵙⵉⵏⴰⵡⵏ, plugins, configs   |
| user         | Utilisation normale, accès à ses données         | Normal use, access to own data                   | استخدام عادي، وصول إلى بياناته                      | ⴰⴷⴷⵔⴰⵏ ⴷ ⴰⵙⵉⵏⴰⵡ ⴷ ⵉⵙⵉⵏⴰⵡⵏ             |
| invité       | Accès limité, pas de modification                | Limited access, no modification                  | وصول محدود، بدون تعديل                              | ⴰⴷⴷⵔⴰⵏ ⴰⴷⴷⵔⴰⵏ ⴰⵎⴰⵣⵉⵖ                   |
| plugin       | Accès restreint à l’API, sandbox, logs anonymes  | Restricted API, sandbox, anonymized logs         | وصول محدود إلى API، sandbox، سجلات مجهولة           | API, sandbox, logs anonymes              |
| auditeur     | Lecture seule sur logs, audit, RGPD              | Read-only on logs, audit, GDPR                   | قراءة فقط للسجلات، التدقيق، RGPD                    | logs, audit, RGPD                        |

---

## 🔄 Modèle RBAC/ABAC – Exemples

### RBAC (Role-Based Access Control)

```yaml
roles:
  superadmin:
    - "*"
  admin:
    - manage_users
    - manage_plugins
    - view_logs
    - manage_configs
  user:
    - view_own_data
    - edit_own_profile
    - use_plugins
  invité:
    - view_public
  plugin:
    - access_api
    - write_logs
  auditeur:
    - view_logs
    - view_audit
    - export_rgpd
```

### ABAC (Attribute-Based Access Control)

```yaml
rules:
  - effect: allow
    action: export_data
    condition: user.role == "user" && user.verified == true
  - effect: deny
    action: delete_user
    condition: user.role != "superadmin"
```

### ABAC (Attribute-Based Access Control)
policies:
  - effect: allow
    action: view_logs
    condition: user.role == 'auditeur' and user.verified == true
  - effect: deny
    action: delete_user
    condition: user.role != 'superadmin'

---

## 📝 Bonnes pratiques & sécurité

- **Principle of Least Privilege** : chaque rôle n’a que les droits nécessaires.
- **Logs d’accès** : anonymisés, chiffrés, effaçables (RGPD).
- **Consentement explicite** pour toute action sensible.
- **Fallback open source** pour toute dépendance critique.
- **Tests automatisés** sur chaque règle d’accès (unit, integration, e2e).
- **Documentation multilingue** pour chaque règle, rôle, et permission.

---

## 🚨 Procédure d’escalade & gestion des incidents

1. **Détection** : toute tentative d’accès non autorisé est loguée et alertée.
2. **Notification** : l’équipe sécurité est notifiée en temps réel.
3. **Audit** : chaque incident est audité, documenté, et corrigé.
4. **Communication** : l’utilisateur concerné est informé dans sa langue.

---

## 📚 Ressources associées

- [securite.md](./Dihya/securite.md)
- [CODEOWNERS](./Dihya/CODEOWNERS)
- [README.md](./Dihya/README.md)
- [docs/policies/access_control_policy.md](./docs/policies/access_control_policy.md)

---

# Contrôle d’accès Dihya

- RBAC complet : rôles, permissions, héritage, gestion dynamique
- Authentification avancée (JWT, OAuth, MFA)
- Sécurité granulaire sur chaque ressource (API, UI, assets)
- Audit des accès, logs, alertes, reporting
- Exemples de configuration (backend, frontend, cloud)

Voir [RBAC_GUIDE.md](RBAC_GUIDE.md), [securite.md](securite.md)

> **Dihya Coding : contrôle d’accès souverain, multilingue, auditable, extensible, sécurisé, accessible pour tous.**

---

## 🔍 Audit, logs & conformité
- **Journalisation structurée** : logs JSON, rotation, stockage souverain, accès restreint
- **Audit RGPD** : export, anonymisation, purge, consentement journalisé
- **Alertes multilingues** : webhook, email, fallback local
- **Exemple Node.js** :
```js
logger.info({ event: 'access', user, role, action, date: new Date().toISOString(), lang: 'fr' });
```
- **Exemple Python** :
```python
logging.info({'event': 'access', 'user': user, 'role': role, 'action': action, 'date': datetime.utcnow(), 'lang': 'fr'})
```

---

## 🧩 Intégration multi-stack & extension
- **React/Node** : hooks RBAC, i18n, fallback souverain
- **Flask/Django** : décorateurs, middlewares, audit, extension
- **Flutter** : guards, accessibilité, logs, fallback
- **Exemples, tests, doc** : voir /tests/access_control/, /docs/access_control.md

---

## 🌍 Multilingue & accessibilité
- **Messages d’erreur, logs, alertes** : fr, en, ar, tzm (amazigh)
- **UI/UX** : accessibilité AA/AAA, i18n, fallback, tests e2e multilingues
- **Docs** : guides multilingues, onboarding, support, contribution

---

## ✅ Checklist sécurité & conformité
- [x] RBAC/ABAC documenté, testé, versionné
- [x] Logs souverains, rotation, audit
- [x] Multilingue, accessibilité, fallback
- [x] Tests unitaires, intégration, e2e
- [x] Conformité RGPD/NIS2, audit, reporting

---

## 📞 Contact & support
- **Contact sécurité** : security@dihya.eu
- **Support** : docs, guides, onboarding, Discord/Slack, fallback email

---

# ACCESS_CONTROL.md

# Contrôle d’Accès Ultra-Avancé – Dihya Coding

## Objectifs
- Sécurité maximale (RBAC, multitenancy, plugins, audit, logging, fallback IA, RGPD)
- Accessibilité, SEO backend, internationalisation dynamique (13+ langues)
- Documentation intégrée, conformité CI/CD

## Modèle RBAC
- Rôles : admin, user, auditor, plugin, guest, etc.
- Permissions : lecture, écriture, audit, gestion plugins, backup, monitoring, etc.
- Multitenancy : séparation stricte des données et accès
- Plugins : gestion des droits d’extension

## Exemples de règles
- Un admin peut tout faire
- Un user peut accéder à ses propres données
- Un plugin a des droits restreints et auditables

## Auditabilité & RGPD
- Tous les accès sont loggués, auditables, conformes RGPD

## Documentation intégrée
- Voir aussi: RBAC_GUIDE.md, API_SECURITY_GUIDE.md, AUDIT_LOGGING_GUIDE.md

---

Pour toute question, contacter l’équipe sécurité.

---

**Ce document est versionné, audité, testé, et mis à jour en continu.**

> Pour toute question, suggestion ou faille, contactez l’équipe sécurité Dihya.
