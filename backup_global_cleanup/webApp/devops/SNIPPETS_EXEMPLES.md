{
  "deploy.sh": {
    "prefix": "deploy-webApp",
    "body": ["./deploy.sh"],
    "description": "Déployer automatiquement le webApp"
  },
  "backup.sh": {
    "prefix": "backup-webApp",
    "body": ["./backup.sh"],
    "description": "Sauvegarder le webApp"
  },
  "restore.sh": {
    "prefix": "restore-webApp",
    "body": ["./restore.sh <backup_dir>"],
    "description": "Restaurer le webApp depuis un backup"
  },
  "maintenance.sh": {
    "prefix": "maintenance-webApp",
    "body": ["./maintenance.sh"],
    "description": "Lancer la maintenance qualité du webApp"
  },
  "seed.sh": {
    "prefix": "seed-webApp",
    "body": ["./seed.sh"],
    "description": "Initialiser les données du webApp"
  }
}
