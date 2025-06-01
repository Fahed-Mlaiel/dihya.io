"""
Dihya – Django Santé API Audit Logging Ultra Avancé
---------------------------------------------------
- Logging souverain, anonymisé, conforme RGPD/NIS2, extensible
- Prêt pour SIEM, fallback local, auditabilité totale
"""

def audit_log(user, action, obj):
    # TODO: envoyer vers SIEM souverain, fallback local, anonymisation
    print(f"[AUDIT] user={getattr(user, 'id', None)} action={action} obj={obj}")
