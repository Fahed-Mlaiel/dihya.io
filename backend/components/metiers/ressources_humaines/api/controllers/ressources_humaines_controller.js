// ressources_humaines_controller.js – Contrôleur ultra avancé API Ressources_humaines (JS)
const db = require('../db/db');
const { validateressources_humainesEntity } = require('../validators/validators');
const { auditEntity } = require('../audit/audit');
const { rgpdSanitize } = require('../rgpd/rgpd');
const { checkAccessibility } = require('../accessibility/accessibility');
const { beforeAction, afterAction } = require('../hooks/hooks');

const Ressources_humainesController = {
  async getById(id) {
    beforeAction('read', { id });
    let entity = db.findById('ressources_humaines', id);
    if (!entity) return null;
    entity = rgpdSanitize(entity);
    checkAccessibility(entity);
    auditEntity(entity, 'read');
    afterAction('read', entity);
    return entity;
  },
  async create(data) {
    beforeAction('create', data);
    validateressources_humainesEntity(data);
    const created = db.insert('ressources_humaines', data);
    auditEntity(created, 'create');
    afterAction('create', created);
    return rgpdSanitize(created);
  },
  async update(id, data) {
    beforeAction('update', { id, ...data });
    validateressources_humainesEntity(data);
    const updated = db.update('ressources_humaines', id, data);
    auditEntity(updated, 'update');
    afterAction('update', updated);
    return rgpdSanitize(updated);
  },
  async delete(id) {
    beforeAction('delete', { id });
    const deleted = db.delete('ressources_humaines', id);
    auditEntity({ id }, 'delete');
    afterAction('delete', { id });
    return deleted;
  }
};

module.exports = Ressources_humainesController;
