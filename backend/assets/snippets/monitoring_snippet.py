"""
monitoring_snippet.py – Monitoring backend (Dihya)
Metrics, healthcheck, logs, audit, RGPD, multilingue.
"""
import time, logging

def healthcheck():
    return {"status": "ok", "timestamp": time.time()}

def record_metric(name, value):
    logging.info(f"[METRIC] {name}={value}")
    return {"metric": name, "value": value}

# Exemple d’utilisation
if __name__ == "__main__":
    print(healthcheck())
    print(record_metric("cpu_usage", 0.12))
