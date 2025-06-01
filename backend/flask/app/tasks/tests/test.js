// Tests avancés pour la gestion des tâches (Node.js)
const { scheduleTask, listTasks } = require('../service');

describe('Tasks: scheduleTask', () => {
  it('should schedule a backup task for tenant', async () => {
    const res = await scheduleTask('tenant1', 'backup', '2025-05-25T00:00:00Z');
    expect(res.success).toBe(true);
  });
});

describe('Tasks: listTasks', () => {
  it('should list tasks for tenant', async () => {
    const res = await listTasks('tenant1');
    expect(Array.isArray(res)).toBe(true);
  });
});
// ...autres tests : plugins, audit, multitenancy, i18n, sécurité, e2e, multilingue...
