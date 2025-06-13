# Exemple avancé d’intégration Monitoring Python
from ...monitoring.monitoring_helper import monitoring_nodejs_hello


def run_monitoring_sample():
    print("--- Monitoring Python Sample ---")
    print(monitoring_nodejs_hello())


if __name__ == "__main__":
    run_monitoring_sample()
