"""
Dihya – Script de monitoring de performance backend Flask
Usage: python monitor_performance.py --interval 60
Surveille le temps de réponse de l’API et la charge système.
"""
import argparse
import requests
import time
import psutil

def monitor(api_url, interval):
    while True:
        start = time.time()
        try:
            resp = requests.get(api_url)
            latency = time.time() - start
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Latence API: {latency:.3f}s, Statut: {resp.status_code}")
        except Exception as e:
            print(f"Erreur API: {e}")
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        print(f"CPU: {cpu}%, RAM: {mem}%")
        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--interval', type=int, default=60)
    parser.add_argument('--api_url', type=str, default='http://localhost:5000/api/health')
    args = parser.parse_args()
    monitor(args.api_url, args.interval)
