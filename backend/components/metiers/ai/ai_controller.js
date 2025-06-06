import { v4 as uuidv4 } from 'uuid';
import { accessibilityCheck, aiSuggest, anonymize, auditLog, exportData, i18n, pluginHook, rbacCheck, seoLog, tenantCheck, validateInput } from '../../../../middleware/ultra_advanced.js';

const models = [];

/**
 * Liste tous les modèles IA (avec audit, i18n, accessibilité, SEO, plugins)
 */
export async function getAIModels(req, res) {
  auditLog('ai_list', req.user, req.tenant);
  accessibilityCheck(req, 'ai_list');
  seoLog('ai_list', req);
  pluginHook('beforeList', req, models);
  res.json({ models: models.map(m => i18n(m, req.lang)) });
}

/**
 * Crée un modèle IA (validation, RGPD, plugins, audit, IA, multitenancy)
 */
export async function createAIModel(req, res) {
  rbacCheck(req.user, ['admin', 'data_scientist']);
  tenantCheck(req.user, req.body.tenant);
  validateInput(req.body, 'AIModel');
  const aiMeta = aiSuggest('ai', req.body);
  const model = { id: uuidv4(), ...req.body, aiMetadata: aiMeta, createdAt: new Date().toISOString(), updatedAt: new Date().toISOString() };
  models.push(model);
  auditLog('ai_create', req.user, req.tenant, model);
  pluginHook('afterCreate', req, model);
  res.status(201).json({ model: i18n(model, req.lang) });
}

/**
 * Met à jour un modèle IA (validation, RGPD, plugins, audit, multitenancy)
 */
export async function updateAIModel(req, res) {
  rbacCheck(req.user, ['admin', 'data_scientist']);
  tenantCheck(req.user, req.body.tenant);
  validateInput(req.body, 'AIModel');
  const idx = models.findIndex(m => m.id === req.params.id);
  if (idx === -1) return res.status(404).json({ error: 'Not found' });
  models[idx] = { ...models[idx], ...req.body, updatedAt: new Date().toISOString() };
  auditLog('ai_update', req.user, req.tenant, models[idx]);
  pluginHook('afterUpdate', req, models[idx]);
  res.json({ model: i18n(models[idx], req.lang) });
}

/**
 * Supprime un modèle IA (audit, RGPD, anonymisation, plugins)
 */
export async function deleteAIModel(req, res) {
  rbacCheck(req.user, ['admin']);
  const idx = models.findIndex(m => m.id === req.params.id);
  if (idx === -1) return res.status(404).json({ error: 'Not found' });
  const deleted = anonymize(models.splice(idx, 1)[0]);
  auditLog('ai_delete', req.user, req.tenant, deleted);
  pluginHook('afterDelete', req, deleted);
  res.json({ deleted });
}

/**
 * Exporte les modèles IA (RGPD, audit, plugins)
 */
export async function exportAIModels(req, res) {
  rbacCheck(req.user, ['admin', 'data_scientist']);
  auditLog('ai_export', req.user, req.tenant);
  const data = exportData(models, req.lang);
  pluginHook('afterExport', req, data);
  res.attachment('ai_models.json').json(data);
}
