"""
Dihya – Assurance Policies Ultra Avancé
--------------------------------------
- RBAC, ABAC, PBAC, RGPD, plugins, audit, multitenant, accessibilité, extensibilité, CI/CD-ready
"""
POLICIES = {
    "access": ["admin", "agent", "assure", "auditeur", "guest"],
    "contrat_create": ["admin", "agent"],
    "contrat_view": ["admin", "agent", "assure", "auditeur"],
    "contrat_update": ["admin", "agent"],
    "contrat_delete": ["admin"],
    "sinistre_manage": ["admin", "agent"],
    "plugin_manage": ["admin"],
    "audit_log": ["admin", "auditeur"],
    "rgpd_export": ["admin", "dpo"],
    "rgpd_delete": ["admin", "dpo"],
    "multitenant": ["admin", "tenant_admin"],
    "accessibility": ["admin", "a11y_auditor"],
    "fallback_ai": ["admin", "agent", "ai_service"],
}

def has_policy(role: str, action: str) -> bool:
    return role in POLICIES.get(action, [])
