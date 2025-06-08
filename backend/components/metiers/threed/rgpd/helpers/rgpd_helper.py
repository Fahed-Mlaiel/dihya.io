# rgpd_helper.py – Helper RGPD (Python)
def mask_pii(data):
    """Exemple de helper RGPD"""
    # TODO: Implémenter la logique de masquage RGPD
    masked = dict(data)
    masked['masked'] = True
    return masked
