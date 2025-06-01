# Politique d'utilisation des utilitaires de génération Dihya

## Sécurité
- Utilisation obligatoire des fonctions de log sécurisé (`secure_log`).
- Validation stricte des entrées/sorties (voir `validate_input`).
- Respect des normes RGPD et auditabilité.

## Internationalisation
- Toutes les chaînes doivent passer par `get_i18n`.
- Support multilingue obligatoire (fr, en, ar, de, zh, ja, ko, nl, he, fa, hi, es, amazigh).

## Extensibilité
- Ajout de plugins via API/CLI autorisé si conforme à la politique de sécurité.

## Conformité
- Toute modification doit être documentée et testée.
- Respect du modèle RESTful et GraphQL.

## Audit
- Les logs doivent être structurés et exportables.

---

# Dihya Coding Project – Politique Utilitaires
