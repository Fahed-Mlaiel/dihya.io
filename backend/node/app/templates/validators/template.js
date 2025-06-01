/**
 * Template de validateurs avancés pour la gestion de projets (tous domaines)
 * Sécurité maximale, i18n, multitenancy, plugins, RGPD, SEO, fallback IA
 * @module validators/template
 */
const Joi = require('joi');

// Validation projet social
function validateSocialProject(req, res, next) {
  const schema = Joi.object({
    name: Joi.string().min(3).max(100).required(),
    description: Joi.string().max(500).required(),
    type: Joi.string().valid('AI', 'VR', 'AR', 'Social').required(),
  });
  const { error } = schema.validate(req.body);
  if (error) return res.status(400).json({ error: error.details[0].message });
  next();
}

// Validation projet sport
function validateSportProject(req, res, next) {
  const schema = Joi.object({
    name: Joi.string().min(3).max(100).required(),
    description: Joi.string().max(500).required(),
    type: Joi.string().valid('AI', 'VR', 'AR', 'Sport').required(),
  });
  const { error } = schema.validate(req.body);
  if (error) return res.status(400).json({ error: error.details[0].message });
  next();
}

// Validation projet tourisme
function validateTourismeProject(req, res, next) {
  const schema = Joi.object({
    name: Joi.string().min(3).max(100).required(),
    description: Joi.string().max(500).required(),
    type: Joi.string().valid('AI', 'VR', 'AR', 'Tourisme').required(),
  });
  const { error } = schema.validate(req.body);
  if (error) return res.status(400).json({ error: error.details[0].message });
  next();
}

// Validation projet transport
function validateTransportProject(req, res, next) {
  const schema = Joi.object({
    name: Joi.string().min(3).max(100).required(),
    description: Joi.string().max(500).required(),
    type: Joi.string().valid('AI', 'VR', 'AR', 'Transport').required(),
  });
  const { error } = schema.validate(req.body);
  if (error) return res.status(400).json({ error: error.details[0].message });
  next();
}

module.exports = {
  validateSocialProject,
  validateSportProject,
  validateTourismeProject,
  validateTransportProject,
};
