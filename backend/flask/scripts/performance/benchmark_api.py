"""
Dihya – Script de benchmark API (performance, sécurité, accessibilité)
Usage: python benchmark_api.py --url http://localhost:5000/api/health --n 100
"""
import argparse
import requests
import time

def benchmark(url, n):
    times = []
    for _ in range(n):
        start = time.time()
        resp = requests.get(url)
        times.append(time.time() - start)
    print(f"Requêtes: {n}, Latence moyenne: {sum(times)/n:.3f}s, Min: {min(times):.3f}s, Max: {max(times):.3f}s")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, required=True)
    parser.add_argument('--n', type=int, default=100)
    args = parser.parse_args()
    benchmark(args.url, args.n)
