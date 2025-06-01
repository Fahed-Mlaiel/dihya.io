// Tests unitaires & intégration – Mode
import { ModeManager } from './index.js';
describe('ModeManager', () => {
  it('addCollection – doit ajouter une collection', async () => {
    const mode = new ModeManager({ lang: 'fr', role: 'admin' });
    const res = await mode.addCollection({ name: 'Test' });
    expect(res.success).toBe(true);
    expect(res.collection).toBeDefined();
  });
  it('exportData – doit exporter les données', async () => {
    const mode = new ModeManager();
    const data = await mode.exportData();
    expect(Array.isArray(data)).toBe(true);
  });
});
