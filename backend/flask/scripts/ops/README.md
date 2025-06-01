# ops/ — Scripts d’opérations et de maintenance (Dihya Coding)

Ce dossier regroupe tous les scripts d’opérations, de maintenance et d’administration pour le backend Flask Dihya Coding.

## Objectif

- Centraliser les scripts utiles à l’exploitation, la supervision et la maintenance du backend.
- Automatiser les tâches récurrentes pour fiabiliser les opérations.
- Garantir la sécurité et la traçabilité des actions d’administration.

## Bonnes pratiques

- Documenter chaque script avec un en-tête (but, usage, paramètres, sécurité).
- Protéger les scripts critiques par des vérifications de permissions ou d’environnement.
- Logger les actions importantes pour audit et conformité.
- Ne jamais inclure de secrets ou de données sensibles en clair dans les scripts.
- Prévoir des tests ou des dry-run pour les scripts à effet destructeur.
- Respecter la conformité RGPD et les bonnes pratiques DevOps.

## Exemples de scripts à placer ici

- `restart_services.sh` : redémarrage contrôlé des services backend.
- `purge_temp_files.sh` : nettoyage des fichiers temporaires.
- `rotate_logs.sh` : rotation et archivage des logs applicatifs.
- `update_dependencies.sh` : mise à jour automatisée des dépendances.
- `check_health.sh` : vérification de l’état de santé des services.

## Exemple d’utilisation

```bash
bash restart_services.sh
bash purge_temp_files.sh --dry-run
````

# Module d’Opérations Métier Avancées (`runOps`)

## Présentation
Ce module centralise l’exécution d’opérations critiques : audit, RGPD, plugins métiers, multitenancy, monitoring, sécurité, reporting CI/CD. Il garantit la conformité, la traçabilité, la souveraineté et l’extensibilité du projet Dihya.

## Utilisation
```js
const { runOps } = require('./index');

// Exemple : Audit d’une action
const res = runOps('audit', { user, tenant, route, action });

// RGPD (anonymisation, export, consentement)
const rgpdRes = runOps('rgpd', { user, data });

// Exécution d’un plugin métier
const pluginRes = runOps('plugin', { user, plugin: 'monPlugin', action: 'do', data });

// Monitoring
const monRes = runOps('monitoring', { user });

// Sécurité
const secRes = runOps('security', { user, route, action });

// Reporting CI/CD
const reportRes = runOps('reporting', { user, tenant, route, action });
```

## Paramètres
- `operation` : Type d’opération (`audit`, `rgpd`, `plugin`, `monitoring`, `security`, `reporting`)
- `context` : Objet `{ user, tenant, data, plugin, route, action }`

## Fonctionnalités couvertes
- **Audit** : log, traçabilité, conformité RGPD, actions critiques
- **RGPD** : anonymisation, export, consentement, auditabilité
- **Plugins métiers** : chargement dynamique, hooks, fallback
- **Multitenancy** : contexte tenant, logs, audit
- **Monitoring** : statut, alertes, intégrité
- **Sécurité** : vérification des rôles, anti-abus, logs sécurité
- **Reporting CI/CD** : logs, reporting, hooks pipeline

## Bonnes pratiques
- Toujours passer le contexte utilisateur et tenant pour la traçabilité.
- Utiliser dans les scripts d’automatisation, pipelines CI/CD, hooks d’audit, tests avancés.
- Étendre les hooks métiers selon les besoins sectoriels.

## Tests
Voir `index.test.js` pour des cas d’usage avancés couvrant tous les axes (audit, RGPD, plugins, monitoring, sécurité, reporting, refus d’accès).

## Intégration CI/CD
Ajoutez dans `.github/workflows/ci.yml` ou `.gitlab-ci.yml` :
```yaml
- name: Tests avancés ops (audit, RGPD, plugins, CI/CD)
  run: npx jest backend/flask/scripts/ops/index.test.js --coverage
```

## Conformité
- RGPD, audit, souveraineté, sécurité, extensibilité, reporting CI/CD, multitenancy, plugins métiers.

---

## Checklist métier avancée & conformité

### Points de contrôle métier et sectoriels
- Traçabilité complète (logs structurés, traceId, correlationId)
- Souveraineté numérique (stockage localisé, portabilité, effacement souverain)
- Conformité RGPD (anonymisation, export, consentement, effacement)
- Sécurité avancée (contrôle d’accès, anti-abus, tests de sécurité, gestion des rôles)
- Monitoring & alertes (statut, intégrité, alertes automatiques, intégration Prometheus/Grafana/ELK/SIEM)
- Extensibilité (plugins, hooks métiers dynamiques, DWeb/IPFS)
- Gestion des incidents (alertes, rollback, fallback, rapport d’incident)
- Multitenancy, quotas, throttling
- Documentation technique et métier exhaustive
- Tests avancés (unitaires, intégration, non-régression, performance, sécurité, souveraineté, DWeb)

### Intégration monitoring avancée
- Exemples d’intégration avec Prometheus, Grafana, ELK, SIEM pour la supervision temps réel, l’alerting et l’audit.
- Export automatique des métriques d’opérations critiques.

### Gestion des incidents
- Déclenchement d’alertes automatiques (webhook, email, Slack) en cas d’échec ou d’anomalie.
- Support rollback/fallback automatisé sur incident.
- Génération de rapports d’incident détaillés (logs, contexte, actions correctives).

### Extension métier sectorielle
- Hooks personnalisés pour secteurs : santé (audit accès patient), éducation (audit notes), e-commerce (audit transactions).
- Exemples d’extension :
```js
runOps('plugin', { plugin: 'auditSante', action: 'auditAcces', data: { patientId } });
```

### DWeb/IPFS
- Export des logs et rapports critiques sur IPFS ou stockage décentralisé.
- Documentation sur la portabilité et la souveraineté des données d’audit.

### Sécurité avancée
- Tests d’injection, contrôle d’accès, audit de permissions, gestion des secrets via vault.
- Checklist sécurité :
  - [ ] Tests d’injection automatisés
  - [ ] Audit des permissions et rôles
  - [ ] Gestion centralisée des secrets
  - [ ] Logs de sécurité anonymisés

### Checklist enrichie (complément)
- [ ] Intégration monitoring avancée (Prometheus, Grafana, ELK, SIEM)
- [ ] Gestion des incidents (alertes, rollback, rapport)
- [ ] Extension métier sectorielle (hooks, plugins)
- [ ] Export DWeb/IPFS pour logs/rapports
- [ ] Sécurité avancée (tests, audit, gestion secrets)
