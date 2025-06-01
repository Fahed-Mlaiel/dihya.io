# tests/performance/ — Tests de charge & performance Backend Dihya Coding

Ce dossier contient les scripts, scénarios et résultats de tests de charge et de performance pour le backend Flask de Dihya Coding.

## Objectif

- Évaluer la robustesse, la scalabilité et la réactivité de l’API et des services critiques.
- Identifier les goulets d’étranglement et anticiper les besoins d’optimisation.
- Garantir une expérience utilisateur fluide, même sous forte charge.

## Bonnes pratiques

- Utiliser des outils open source (Locust, JMeter, k6, etc.) pour simuler la charge.
- Documenter chaque scénario de test (endpoints, volume, durée, utilisateurs virtuels).
- Ne jamais utiliser de données sensibles ou de secrets dans les scénarios.
- Logger les résultats et anomalies détectées pour audit et amélioration continue.
- Automatiser les tests de performance dans la CI/CD si possible.
- Prévoir des seuils d’alerte (latence, taux d’erreur, saturation).

## Exemple de structure

- `locustfile.py` : scénario Locust pour simuler des utilisateurs concurrents.
- `report/` : dossiers pour les rapports de tests (HTML, CSV, etc.).
- `README.md` : documentation et consignes d’utilisation.

## Exemple d’utilisation (Locust)

```bash
locust -f locustfile.py --host=http://localhost:5000
````

---

## Checklist métier avancée & conformité
- [ ] Scénarios de charge réalistes (API critiques, edge-cases, multitenancy)
- [ ] Sécurité avancée (aucune donnée sensible, anonymisation, audit des accès)
- [ ] Auditabilité complète (logs structurés, horodatage, rapport de test)
- [ ] Souveraineté numérique (stockage localisé, portabilité, effacement souverain)
- [ ] Extensibilité (hooks métier, DWeb/IPFS, plugins sectoriels)
- [ ] Validation automatique de la cohérence métier après chaque test
- [ ] Documentation technique et métier exhaustive
- [ ] Tests avancés (charge, endurance, stress, edge-cases, sécurité, souveraineté, DWeb)
- [ ] Intégration CI/CD complète (tests, lint, audit, reporting, publication doc)

## Extension DWeb/IPFS
- Export des rapports de tests de performance sur IPFS ou stockage décentralisé
- Documentation sur la portabilité et la souveraineté des rapports

## Hooks métier performance
- Ajoutez des hooks pour déclencher des actions métier après chaque test critique (ex : notification, audit, synchronisation DWeb)

## Intégration CI/CD
Ajoutez dans `.github/workflows/ci.yml` :
```yaml
- name: Tests de performance backend
  run: locust -f backend/flask/tests/performance/locustfile.py --headless -u 100 -r 10 --run-time 5m --host=http://localhost:5000
```

## Tests avancés recommandés
- Tests de charge sur endpoints critiques (CRUD, login, recherche, etc.)
- Tests d’endurance (longue durée, montée en charge progressive)
- Tests de stress (saturation, gestion des erreurs)
- Tests de souveraineté (stockage, portabilité, effacement souverain)
- Tests DWeb/IPFS (export, intégrité, portabilité)
- Tests d’auditabilité (logs, rapports, traçabilité)
