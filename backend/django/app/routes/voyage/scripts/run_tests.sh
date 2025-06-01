# Script shell de test automatisé pour le module voyage
# Usage: ./run_tests.sh
# Exécute tous les tests unitaires, d’intégration, e2e, accessibilité, performance du module voyage.

pytest tests/ --maxfail=1 --disable-warnings -v
