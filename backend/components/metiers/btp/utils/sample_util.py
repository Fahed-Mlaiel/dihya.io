# Utilitaire Python exemple pour BTP
def chantier_status(chantier):
    return chantier.get('etat', 'inconnu')

def anonymiser_chantier(chantier):
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
