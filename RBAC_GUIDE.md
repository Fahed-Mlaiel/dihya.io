# 🛡️ Dihya – Guide RBAC (Role-Based Access Control) Ultra Avancé, Multilingue, Souveraineté

---

## Table des matières

- [Introduction](#introduction)
- [Objectifs](#objectifs)
- [Principes RBAC Dihya](#principes-rbac-dihya)
- [Modèle de rôles & permissions](#modèle-de-rôles--permissions)
- [Architecture RBAC multi-stack](#architecture-rbac-multi-stack)
- [Sécurité, conformité & souveraineté](#sécurité-conformité--souveraineté)
- [Exemples d’implémentation](#exemples-dimplémentation)
- [Tests & auditabilité](#tests--auditabilité)
- [Templates & modèles](#templates--modèles)
- [Multilingue](#multilingue)
- [Contact & support](#contact--support)

---

## Introduction

Ce guide décrit la politique RBAC (Role-Based Access Control) du projet **Dihya**.
Il garantit la sécurité, la traçabilité, la conformité RGPD/NIS2, la souveraineté numérique, la compatibilité multi-stack (React, Flask, Node, Django, Flutter…), l’accessibilité, et la portabilité (Linux, Codespaces, cloud souverain, fallback open source).

---

## Objectifs

- Contrôle d’accès basé sur les rôles (RBAC), multitenancy, plugins, audit, logging, RGPD
- Accessibilité, SEO backend, internationalisation dynamique (13+ langues)
- Documentation intégrée, conformité CI/CD

---

## Principes RBAC Dihya

- **Séparation stricte des rôles** : chaque métier a des droits limités à ses besoins.
- **Gestion centralisée** : mapping rôles-permissions versionné, auditable, multilingue.
- **Traçabilité** : chaque attribution, modification ou révocation de rôle est loggée.
- **Multilingue** : chaque rôle et permission est documenté en fr, en, ar, tzm.
- **Auditabilité** : chaque action critique est journalisée et exportable.
- **Souveraineté** : aucune dépendance cloud non maîtrisée, fallback open source.

---

## Modèle de rôles & permissions

| Rôle système         | Description (fr/en/ar/tzm)         | Permissions principales                    |
|----------------------|------------------------------------|--------------------------------------------|
| admin                | Admin global                       | * (tous droits)                            |
| devops               | DevOps                             | deploy, monitor, rollback, manage-secrets  |
| frontend             | Développeur Frontend               | ui:edit, i18n:manage, a11y:test            |
| backend              | Développeur Backend                | api:edit, rgpd:manage, ai:fallback         |
| dpo                  | Data Privacy Officer               | rgpd:audit, dpi:manage, notify:cnil        |
| qa                   | QA/Accessibilité                   | test:run, a11y:audit, report:issue         |
| po                   | Product Owner                      | doc:edit, roadmap:manage, consent:manage   |
| user                 | Utilisateur                        | app:use                                    |

### Exemple YAML (roles.yaml)

```yaml
roles:
  admin:
    permissions: ["*"]
  devops:
    permissions: [deploy, monitor, rollback, manage-secrets]
  frontend:
    permissions: [ui:edit, i18n:manage, a11y:test]
  backend:
    permissions: [api:edit, rgpd:manage, ai:fallback]
  dpo:
    permissions: [rgpd:audit, dpi:manage, notify:cnil]
  qa:
    permissions: [test:run, a11y:audit, report:issue]
  po:
    permissions: [doc:edit, roadmap:manage, consent:manage]
  user:
    permissions: [app:use]
```

---

## Architecture RBAC multi-stack

- **Backend** : Décorateurs RBAC (Python/Node), middleware, JWT claims, logs.
- **Frontend** : Affichage conditionnel selon rôle, fallback accessibilité, i18n.
- **Mobile** : Permissions dynamiques, fallback offline, logs locaux.
- **Plugins** : RBAC appliqué à chaque extension, auditabilité.
- **CI/CD** : Rôles sur pipelines, secrets, artefacts.
- **Infra** : RBAC sur monitoring, logs, accès cloud souverain.

---

## Sécurité, conformité & souveraineté

- **Chiffrement JWT** : claims rôles, permissions, exp, logs d’accès.
- **MFA obligatoire** pour tout accès critique/admin.
- **Logs anonymisés** : aucune donnée perso dans les logs RBAC.
- **Fallback open source** : RBAC fonctionnel même sans cloud externe.
- **Audit RGPD/NIS2** : export, purge, conformité.

---

## Exemples d’implémentation

### Python (Flask/FastAPI)

```python
from functools import wraps
import jwt

def require_role(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = request.headers.get("Authorization", "").replace("Bearer ", "")
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            if role not in payload.get("roles", []):
                return jsonify({"error": "Accès refusé"}), 403
            return f(*args, **kwargs)
        return wrapper
    return decorator

@app.route("/api/secure")
@require_role("admin")
def secure_route():
    return jsonify({"msg": "OK"})
```

### Frontend (React)

```javascript
function RBAC({ role, children }) {
  const userRoles = useUserRoles(); // hook custom
  if (!userRoles.includes(role)) return null;
  return children;
}

// Usage :
<RBAC role="admin"><AdminPanel /></RBAC>
```

---

## Tests & auditabilité

- **Tests unitaires** : chaque permission, chaque rôle.
- **Tests intégration/e2e** : accès/refus, logs, multilingue.
- **Tests sécurité** : MFA, JWT, logs, RBAC bypass.
- **Audit** : export logs, rapport conformité, purge RGPD.

---

## Templates & modèles

### Template d’attribution de rôle

```
- Utilisateur :
- Rôle attribué :
- Permissions :
- Date d’attribution :
- Attribué par :
- Preuve : [capture/log]
- Commentaire :
```

### Exemple rempli

```
- Utilisateur : alice@dihya.eu
- Rôle attribué : devops
- Permissions : deploy, monitor, rollback
- Date d’attribution : 2025-05-20
- Attribué par : @admin
- Preuve : /logs/rbac/2025-05-20_alice.log
- Commentaire : MFA activé, accès validé
```

---

## Multilingue

- **Français** : Ce guide est disponible en français.
- **English** : This guide is available in English.
- **العربية** : هذا الدليل متوفر باللغة العربية.
- **ⴰⵣⵉⵖⴻⵏⵜ** : Asnif n tamedyazt-agi d-ittwasnen s tmazight.

*(Voir `/docs/i18n/` pour les versions traduites)*

---

## Contact & support

- **Slack** : #dihya-rbac
- **Email** : rbac@dihya.eu
- **GitHub Issues** : [Lien](https://github.com/your-org/dihya/issues)

---

> **Ce guide est validé pour la production. Toute modification doit être soumise via PR et validée par le Doc Lead et le RSSI.**

# Guide RBAC Dihya

- Modèle RBAC complet (rôles, permissions, héritage)
- Exemples de configuration (backend, frontend, cloud)
- Sécurité, audit, reporting, tests
- Intégration avec l’authentification, la gestion des accès

Voir [ACCESS_CONTROL.md](ACCESS_CONTROL.md), [securite.md](securite.md)

---

## 🛡️ Modèle RBAC ultra avancé Dihya
- Séparation stricte des rôles (superadmin, admin, user, invité, plugin, auditeur, etc.)
- Mapping YAML/JSON, logs d’attribution, auditabilité, rotation, fallback souverain
- Exemples d’intégration multi-stack (Node.js, Flask, Django, React, Flutter)
- Gestion multilingue des messages d’erreur, logs, alertes (fr, en, ar, amazigh)
- Tests unitaires, intégration, e2e, audit SAST/DAST, conformité RGPD/NIS2

### Extrait Node.js
```js
const { checkRole } = require('./rbac');
if (!checkRole(user, 'admin')) throw new Error(i18n['fr'] + ' : accès refusé');
```

### Extrait Python/Flask
```python
from rbac import check_role
if not check_role(user, 'admin'):
    raise PermissionError(i18n['fr'] + ' : accès refusé')
```

### Extrait Flutter
```dart
if (!user.roles.contains('admin')) {
  throw Exception(i18n['fr'] + ' : accès refusé');
}
```

---

## 🔍 Audit, logs & conformité
- Journalisation structurée, rotation, stockage souverain, accès restreint
- Audit RGPD, export, anonymisation, purge, consentement journalisé
- Alertes multilingues, webhook, email, fallback local

---

## ✅ Checklist sécurité & conformité
- [x] RBAC documenté, testé, versionné
- [x] Logs souverains, rotation, audit
- [x] Multilingue, accessibilité, fallback
- [x] Tests unitaires, intégration, e2e
- [x] Conformité RGPD/NIS2, audit, reporting

---

**Ce guide est versionné, audité, testé, et mis à jour en continu.**

> Pour toute question, suggestion ou faille, contactez l’équipe sécurité Dihya.
