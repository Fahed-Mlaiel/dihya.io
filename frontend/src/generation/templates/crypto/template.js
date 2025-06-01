// template.js
/**
 * Générateur de projet crypto ultra sécurisé, multilingue, extensible.
 * @module templates/crypto/template
 * @param {object} req - Requête Express (body: {name, lang, tenant, userRole, features})
 * @param {object} res - Réponse Express
 * @param {function} next - Middleware suivant
 * @returns {void}
 * @example
 *   generateCryptoProject(req, res, next)
 */
const { i18n } = require('../../../../utils/i18n');
const { validateCryptoInput } = require('../../../../utils/validation');
const { auditLog } = require('../../../../utils/audit');
const { applyPlugins } = require('../../../../utils/plugins');
const { getAIService } = require('../../../../utils/ai');

async function generateCryptoProject(req, res, next) {
  try {
    validateCryptoInput(req.body);
    const lang = req.body.lang || 'fr';
    const project = {
      name: req.body.name,
      lang,
      tenant: req.body.tenant,
      userRole: req.body.userRole,
      features: req.body.features,
      security: {
        cors: true,
        jwt: true,
        waf: true,
        antiDDOS: true,
        audit: true,
        rgpd: true,
      },
      plugins: applyPlugins('crypto', req.body.features),
      ai: await getAIService(['LLaMA', 'Mixtral', 'Mistral']),
      i18n: i18n(lang),
      createdAt: new Date(),
    };
    auditLog('crypto_project_generated', { project, user: req.user });
    res.status(201).json({ project });
  } catch (err) {
    auditLog('crypto_project_error', { error: err, user: req.user });
    next(err);
  }
}

module.exports = { generateCryptoProject };
