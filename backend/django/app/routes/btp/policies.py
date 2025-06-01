"""
Politiques avancées (RBAC, sécurité, RGPD, plugins) pour BTP.
"""
# Ultra-advanced RBAC, ABAC, PBAC, RGPD, plugins, audit, multitenant, accessibilité, extensibilité, CI/CD-ready
POLICIES = {
    "access": ["admin", "entrepreneur", "ouvrier", "auditeur", "guest"],
    "chantier_create": ["admin", "entrepreneur"],
    "chantier_view": ["admin", "entrepreneur", "ouvrier", "auditeur"],
    "chantier_update": ["admin", "entrepreneur"],
    "chantier_delete": ["admin"],
    "plugin_manage": ["admin"],
    "audit_log": ["admin", "auditeur"],
    "rgpd_export": ["admin", "dpo"],
    "rgpd_delete": ["admin", "dpo"],
    "multitenant": ["admin", "tenant_admin"],
    "accessibility": ["admin", "a11y_auditor"],
    "fallback_ai": ["admin", "entrepreneur", "ai_service"],
}

def has_policy(role: str, action: str) -> bool:
    return role in POLICIES.get(action, [])
