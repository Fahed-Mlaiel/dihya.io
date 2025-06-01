# Dihya API Favicons PNG – Exemples Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dihya-favicons-png
spec:
  replicas: 1
  selector:
    matchLabels:
      app: dihya-favicons-png
  template:
    metadata:
      labels:
        app: dihya-favicons-png
    spec:
      containers:
      - name: dihya-favicons-png
        image: dihya-favicons-png:latest
        ports:
        - containerPort: 4003
        volumeMounts:
        - name: favicons-volume
          mountPath: /app
      volumes:
      - name: favicons-volume
        hostPath:
          path: /workspaces/Dihya/Dihya/backend/assets/branding/api_favicons/png
          type: Directory
```
