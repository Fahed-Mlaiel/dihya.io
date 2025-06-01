"""
Politiques avancées (RBAC, sécurité, RGPD, plugins) pour banque/finance.
"""
# Ultra-advanced RBAC, ABAC, PBAC, RGPD, plugins, audit, multitenant, accessibilité, extensibilité, CI/CD-ready
POLICIES = {
    "access": ["admin", "conseiller", "client", "auditeur", "guest"],
    "compte_create": ["admin", "conseiller"],
    "compte_view": ["admin", "conseiller", "client", "auditeur"],
    "compte_update": ["admin", "conseiller"],
    "compte_delete": ["admin"],
    "transaction_manage": ["admin", "conseiller"],
    "plugin_manage": ["admin"],
    "audit_log": ["admin", "auditeur"],
    "rgpd_export": ["admin", "dpo"],
    "rgpd_delete": ["admin", "dpo"],
    "multitenant": ["admin", "tenant_admin"],
    "accessibility": ["admin", "a11y_auditor"],
    "fallback_ai": ["admin", "conseiller", "ai_service"],
}

def has_policy(role: str, action: str) -> bool:
    return role in POLICIES.get(action, [])
