/**
 * Validation avancée des entrées VR/AR (REST, GraphQL, sécurité, RGPD, i18n)
 * @module validators/vr_ar
 * @author Dihya Team
 * @since 2025-05-25
 */
const Joi = require('joi');

/**
 * Schéma de validation pour la création/modification d'une entrée VR/AR
 */
const vrArSchema = Joi.object({
  name: Joi.string().min(2).max(128).required(),
  description: Joi.string().max(2048).allow(''),
  type: Joi.string().valid('VR', 'AR', 'Mixed').required(),
  owner: Joi.string().required(),
  lang: Joi.string().valid('fr','en','ar','ber','de','zh','ja','ko','nl','he','fa','hi','es').default('fr')
});

/**
 * Middleware de validation pour Express
 */
function validateVRARInput(req, res, next) {
  const { error } = vrArSchema.validate(req.body);
  if (error) {
    return res.status(400).json({ success: false, error: req.t('error.invalid_input'), details: error.details });
  }
  next();
}

module.exports = { validateVRARInput, vrArSchema };
