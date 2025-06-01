# cleaning/ — Scripts de nettoyage et purge (Dihya Coding)

Ce dossier regroupe les scripts de nettoyage et de purge pour le backend Flask Dihya Coding.

## Objectif

- Automatiser le nettoyage des fichiers temporaires, logs obsolètes, données expirées ou inutilisées.
- Garantir la performance, la sécurité et la conformité du système en limitant l’accumulation de données inutiles.
- Faciliter la maintenance régulière et la gestion de l’espace disque.

## Bonnes pratiques

- Documenter chaque script avec un en-tête (but, usage, paramètres, sécurité).
- Protéger les scripts critiques par des vérifications d’environnement ou de permissions.
- Logger les opérations de nettoyage pour audit et conformité (voir utils/audit.js).
- Prévoir des options de dry-run pour éviter les suppressions accidentelles.
- Ne jamais supprimer de données critiques sans sauvegarde préalable.
- Respecter la conformité RGPD pour la suppression des données personnelles (voir utils/rgpd.js).
- Supporter le multitenancy, la sécurité, le monitoring et l’extensibilité via plugins.

## Exemple de structure

- `purge_temp_files.sh` : suppression des fichiers temporaires.
- `clean_old_logs.sh` : nettoyage des logs anciens ou volumineux.
- `delete_expired_data.py` : suppression des données expirées en base.
- `dry_run_example.sh` : exemple de script avec option dry-run.
- `index.js` : API Node.js pour automatisation CI/CD, audit, RGPD, plugins, multitenancy.
- `index.test.js` : tests avancés (audit, RGPD, plugins, multitenancy, monitoring, sécurité).

## Exemple d’utilisation

```bash
bash purge_temp_files.sh --dry-run
python delete_expired_data.py --confirm
node index.js
npx jest index.test.js --coverage
```

## Intégration CI/CD

- Les tests cleaning sont intégrés dans le pipeline `.github/workflows/ci.yml`.
- Toute modification doit passer les tests unitaires et d’intégration avec couverture élevée.
- Les logs d’audit et de conformité sont vérifiés automatiquement.

---

## Recommandations avancées & Checklist de conformité

### Sécurité & Conformité
- Utiliser des variables d’environnement pour toute configuration sensible.
- Intégrer des scans de vulnérabilité (ex: npm audit, bandit pour Python) dans le CI/CD.
- Appliquer le principe du moindre privilège pour les scripts et accès aux données.
- S’assurer que tous les logs sensibles sont masqués ou anonymisés.
- Ajouter des tests de sécurité automatisés (ex: injection, accès non autorisé).

### Audit & Traçabilité
- Générer un identifiant unique de session pour chaque exécution de script.
- Archiver les logs d’audit dans un stockage sécurisé et redondant.
- Prévoir une rotation automatique des logs et leur purge conforme.

### Monitoring & Observabilité
- Intégrer des métriques d’exécution (temps, succès/échec, volume traité) dans un dashboard (Prometheus, Grafana, etc.).
- Déclencher des alertes en cas d’échec ou d’anomalie (ex: via webhook, email, Slack).

### Tests & Qualité
- Couvrir 100% des branches critiques par des tests unitaires et d’intégration.
- Ajouter des tests de non-régression à chaque évolution.
- Générer automatiquement les rapports de couverture et les publier dans le CI.

### Documentation & Maintenabilité
- Générer la documentation technique à chaque build (Sphinx, JSDoc, OpenAPI).
- Ajouter des exemples d’utilisation avancés (scénarios edge-case, erreurs courantes).
- Lister les dépendances et leur politique de mise à jour.

### Souveraineté & DWeb
- Privilégier des solutions open source et souveraines pour le stockage, la base de données et l’orchestration.
- Documenter les points de contrôle de souveraineté (localisation, portabilité, effacement).
- Prévoir une option d’exécution décentralisée (DWeb/IPFS) si pertinent.

### CI/CD & Automatisation
- Vérifier la reproductibilité des environnements (Docker, requirements.txt, package-lock.json).
- Intégrer des étapes de linting, formatage automatique et vérification de licences.
- Déployer automatiquement la documentation et les artefacts de build.

### Checklist de conformité
- [ ] Tous les scripts sont documentés et testés.
- [ ] Les logs d’audit sont activés et vérifiés.
- [ ] Les tests de sécurité et de conformité passent dans le CI.
- [ ] La couverture de test est supérieure à 90%.
- [ ] Les dépendances sont à jour et sans vulnérabilité critique.
- [ ] La documentation est générée et publiée à chaque release.
- [ ] Les exigences de souveraineté et RGPD sont respectées.
