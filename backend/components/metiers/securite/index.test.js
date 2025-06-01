// Tests unitaires & intégration – Securite
import { SecuriteController } from './securite_controller.js';
describe('SecuriteController', () => {
  it('createIncident – doit créer un incident', async () => {
    const req = { body: { name: 'Test' }, user: { role: 'admin' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    await SecuriteController.createIncident(req, res);
    expect(res.status).toHaveBeenCalledWith(201);
    expect(res.json).toHaveBeenCalledWith({ success: true });
  });
});
