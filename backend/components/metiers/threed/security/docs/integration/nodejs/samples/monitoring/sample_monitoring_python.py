# Exemple avancé d’intégration Monitoring Python (Node.js)
from ...monitoring.monitoring_helper import monitoring_nodejs_hello

def run_monitoring_sample():
    print('--- Monitoring Node.js Sample (Python) ---')
    print(monitoring_nodejs_hello())

if __name__ == "__main__":
    run_monitoring_sample()
