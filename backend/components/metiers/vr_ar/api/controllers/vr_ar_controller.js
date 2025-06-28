// vr_ar_controller.js – Contrôleur ultra avancé API vr_ar (JS)
const db = require('../db/db');
const { validatevr_arEntity } = require('../validators/validators');
const { auditEntity } = require('../audit/audit');
const { rgpdSanitize } = require('../rgpd/rgpd');
const { checkAccessibility } = require('../accessibility/accessibility');
const { beforeAction, afterAction } = require('../hooks/hooks');

const vr_arController = {
  async getById(id) {
    beforeAction('read', { id });
    let entity = db.findById('vr_ar', id);
    if (!entity) return null;
    entity = rgpdSanitize(entity);
    checkAccessibility(entity);
    auditEntity(entity, 'read');
    afterAction('read', entity);
    return entity;
  },
  async create(data) {
    beforeAction('create', data);
    validatevr_arEntity(data);
    const created = db.insert('vr_ar', data);
    auditEntity(created, 'create');
    afterAction('create', created);
    return rgpdSanitize(created);
  },
  async update(id, data) {
    beforeAction('update', { id, ...data });
    validatevr_arEntity(data);
    const updated = db.update('vr_ar', id, data);
    auditEntity(updated, 'update');
    afterAction('update', updated);
    return rgpdSanitize(updated);
  },
  async delete(id) {
    beforeAction('delete', { id });
    const deleted = db.delete('vr_ar', id);
    auditEntity({ id }, 'delete');
    afterAction('delete', { id });
    return deleted;
  }
};

module.exports = vr_arController;
