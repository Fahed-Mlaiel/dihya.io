# Quickstart 3D API (Dihya)

## 1. Créer un projet 3D
```bash
curl -X POST http://localhost:8000/threedprojects/ -H 'Authorization: Bearer <token>' -d '{"name": "Projet Test", "description": "Demo", "lang": "fr"}'
```

## 2. Lister les projets 3D
```bash
curl http://localhost:8000/threedprojects/
```

## 3. Export RGPD d’un projet
```bash
curl http://localhost:8000/threedprojects/1/export_rgpd/
```

## 4. Importer un projet (CLI)
```bash
python cli_3d.py import --file export.json
```

## 5. Lister les plugins dynamiques
```bash
curl http://localhost:8000/3d/plugins/list
```

## 6. Exécuter un plugin métier
```bash
curl -X POST http://localhost:8000/3d/plugins/run -d '{"plugin": "industrie", "params": {"foo": "bar"}}'
```

## 7. Tester l’accessibilité
```bash
pytest tests/test_accessibility_e2e.py
```

## 8. Tester la sécurité
```bash
pytest tests/test_security_e2e.py
```

## 9. Tester la performance
```bash
pytest tests/test_performance_e2e.py
```

## 10. Tester le fallback AI
```bash
pytest tests/test_fallback_ai.py
```

---

*Guide multilingue, accessible, RGPD, SEO, extensible, CI/CD-ready.*
