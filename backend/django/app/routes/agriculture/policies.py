"""
Dihya – Agriculture Policies Ultra Avancé
----------------------------------------
- RBAC, ABAC, PBAC, RGPD, plugins, audit, multitenant, accessibilité, extensibilité, CI/CD-ready
"""
POLICIES = {
    "access": ["admin", "agriculteur", "conseiller", "auditeur", "guest"],
    "exploit_create": ["admin", "agriculteur"],
    "exploit_view": ["admin", "agriculteur", "conseiller", "auditeur"],
    "exploit_update": ["admin", "agriculteur"],
    "exploit_delete": ["admin"],
    "capteur_manage": ["admin", "agriculteur"],
    "alert_manage": ["admin", "conseiller"],
    "plugin_manage": ["admin"],
    "audit_log": ["admin", "auditeur"],
    "rgpd_export": ["admin", "dpo"],
    "rgpd_delete": ["admin", "dpo"],
    "multitenant": ["admin", "tenant_admin"],
    "accessibility": ["admin", "a11y_auditor"],
    "fallback_ai": ["admin", "agriculteur", "ai_service"],
}

def has_policy(role: str, action: str) -> bool:
    return role in POLICIES.get(action, [])
