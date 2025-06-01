# performance/ — Scripts d’analyse et d’optimisation des performances (Dihya Coding)

Ce dossier regroupe les scripts dédiés à l’analyse, au suivi et à l’optimisation des performances du backend Flask Dihya Coding.

## Objectif

- Mesurer et améliorer la rapidité, la scalabilité et l’efficacité des composants backend.
- Identifier les goulets d’étranglement, les requêtes lentes et les ressources surconsommées.
- Automatiser les benchmarks et les tests de charge.

## Bonnes pratiques

- Documenter chaque script avec un en-tête (but, usage, paramètres, sécurité).
- Protéger les scripts critiques par des vérifications d’environnement ou de permissions.
- Logger les résultats pour audit, analyse et suivi dans le temps.
- Ne jamais inclure de données sensibles ou de secrets dans les scripts ou les logs.
- Prévoir des tests reproductibles et des comparaisons avant/après optimisation.
- Utiliser des outils standards (locust, ab, wrk, py-spy, etc.) si pertinent.

## Exemple de structure

- `benchmark_api.py` : benchmark des endpoints API.
- `profile_memory.py` : analyse de la consommation mémoire.
- `analyze_db_queries.py` : détection des requêtes SQL lentes.
- `stress_test.sh` : test de charge automatisé.

## Exemple d’utilisation

```bash
python benchmark_api.py --endpoint /api/generate --count 1000
bash stress_test.sh --duration 5m