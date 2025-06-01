# templates/ — Templates intelligents par domaine (Dihya Coding)

Ce dossier contient les templates dynamiques utilisés pour la génération automatique de projets selon le domaine métier (e-commerce, éducation, social, etc.).

---

## Objectif

- Offrir des bases de code et de structure adaptées à chaque secteur d’activité.
- Permettre la personnalisation et l’extension sans modifier le cœur du backend.
- Garantir la sécurité, la conformité RGPD, la modularité et la souveraineté logicielle.

---

## Bonnes pratiques

- **Documenter chaque template** (fonction, structure, dépendances, domaine visé, hooks disponibles).
- **Versionner chaque template** pour assurer la traçabilité des évolutions.
- **Valider la conformité métier, sécurité, accessibilité et RGPD** de chaque template.
- **Sélection automatique** du template selon le domaine détecté (`get_template_for_domain`).
- **Ajout facile** : chaque nouveau template = un nouveau fichier/module dans ce dossier.
- **Ne jamais inclure de secrets, d’identifiants ou de données sensibles** dans les templates.
- **Prévoir des tests unitaires** pour chaque template critique.
- **Logger les actions critiques** pour auditabilité (sans fuite de données sensibles).
- **Respecter la licence AGPL et la charte Dihya Coding**.
- **Prévoir la purge et l’export des logs liés à la génération de templates** (conformité RGPD).
- **Documenter les hooks et points d’extension** pour chaque template.

---

## Exemple de structure de template

```python
"""
Template e-commerce pour Dihya Coding.
Inclut la structure de base, les routes, les modèles et les bonnes pratiques du secteur.
"""
from app.plugins.templates.generation_template import GenerationTemplateBase

class EcommerceTemplate(GenerationTemplateBase):
    name = "Ecommerce"
    description = "Template pour boutique en ligne avec panier, paiement, gestion produits."
    domain = "e-commerce"
    version = "1.0.0"
    author = "Dihya Coding"
    safe = True

    def generate_files(self, needs):
        # Validation minimale des besoins (sécurité)
        if not isinstance(needs, dict):
            return {}
        # Exemple fictif
        return {
            "frontend/pages/Shop.js": "// Page boutique auto-générée",
            "backend/routes/shop.py": "# Route Flask pour la boutique"
        }