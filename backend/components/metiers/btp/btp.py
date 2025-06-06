# Module principal BTP

def get_chantier_info(chantier_id):
    # Logique métier avancée pour récupérer les infos d’un chantier
    return {
        'id': chantier_id,
        'nom': f'Chantier {chantier_id}',
        'etat': 'en_cours',
        'responsable': 'Chef BTP',
        'date_debut': '2025-01-01',
        'date_fin': None
    }

def planifier_chantier(data):
    # Logique de planification avancée
    return {'status': 'success', 'chantier': data}

def anonymiser_chantier(chantier):
    # Anonymisation RGPD
    c = chantier.copy()
    c['responsable'] = 'ANONYMISED'
    return c

def exporter_chantier(chantier, format='json'):
    if format == 'json':
        import json
        return json.dumps(chantier, ensure_ascii=False)
    if format == 'csv':
        import csv, io
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=chantier.keys())
        writer.writeheader()
        writer.writerow(chantier)
        return output.getvalue()
    return str(chantier)
