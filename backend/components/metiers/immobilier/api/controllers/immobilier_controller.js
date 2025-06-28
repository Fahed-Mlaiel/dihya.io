// immobilier_controller.js – Contrôleur ultra avancé API Immobilier (JS)
const db = require('../db/db');
const { validateimmobilierEntity } = require('../validators/validators');
const { auditEntity } = require('../audit/audit');
const { rgpdSanitize } = require('../rgpd/rgpd');
const { checkAccessibility } = require('../accessibility/accessibility');
const { beforeAction, afterAction } = require('../hooks/hooks');

const ImmobilierController = {
  async getById(id) {
    beforeAction('read', { id });
    let entity = db.findById('immobilier', id);
    if (!entity) return null;
    entity = rgpdSanitize(entity);
    checkAccessibility(entity);
    auditEntity(entity, 'read');
    afterAction('read', entity);
    return entity;
  },
  async create(data) {
    beforeAction('create', data);
    validateimmobilierEntity(data);
    const created = db.insert('immobilier', data);
    auditEntity(created, 'create');
    afterAction('create', created);
    return rgpdSanitize(created);
  },
  async update(id, data) {
    beforeAction('update', { id, ...data });
    validateimmobilierEntity(data);
    const updated = db.update('immobilier', id, data);
    auditEntity(updated, 'update');
    afterAction('update', updated);
    return rgpdSanitize(updated);
  },
  async delete(id) {
    beforeAction('delete', { id });
    const deleted = db.delete('immobilier', id);
    auditEntity({ id }, 'delete');
    afterAction('delete', { id });
    return deleted;
  }
};

module.exports = ImmobilierController;
