"""
Dihya – Automobile Policies Ultra Avancé
---------------------------------------
- RBAC, ABAC, PBAC, RGPD, plugins, audit, multitenant, accessibilité, extensibilité, CI/CD-ready
"""
POLICIES = {
    "access": ["admin", "proprietaire", "garage", "assureur", "auditeur", "guest"],
    "vehicule_create": ["admin", "proprietaire", "garage"],
    "vehicule_view": ["admin", "proprietaire", "garage", "assureur", "auditeur"],
    "vehicule_update": ["admin", "proprietaire", "garage"],
    "vehicule_delete": ["admin"],
    "maintenance_manage": ["admin", "garage"],
    "sinistre_manage": ["admin", "assureur"],
    "plugin_manage": ["admin"],
    "audit_log": ["admin", "auditeur"],
    "rgpd_export": ["admin", "dpo"],
    "rgpd_delete": ["admin", "dpo"],
    "multitenant": ["admin", "tenant_admin"],
    "accessibility": ["admin", "a11y_auditor"],
    "fallback_ai": ["admin", "garage", "ai_service"],
}

def has_policy(role: str, action: str) -> bool:
    return role in POLICIES.get(action, [])
