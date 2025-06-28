// health_controller.js – Contrôleur ultra avancé API Health (JS)
const db = require('../db/db');
const { validatehealthEntity } = require('../validators/validators');
const { auditEntity } = require('../audit/audit');
const { rgpdSanitize } = require('../rgpd/rgpd');
const { checkAccessibility } = require('../accessibility/accessibility');
const { beforeAction, afterAction } = require('../hooks/hooks');

const HealthController = {
  async getById(id) {
    beforeAction('read', { id });
    let entity = db.findById('health', id);
    if (!entity) return null;
    entity = rgpdSanitize(entity);
    checkAccessibility(entity);
    auditEntity(entity, 'read');
    afterAction('read', entity);
    return entity;
  },
  async create(data) {
    beforeAction('create', data);
    validatehealthEntity(data);
    const created = db.insert('health', data);
    auditEntity(created, 'create');
    afterAction('create', created);
    return rgpdSanitize(created);
  },
  async update(id, data) {
    beforeAction('update', { id, ...data });
    validatehealthEntity(data);
    const updated = db.update('health', id, data);
    auditEntity(updated, 'update');
    afterAction('update', updated);
    return rgpdSanitize(updated);
  },
  async delete(id) {
    beforeAction('delete', { id });
    const deleted = db.delete('health', id);
    auditEntity({ id }, 'delete');
    afterAction('delete', { id });
    return deleted;
  }
};

module.exports = HealthController;
