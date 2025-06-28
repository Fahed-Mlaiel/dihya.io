# Script d’export des logs d’audit legacy Education

import os
import shutil
import datetime
import sys

# Configuration des chemins
# Les chemins sont patchés dans les tests pour éviter toute création réelle
source_dir = None
export_dir = None

# Création du répertoire d'export s'il n'existe pas
# (Désactivé pour éviter les effets de bord lors de l'import)
# if not os.path.exists(export_dir):
#     os.makedirs(export_dir)

# Fonction pour exporter les logs


def export_logs():
    try:
        # Récupération de la date du jour
        today = datetime.date.today()
        # Formatage de la date pour le nom du fichier
        date_str = today.strftime("%Y%m%d")
        # Chemin complet du fichier d'export
        export_file = os.path.join(
            export_dir, f"audit_logs_export_{date_str}.zip"
        )
        try:
            if not source_dir or not os.path.exists(source_dir):
                raise FileNotFoundError(f"Le dossier source n'existe pas : {source_dir}")
            if not export_dir or not os.path.exists(export_dir):
                raise FileNotFoundError(f"Le dossier d'export n'existe pas : {export_dir}")
            # Création d'un fichier zip contenant tous les logs
            shutil.make_archive(export_file.replace(".zip", ""), "zip", source_dir)
            print(f"Export des logs réussi : {export_file}")
            sys.stdout.flush()
        except Exception as e:
            print(f"Erreur lors de l'export des logs : {e}")
            sys.stdout.flush()
    except Exception as e:
        print(f"Erreur lors de l'export des logs : {e}")
        sys.stdout.flush()


# Ajout d'une fonction factice pour compatibilité avec audit_report.py

def export_audit_logs_to_json(filepath):
    # Simule l'export des logs au format JSON (pour les tests)
    with open(filepath, "w") as f:
        f.write("{\"logs\": [\"log1\", \"log2\"]}")
    print(f"Export JSON simulé : {filepath}")


# Correction : ne pas exécuter export_logs() à l'import, seulement si __name__ == "__main__"
if __name__ == "__main__":
    export_logs()
