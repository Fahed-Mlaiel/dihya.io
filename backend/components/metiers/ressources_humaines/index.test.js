// Tests unitaires & intégration – RH
import { RHController } from './ressources_humaines_controller.js';
describe('RHController', () => {
  it('createEmployee – doit créer un employé', async () => {
    const req = { body: { name: 'Test' }, user: { role: 'admin' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    await RHController.createEmployee(req, res);
    expect(res.status).toHaveBeenCalledWith(201);
    expect(res.json).toHaveBeenCalledWith({ success: true });
  });
});
