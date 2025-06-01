// Tests unitaires & intégration – Sante
import { SanteController } from './sante_controller.js';
describe('SanteController', () => {
  it('createDossier – doit créer un dossier', async () => {
    const req = { body: { name: 'Test' }, user: { role: 'admin' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    await SanteController.createDossier(req, res);
    expect(res.status).toHaveBeenCalledWith(201);
    expect(res.json).toHaveBeenCalledWith({ success: true });
  });
});
