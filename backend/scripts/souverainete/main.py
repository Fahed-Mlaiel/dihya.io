"""
Script souveraineté numérique pour Dihya (audit, RGPD, fallback IA open source)
"""
import logging
from backend.souverainete import check_souverainete, export_souverainete_log

def main():
    """
    Vérifie la souveraineté numérique (données, IA, plugins, logs).
    """
    logging.basicConfig(level=logging.INFO)
    logging.info("Vérification de la souveraineté numérique Dihya...")
    souverainete_result = check_souverainete()
    export_souverainete_log(souverainete_result, "souverainete_report.txt")
    logging.info("Souveraineté vérifiée. Rapport exporté.")

if __name__ == "__main__":
    main()
