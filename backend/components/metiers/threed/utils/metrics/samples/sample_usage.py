# sample_usage.py – Exemples ultra avancés pour le module metrics (clé en main)
from ..core import metrics
import json
with open('sample_metrics_data.json') as f:
    data = json.load(f)["metrics"]

print('Moyenne:', metrics.calculer_moyenne(data))
print('Médiane:', metrics.calculer_mediane(data))

try:
    metrics.calculer_moyenne([])
except Exception as e:
    print('Erreur attendue:', e)
