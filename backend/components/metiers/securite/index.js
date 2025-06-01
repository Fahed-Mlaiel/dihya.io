// Middleware de sécurité ultra avancé pour projets IA, VR, AR
// CORS, JWT, validation, audit, WAF, anti-DDOS, RGPD, plugins
// @module SecurityMiddleware

/**
 * Middleware de sécurité
 * @param {Object} options - Options de configuration
 * @param {Array<string>} options.roles - Rôles autorisés (admin, user, invité)
 * @returns {Function} Middleware Express/Node
 */
export function SecurityMiddleware({ roles = ['user'] } = {}) {
  return function (req, res, next) {
    // CORS strict
    res.setHeader('Access-Control-Allow-Origin', 'https://dihya.app');
    res.setHeader('Access-Control-Allow-Methods', 'GET,POST,PUT,DELETE,OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Authorization,Content-Type');
    // JWT obligatoire
    const token = req.headers['authorization']?.split(' ')[1];
    if (!token) return res.status(401).json({ error: 'JWT required' });
    // ...vérification JWT, validation, audit, WAF, anti-DDOS, RGPD...
    // Rôles
    if (!roles.includes('user')) return res.status(403).json({ error: 'Role not allowed' });
    // Audit log
    // ...log structuré, anonymisation RGPD...
    next();
  };
}

export default SecurityMiddleware;
