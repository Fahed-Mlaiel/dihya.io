# Guide de déploiement du module backup Dihya

## Docker
```bash
cd backend/backup
docker build -t dihya-backup .
docker run -p 8000:8000 dihya-backup
```

## GitHub Actions (extrait)
```yaml
name: CI Backup
on: [push, pull_request]
jobs:
  test-backup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Install deps
        run: |
          cd backend/backup
          pip install -r ../../requirements-dev.txt
      - name: Run tests
        run: pytest tests/
```

## Kubernetes (exemple)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dihya-backup
spec:
  replicas: 1
  selector:
    matchLabels:
      app: dihya-backup
  template:
    metadata:
      labels:
        app: dihya-backup
    spec:
      containers:
      - name: backup
        image: dihya-backup:latest
        ports:
        - containerPort: 8000
```

## Fallback local
```bash
cd backend/backup
uvicorn backup_service:router --reload
```

## Codespaces/Linux
- 100% compatible, pas de dépendance propriétaire.

## Sécurité
- Voir backup_config.toml, RGPD_POLICY.md, API_DOC.md
