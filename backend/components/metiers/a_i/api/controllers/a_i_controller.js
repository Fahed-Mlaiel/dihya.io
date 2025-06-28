// a_i_controller.js – Contrôleur ultra avancé API A_I (JS)
const db = require('../db/db');
const { validatea_iEntity } = require('../validators/validators');
const { auditEntity } = require('../audit/audit');
const { rgpdSanitize } = require('../rgpd/rgpd');
const { checkAccessibility } = require('../accessibility/accessibility');
const { beforeAction, afterAction } = require('../hooks/hooks');

const A_IController = {
  async getById(id) {
    beforeAction('read', { id });
    let entity = db.findById('a_i', id);
    if (!entity) return null;
    entity = rgpdSanitize(entity);
    checkAccessibility(entity);
    auditEntity(entity, 'read');
    afterAction('read', entity);
    return entity;
  },
  async create(data) {
    beforeAction('create', data);
    validatea_iEntity(data);
    const created = db.insert('a_i', data);
    auditEntity(created, 'create');
    afterAction('create', created);
    return rgpdSanitize(created);
  },
  async update(id, data) {
    beforeAction('update', { id, ...data });
    validatea_iEntity(data);
    const updated = db.update('a_i', id, data);
    auditEntity(updated, 'update');
    afterAction('update', updated);
    return rgpdSanitize(updated);
  },
  async delete(id) {
    beforeAction('delete', { id });
    const deleted = db.delete('a_i', id);
    auditEntity({ id }, 'delete');
    afterAction('delete', { id });
    return deleted;
  }
};

module.exports = A_IController;
