# Dihya API Favicon – Exemples Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dihya-favicon-meta
spec:
  replicas: 1
  selector:
    matchLabels:
      app: dihya-favicon-meta
  template:
    metadata:
      labels:
        app: dihya-favicon-meta
    spec:
      containers:
      - name: dihya-favicon-meta
        image: dihya-favicon-meta:latest
        ports:
        - containerPort: 4004
        volumeMounts:
        - name: favicon-meta-volume
          mountPath: /app
      volumes:
      - name: favicon-meta-volume
        hostPath:
          path: /workspaces/Dihya/Dihya/backend/assets/branding/api_favicons/meta
          type: Directory
```
