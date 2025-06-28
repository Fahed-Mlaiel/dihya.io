# exporter_helper.py
# Helper d'export Python pour Health – exemple clé en main
import json


def format_export_json(data):
    """
    Formate les données à exporter en JSON compacté
    """
    return json.dumps(data)
