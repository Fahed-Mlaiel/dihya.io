"""
Politiques avancées (RBAC, sécurité, RGPD, plugins) pour crypto.
"""
POLICIES = {
    "access": ["admin", "user", "invite"],
    "export": ["admin"],
    "plugin_manage": ["admin"],
    "audit": ["admin", "user"],
}
