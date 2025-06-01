// Tests unitaires & intégration – Utils
import { UtilsController } from './utils_controller.js';
describe('UtilsController', () => {
  it('createUtil – doit créer un utilitaire', async () => {
    const req = { body: { name: 'Test' }, user: { role: 'admin' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    await UtilsController.createUtil(req, res);
    expect(res.status).toHaveBeenCalledWith(201);
    expect(res.json).toHaveBeenCalledWith({ success: true });
  });
});
