"""
exporter.py – Exportation avancée des données environnementales (Python)
"""
import json, csv

def export_to_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return file_path

def export_to_csv(data, file_path):
    if not data:
        return file_path
    keys = data[0].keys()
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    return file_path
