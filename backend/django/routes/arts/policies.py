"""
Politiques avancées (RBAC, sécurité, RGPD, plugins) pour arts.
"""
POLICIES = {
    "access": ["admin", "user", "invite"],
    "export": ["admin"],
    "plugin_manage": ["admin"],
    "audit": ["admin", "user"],
}
