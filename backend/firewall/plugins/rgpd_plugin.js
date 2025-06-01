// rgpd_plugin.js – Plugin RGPD/anonymisation (Dihya)
module.exports = function rgpdPlugin(req, res, next) {
  // Exemple d’anonymisation de log
  if (req.user) req.user = { ...req.user, email: undefined };
  next();
};
