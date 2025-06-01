// Modèles de validation pour les templates Dihya Coding (Joi)
const Joi = require('joi');

const SEOInputModel = Joi.object({
  title: Joi.string().min(1).max(255).required(),
  description: Joi.string().min(1).max(1024).required(),
  locale: Joi.string().required(),
  tenant: Joi.string().required(),
  meta: Joi.object().optional()
});

const ServiceInputModel = Joi.object({
  name: Joi.string().min(1).max(255).required(),
  description: Joi.string().min(1).max(1024).required(),
  locale: Joi.string().required(),
  tenant: Joi.string().required(),
  details: Joi.object().optional()
});

const SportInputModel = Joi.object({
  name: Joi.string().min(1).max(255).required(),
  description: Joi.string().min(1).max(1024).required(),
  locale: Joi.string().required(),
  tenant: Joi.string().required(),
  details: Joi.object().optional()
});

const TourismeInputModel = Joi.object({
  name: Joi.string().min(1).max(255).required(),
  description: Joi.string().min(1).max(1024).required(),
  locale: Joi.string().required(),
  tenant: Joi.string().required(),
  details: Joi.object().optional()
});

const TransportInputModel = Joi.object({
  name: Joi.string().min(1).max(255).required(),
  description: Joi.string().min(1).max(1024).required(),
  locale: Joi.string().required(),
  tenant: Joi.string().required(),
  details: Joi.object().optional()
});

module.exports = {
  SEOInputModel,
  ServiceInputModel,
  SportInputModel,
  TourismeInputModel,
  TransportInputModel
};
