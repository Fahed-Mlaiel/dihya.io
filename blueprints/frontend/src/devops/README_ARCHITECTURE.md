# Architecture – DevOps

## Schéma d’architecture (ASCII)
```
[ci.yml] -> [deploy.sh] -> [Dockerfile.frontend] -> [deployment.yaml]
      |           |                |
[backup.sh]   [restore.sh]   [seed.sh]   [maintenance.sh]
      |           |                |
   [main.tf]   [README.md]   [README_CI.md]
```

- **ci.yml** : Automatisation CI/CD (tests, build, déploiement)
- **deploy.sh** : Déploiement automatique
- **Dockerfile.frontend** : Build et conteneurisation
- **deployment.yaml** : Déploiement Kubernetes
- **main.tf** : Infrastructure as Code (Terraform)
- **backup.sh / restore.sh** : Sauvegarde et restauration
- **seed.sh** : Initialisation de données
- **maintenance.sh** : Qualité, lint, format
- **README** : Documentation, conventions, exemples
