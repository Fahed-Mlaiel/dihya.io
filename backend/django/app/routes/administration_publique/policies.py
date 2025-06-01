"""
Dihya – Administration Publique Policies Ultra Avancé
----------------------------------------------------
- RBAC, ABAC, PBAC, RGPD, plugins, audit, multitenant, accessibilité, extensibilité, CI/CD-ready
"""
POLICIES = {
    "access": ["admin", "agent", "usager", "auditeur", "guest"],
    "demarche_create": ["admin", "agent"],
    "demarche_view": ["admin", "agent", "usager", "auditeur"],
    "demarche_update": ["admin", "agent"],
    "demarche_delete": ["admin"],
    "document_export": ["admin", "agent", "auditeur"],
    "audit_log": ["admin", "auditeur"],
    "plugin_manage": ["admin"],
    "rgpd_export": ["admin", "dpo"],
    "rgpd_delete": ["admin", "dpo"],
    "multitenant": ["admin", "tenant_admin"],
    "accessibility": ["admin", "a11y_auditor"],
    "fallback_ai": ["admin", "agent", "ai_service"],
}

def has_policy(role: str, action: str) -> bool:
    return role in POLICIES.get(action, [])
