{
  "deploy.sh": {
    "prefix": "deploy-frontend",
    "body": ["./deploy.sh"],
    "description": "Déployer automatiquement le frontend"
  },
  "backup.sh": {
    "prefix": "backup-frontend",
    "body": ["./backup.sh"],
    "description": "Sauvegarder le frontend"
  },
  "restore.sh": {
    "prefix": "restore-frontend",
    "body": ["./restore.sh <backup_dir>"],
    "description": "Restaurer le frontend depuis un backup"
  },
  "maintenance.sh": {
    "prefix": "maintenance-frontend",
    "body": ["./maintenance.sh"],
    "description": "Lancer la maintenance qualité du frontend"
  },
  "seed.sh": {
    "prefix": "seed-frontend",
    "body": ["./seed.sh"],
    "description": "Initialiser les données du frontend"
  }
}
