# Rapports d’audit de conformité – Dihya Compliance

Ce dossier centralise la génération, l’export et l’archivage sécurisé des rapports d’audit de conformité pour la plateforme Dihya Coding.

## 📚 Contenu du dossier
- **badge_conformite.svg** : Badge dynamique de conformité RGPD, sécurité, audit, accessibilité, CI
- **test_badge_conformite.py** : Tests unitaires/accessibilité/conformité du badge et des rapports
- **README.md** : Présentation, bonnes pratiques, exemples, multilingue

## 🛡️ Sécurité & conformité
- Génération automatisée de rapports RGPD, licences, politiques, provenance
- Badge de conformité dynamique (SVG, multilingue, accessibilité, CI/CD)
- Exports automatisés pour audit externe (CSV, JSON, PDF)
- Archivage sécurisé, logs structurés, anonymisation, auditabilité
- Conformité RGPD, portabilité, droit à l’oubli

## 🔗 Liens utiles
- [Guide RGPD](../../../LEGAL_COMPLIANCE_GUIDE.md)
- [Guide audit](../../../AUDIT_LOGGING_GUIDE.md)
- [README global](../../../README.md)

## 🧑‍💻 Bonnes pratiques
- Générer un badge à chaque build CI/CD (GitHub Actions, Docker, K8s)
- Tester l’accessibilité (contraste, alt, ARIA)
- Exporter les rapports dans tous les formats requis (CSV, JSON, PDF)
- Ne jamais exposer de données sensibles dans les rapports publics
- Archiver chaque rapport avec horodatage, hash, signature

## 📝 Exemple d’utilisation

### Génération du badge de conformité (Python)
```python
from badge_conformite import generer_badge_conformite
svg = generer_badge_conformite(etat="conforme", langue="fr")
with open("badge_conformite.svg", "w") as f:
    f.write(svg)
```

### Test d’accessibilité du badge
```bash
pytest test_badge_conformite.py
```

---

> **Dihya Coding : conformité, sécurité, auditabilité, accessibilité, souveraineté, multilingue.**
