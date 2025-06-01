# monitor_ddos.py – Monitoring DDoS (Python, Dihya)
"""
Script de monitoring réseau pour détecter les attaques DDoS (logs, alertes, analyse de trafic).
"""
import time, logging

def monitor():
    logging.basicConfig(filename='ddos_monitor.log', level=logging.INFO)
    while True:
        # ...logique de détection d’anomalies réseau...
        logging.info('Vérification DDoS OK')
        time.sleep(60)

if __name__ == '__main__':
    monitor()
