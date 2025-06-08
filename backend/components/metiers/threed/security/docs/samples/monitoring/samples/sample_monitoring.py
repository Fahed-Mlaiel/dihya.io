# sample_monitoring.py
# Exemple d’intégration avancée pour la supervision

from helpers_monitoring import send_alert, generate_dashboard

send_alert('CPU usage high')
print(generate_dashboard({'cpu': 90, 'ram': 80}))
