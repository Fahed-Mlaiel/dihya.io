# Dihya Coding – Tests Plugins & Templates Métiers

## Présentation

Ce dossier contient les tests automatisés pour le module de plugins et de templates métiers de Dihya Coding. Ce module permet d’étendre la plateforme avec des templates métiers intelligents (e-commerce, éducation, santé, IA, etc.) et des plugins personnalisés (analytics, paiement, CMS…). Les tests garantissent la robustesse, la sécurité, la conformité RGPD et l’extensibilité de l’écosystème plugins/templates.

---

## Objectifs des tests

- **Vérifier l’import, l’export et la génération de templates métiers**
- **Assurer la compatibilité multi-stack (frontend, backend, scripts, IA, DevOps, Blockchain)**
- **Tester l’installation, l’activation et la désactivation des plugins**
- **Garantir la sécurité des templates/plugins (validation, sandbox, permissions)**
- **Valider la conformité RGPD (logs, audit, suppression/export)**
- **Couvrir tous les cas d’usage métier (génération, personnalisation, marketplace, etc.)**
- **Assurer la non-exposition des secrets/API dans les logs ou réponses**

---

## Structure des tests

```
/plugins/templates/tests/
├── test_template_import.py      # Tests import/export de templates métiers (JSON, YAML, JS)
├── test_template_generation.py  # Tests génération de projets à partir de templates
├── test_plugin_install.py       # Tests installation/activation/désactivation de plugins
├── test_plugin_security.py      # Tests sécurité (sandbox, permissions, validation)
├── test_rgpd_compliance.py      # Tests conformité RGPD (logs, suppression, export)
├── test_marketplace.py          # Tests intégration marketplace (ajout, rating, contribution)
└── fixtures/                    # Données de test, mocks, configs simulées
```

---

## Bonnes pratiques

- **Tests unitaires et d’intégration** (pytest)
- **Mocks** pour simuler les templates/plugins externes
- **Validation stricte** des schémas de templates et plugins
- **Logs horodatés** pour auditabilité
- **Vérification de la non-exposition des secrets**
- **Tests automatisés dans CI/CD (GitHub Actions)**
- **Documentation claire et cas d’usage reproductibles**

---

## Exemples de cas testés

- Import d’un template métier (santé, finance, IA…) → génération projet fonctionnel
- Export d’un template personnalisé par l’utilisateur
- Installation d’un plugin analytics ou paiement → activation sécurisée
- Désactivation/suppression d’un plugin → rollback sans perte de données
- Marketplace : ajout d’un template/plugin, rating, contribution externe
- Suppression/export des logs sur demande utilisateur (RGPD)
- Sécurité : aucune fuite de clé/API dans les logs ou réponses

---

## Lancer les tests

Depuis la racine du backend Flask :

```bash
pytest app/plugins/templates/tests/
```

---

## Contribution

- Ajouter des cas de test pour chaque nouveau template métier ou plugin intégré
- Respecter la structure et les conventions de nommage
- Documenter chaque test (docstring, typage)
- Vérifier la conformité RGPD et la sécurité à chaque PR

---

## Licence

Projet sous licence **AGPL** – open source, souveraineté numérique garantie.

---