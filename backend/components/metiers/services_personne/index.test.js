// Tests unitaires & intégration – Services Personne
import { ServicesPersonneController } from './services_personne_controller.js';
describe('ServicesPersonneController', () => {
  it('createService – doit créer un service', async () => {
    const req = { body: { name: 'Test' }, user: { role: 'admin' } };
    const res = { status: jest.fn().mockReturnThis(), json: jest.fn() };
    await ServicesPersonneController.createService(req, res);
    expect(res.status).toHaveBeenCalledWith(201);
    expect(res.json).toHaveBeenCalledWith({ success: true });
  });
});
