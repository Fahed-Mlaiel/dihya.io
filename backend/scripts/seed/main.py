"""
Script de seed avancé pour Dihya (données multilingues, sécurité, RGPD)
"""
import logging
from backend.seed import seed_all, export_seed_log

def main():
    """
    Lance le seed complet du backend Dihya (données, utilisateurs, rôles, plugins).
    """
    logging.basicConfig(level=logging.INFO)
    logging.info("Démarrage du seed Dihya...")
    seed_result = seed_all()
    export_seed_log(seed_result, "seed_report.txt")
    logging.info("Seed terminé. Rapport exporté.")

if __name__ == "__main__":
    main()
