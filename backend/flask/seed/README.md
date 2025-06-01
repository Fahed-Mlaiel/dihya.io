# seed/ — Seed avancé & données de démonstration (Dihya Coding)

Ce dossier contient les scripts pour injecter des données de démonstration dans la base du backend Dihya Coding.

## Objectif

- Faciliter les tests, la démo et l’onboarding avec des jeux de données réalistes et multilingues.
- Permettre la validation rapide des fonctionnalités (utilisateurs, projets, contenus, etc.).

## Bonnes pratiques

- Ne jamais inclure de données sensibles ou de vrais secrets dans les seeds.
- Logger chaque opération de seed avec horodatage dans un fichier dédié.
- Prévoir des seeds multilingues (français, anglais, dialectes…).
- Valider la cohérence des données après injection.
- Utiliser ces scripts uniquement en environnement de développement ou de test.
- Documenter chaque type de seed dans ce README.

## Exemple d’utilisation

```bash
python demo_data.py
```

---

## Checklist métier avancée & conformité

### Points de contrôle métier et sectoriels
- Multilinguisme et diversité des jeux de données (fr, en, dialectes, edge-cases)
- Cohérence métier et validation automatique après seed
- Conformité RGPD (anonymisation, export, consentement, effacement)
- Auditabilité complète (logs structurés, horodatage, rapport de seed)
- Souveraineté numérique (stockage localisé, portabilité, effacement souverain)
- Sécurité avancée (aucune donnée sensible, contrôle d’accès, tests de sécurité)
- Extensibilité (ajout de nouveaux types de données, scénarios edge-case, DWeb/IPFS)
- Support rollback/suppression des seeds
- Documentation technique et métier exhaustive
- Tests avancés (unitaires, intégration, non-régression, performance, sécurité, souveraineté, DWeb)
- Intégration CI/CD complète (tests, lint, audit, reporting, publication doc)

### Exemples sectoriels
- Santé : seed patients, anonymisation, cohérence dossiers
- Éducation : seed élèves/classes, multilinguisme, edge-cases
- E-commerce : seed produits, utilisateurs, scénarios de test

### Checklist de conformité et d’industrialisation
- [ ] Multilinguisme et diversité des jeux de données
- [ ] Validation automatique de la cohérence métier
- [ ] Conformité RGPD (anonymisation, export, consentement, effacement)
- [ ] Auditabilité complète (logs, traçabilité, rapport de seed)
- [ ] Souveraineté numérique (stockage, portabilité, effacement)
- [ ] Sécurité avancée (aucune donnée sensible, contrôle d’accès, tests de sécurité)
- [ ] Extensibilité (edge-cases, nouveaux types, DWeb)
- [ ] Support rollback/suppression des seeds
- [ ] Documentation technique et métier exhaustive
- [ ] Tests avancés (unitaires, intégration, non-régression, performance, sécurité)
- [ ] Intégration CI/CD complète (tests, lint, audit, reporting)

### Exemples de seed sectoriels avancés
- Santé : patients, dossiers anonymisés, cohérence inter-dossiers, edge-cases (données manquantes, doublons).
- Éducation : élèves, classes, notes, multilinguisme, edge-cases (caractères spéciaux, valeurs extrêmes).
- E-commerce : produits, utilisateurs, transactions, edge-cases (prix négatifs, stocks nuls).

### Validation automatique post-seed
- Vérification de la cohérence métier, unicité, intégrité référentielle.
- Génération automatique d’un rapport de seed (succès, erreurs, couverture, cohérence).

### Rapport de seed & DWeb/IPFS
- Export du rapport de seed sur IPFS ou stockage décentralisé pour auditabilité souveraine.
- Documentation sur la portabilité et la souveraineté des rapports de seed.

### Rollback/suppression sécurisée des seeds
- Scripts de suppression/rollback avec logs et auditabilité complète.
- Exemples :
```bash
python demo_data.py --rollback
```

### Checklist tests avancés
- [ ] Tests de performance sur l’injection de données
- [ ] Tests de sécurité (aucune donnée sensible, contrôle d’accès)
- [ ] Tests de souveraineté (stockage, portabilité, effacement)
- [ ] Tests DWeb/IPFS (export, intégrité)

---
*Document enrichi automatiquement le 28/05/2025 – conforme au cahier des charges Dihya.*
